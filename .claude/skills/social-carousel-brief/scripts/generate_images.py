#!/usr/bin/env python3
"""Generate illustration art with the OpenAI Images API from a prompts file.

Usage:
  python3 -I generate_images.py PROMPTS.json --out DIR [--refs DIR] [--only ID ...]
                                [--model NAME] [--quality low|medium|high] [--dry-run]

PROMPTS.json is a list of objects:
  {"id": "01-cover", "prompt": "...", "size": "1024x1536",
   "background": "transparent", "quality": "high"}
  size:       1024x1024, 1024x1536 or 1536x1024 (default 1024x1536)
  background: transparent or opaque (default opaque)
  quality:    low, medium or high (default high; --quality overrides)

--refs DIR sends up to 5 style reference images (png, jpg, webp, sorted by name)
with every request through the image edit endpoint, so the look stays consistent.
The API keeps no memory between calls, unlike a ChatGPT thread.

Output: DIR/<id>.png and DIR/manifest.json (one entry per image with prompt,
model, size, references, date and ai_generated: true). Existing entries with the
same id are replaced.

The key is read from the OPENAI_API_KEY environment variable and is never printed.
The model defaults to gpt-image-1 and can be set with --model or OPENAI_IMAGE_MODEL.
Needs the requests library.
"""
import argparse
import base64
import datetime
import json
import mimetypes
import os
import re
import sys
import time

import requests

API = "https://api.openai.com/v1/images"
DEFAULT_MODEL = os.environ.get("OPENAI_IMAGE_MODEL", "gpt-image-1")
SIZES = {"1024x1024", "1024x1536", "1536x1024"}
QUALITIES = {"low", "medium", "high"}
BACKGROUNDS = {"transparent", "opaque"}
REF_EXTS = {".png", ".jpg", ".jpeg", ".webp"}
MAX_REFS = 5
RETRIES = 3


def die(msg):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(1)


def load_items(path):
    try:
        with open(path, encoding="utf-8") as f:
            items = json.load(f)
    except (OSError, ValueError) as e:
        die(f"cannot read {path}: {e}")
    if not isinstance(items, list) or not items:
        die("prompts file must be a non-empty JSON list")
    seen = set()
    for i, it in enumerate(items):
        for key in ("id", "prompt"):
            if not isinstance(it.get(key), str) or not it[key].strip():
                die(f"item {i}: missing {key}")
        if it["id"] in seen:
            die(f"duplicate id {it['id']}")
        seen.add(it["id"])
        it.setdefault("size", "1024x1536")
        it.setdefault("background", "opaque")
        if it["size"] not in SIZES:
            die(f"{it['id']}: size must be one of {sorted(SIZES)}")
        if it["background"] not in BACKGROUNDS:
            die(f"{it['id']}: background must be one of {sorted(BACKGROUNDS)}")
        if it.get("quality", "high") not in QUALITIES:
            die(f"{it['id']}: quality must be one of {sorted(QUALITIES)}")
    return items


def load_refs(folder):
    if not folder:
        return []
    if not os.path.isdir(folder):
        die(f"reference folder not found: {folder}")
    names = sorted(n for n in os.listdir(folder) if os.path.splitext(n)[1].lower() in REF_EXTS)
    if not names:
        print(f"warning: no reference images in {folder}; style may drift", file=sys.stderr)
    return [os.path.join(folder, n) for n in names[:MAX_REFS]]


def call(session, headers, item, model, quality, refs):
    fields = {
        "model": model,
        "prompt": item["prompt"],
        "size": item["size"],
        "quality": quality,
        "background": item["background"],
        "output_format": "png",
        "n": "1",
    }
    for attempt in range(1, RETRIES + 1):
        if refs:
            files = []
            for p in refs:
                mime = mimetypes.guess_type(p)[0] or "image/png"
                files.append(("image[]", (os.path.basename(p), open(p, "rb"), mime)))
            try:
                resp = session.post(f"{API}/edits", headers=headers, data=fields, files=files, timeout=300)
            finally:
                for _, (_, fh, _) in files:
                    fh.close()
        else:
            resp = session.post(f"{API}/generations", headers=headers, json=fields, timeout=300)
        if resp.status_code == 200:
            return base64.b64decode(resp.json()["data"][0]["b64_json"])
        retryable = resp.status_code == 429 or resp.status_code >= 500
        if retryable and attempt < RETRIES:
            time.sleep(2 ** attempt)
            continue
        try:
            detail = resp.json().get("error", {}).get("message", resp.text[:300])
        except ValueError:
            detail = resp.text[:300]
        detail = re.sub(r"sk-[\w*-]+", "sk-***", detail)  # API errors can echo part of the key
        die(f"{item['id']}: HTTP {resp.status_code}: {detail}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("prompts")
    ap.add_argument("--out", required=True)
    ap.add_argument("--refs")
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--quality", choices=sorted(QUALITIES))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    items = load_items(args.prompts)
    if args.only:
        missing = set(args.only) - {it["id"] for it in items}
        if missing:
            die(f"unknown ids: {', '.join(sorted(missing))}")
        items = [it for it in items if it["id"] in args.only]
    refs = load_refs(args.refs)

    if args.dry_run:
        print(f"dry run: {len(items)} image(s), model {args.model}, {len(refs)} reference image(s)")
        for it in items:
            q = args.quality or it.get("quality", "high")
            print(f"  {it['id']}: {it['size']}, {it['background']}, quality {q}, {len(it['prompt'])} chars")
        print("no request sent")
        return

    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        die("OPENAI_API_KEY is not set. Add it in the environment settings, not in chat.")
    headers = {"Authorization": f"Bearer {key}"}
    os.makedirs(args.out, exist_ok=True)
    manifest_path = os.path.join(args.out, "manifest.json")
    manifest = []
    if os.path.exists(manifest_path):
        with open(manifest_path, encoding="utf-8") as f:
            manifest = json.load(f)

    session = requests.Session()
    for it in items:
        quality = args.quality or it.get("quality", "high")
        png = call(session, headers, it, args.model, quality, refs)
        path = os.path.join(args.out, f"{it['id']}.png")
        with open(path, "wb") as f:
            f.write(png)
        manifest = [m for m in manifest if m["id"] != it["id"]]
        manifest.append({
            "id": it["id"],
            "file": os.path.basename(path),
            "prompt": it["prompt"],
            "model": args.model,
            "size": it["size"],
            "background": it["background"],
            "quality": quality,
            "references": [os.path.basename(p) for p in refs],
            "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
            "ai_generated": True,
        })
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2)
        print(f"wrote {path} ({len(png) // 1000} KB)")


if __name__ == "__main__":
    main()

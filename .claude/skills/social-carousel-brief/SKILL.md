---
name: social-carousel-brief
description: Turn a blog post, site page or case study into a social carousel brief for Point of Rental or Record360 with sourced slide copy, illustration prompts (and the images, when an OpenAI key is set), a Claude Design layout spec, and captions per channel. Use when asked to make a carousel or social post from a URL, write slide copy or captions from a blog, build image prompts for a carousel, or "start a social post" for either brand. Reads the performance playbook first, checks every claim against the source, and never posts or schedules anything.
---

# Social carousel brief

Source material in, a reviewable brief out. The brief is the single document that feeds Claude Design (layout), the image generator, Asana (review) and the UTM sheet.

**Needs:** WebFetch (to read the source page). Optional: `OPENAI_API_KEY` in the environment to generate images, Python with `requests`. Layout is done by the user in Claude Design from the spec this skill writes.

**Inputs:** brand (Point of Rental or Record360), one or more source URLs, optionally an angle, campaign and the target channels. If the brand or source is missing, ask. If the post is about people, an event or a milestone, say it needs real photos and stop: illustration is for stories about the software.

## Step 1: Read the rules
Read, in this order: `CLAUDE.md`, `references/playbook.md`, the brand voice file (`voice-por.md` or `voice-r360.md`), `references/channels.md`, `references/slop-checklist.md`, and the brand illustration file.

## Step 2: Read the source and build the claims table
- Fetch each URL with WebFetch. WebFetch summarizes with a small model, so ask for **verbatim quotes** and treat anything paraphrased as unverified. Re-fetch the specific section to confirm any number or named feature before it goes in a slide.
- Build a claims table: `id | exact quote | source URL | status`. Status is `verified` (quote confirmed on the page) or `unverified`. Unverified claims are not used in slides. List them in the flags.
- Product claims (features, AI behavior, numbers, results) are marked for product review: Andy Lynch for Point of Rental, Bryan Osuszek for Record360.
- Customer quotes: record the speaker and company exactly as the page shows them, and note that permission to reuse a quote on social is not confirmed unless the page or case study says so.

## Step 3: Pick the angle and shape
- Default: LinkedIn-first document carousel, 5 to 7 slides, repurposed as images for the other channels (see `channels.md`).
- Slide 1 is the hook: the problem or the result, from a verified claim or a real situation in the source. Not a product description.
- One idea per slide. Each slide cites a claim id. A closing slide says what to do and where the link is, in text.
- Pick one angle. If the source supports two, propose both and let the user choose.
- Tag the post with a test id from the playbook if it belongs to one.

## Step 4: Write slide copy
For each slide: headline (max 8 words), support line (max 20 words), claim id. Write in the brand voice, then run the slop checklist and fix failures.

## Step 5: Illustration prompts
- One illustration per slide that needs one, many slides can be type only.
- Elements are concrete drawable things from the source, 2 to 3 per image, as in `email-image-prompts` step 4.
- Every prompt starts with the brand style paragraph, then the elements, composition and background. No words, numbers, logos or readable UI text in the art.
- Write prompts to `images.json` (format below) so the generator and the user both use the same text.
- Photoreal AI imagery is not used for damage, product proof, people or events. If the story needs proof, say a real screenshot or capture is needed and where it goes in the layout.

`images.json`:
```
[
  {"id": "01-cover", "prompt": "...", "size": "1024x1536", "background": "transparent", "quality": "high"}
]
```
Valid sizes: 1024x1024, 1024x1536, 1536x1024. `background`: transparent or opaque.

## Step 6: Layout spec for Claude Design
Write it so it can be pasted: canvas 1080 x 1350 px, the brand design system, slide-by-slide layout (what sits where), type sizes from the slop checklist (headline at least 64 px, body at least 30 px, nothing under 24 px, margins at least 72 px), page indicator, swipe cue, closing slide with text instead of a button, and the export set: PNG slides plus one PDF for LinkedIn, X gets cover plus three. Leave empty space where generated art needs to sit.

## Step 7: Captions
Write one per channel in `channels.md` that applies. First line adds new information. No repeated emoji or opener. Put the tracked link only where the channel allows it, and say "link in bio" on Instagram. Use the proposed UTM values from `social-post-package` (source per channel, medium `organic_social`, campaign slug, content `carousel_<angle>`).

## Step 8: Save the brief
Write `briefs/<yyyy-mm-dd>-<brand>-<slug>/brief.md` from `references/brief-template.md`, plus `images.json`. Show the user a short summary: angle, slide headlines, flags. Do not paste the whole brief into chat.

## Step 9: Generate images (optional)
If the user wants images generated and `OPENAI_API_KEY` is set:
```
python3 -I .claude/skills/social-carousel-brief/scripts/generate_images.py briefs/<folder>/images.json --out briefs/<folder>/art --refs assets/style-refs/<brand-style> --dry-run
```
Show the dry-run, ask before the real run (it costs money per image), then rerun without `--dry-run`. It writes PNGs and `manifest.json` (prompt, model, size, date, AI-generated flag). Review each image against the slop checklist. If the key is not set, tell the user to add `OPENAI_API_KEY` in the environment settings (never in chat) and give them the prompts to paste into ChatGPT in the meantime.

## Flags to end with
Unverified claims dropped, product claims needing review, quotes needing permission, any slide that needs a real screenshot or photo, AI imagery used, missing reference images.

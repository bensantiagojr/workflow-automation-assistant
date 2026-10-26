---
name: email-image-prompts
description: Build the two ChatGPT image prompts for an upcoming email graphic task in Asana, a pointillism header icon (1:1, transparent PNG) and an email banner (3:1, off-white background), then resize the generated images for the email (icon 800x800, banner 1200 px wide, both under 200 KB). Use when asked for email graphic prompts, header icon or banner prompts, to "do the email image prompts" for an Asana email task, or to resize the email icon and banner PNGs. Pulls the email copy from the task's Google Doc or description, picks a couple of visual elements from the email, returns both prompts ready to paste into the two ChatGPT threads, and asks for the finished images to resize.
---

# Email image prompts

Turns an Asana email task into two copy-paste prompts for ChatGPT image generation.

| Output | ChatGPT thread | Use in email | Aspect ratio | Background |
|---|---|---|---|---|
| **Prompt 1: header icon** | Pointillism thread | Email header | 1:1 | transparent PNG |
| **Prompt 2: banner** | Clay thread (sometimes pointillism mixed in) | Inside the email body | 3:1 | off-white |

This skill cannot send anything to ChatGPT. It only produces the text to paste, and later resizes the images the user brings back.

**Needs:** the Asana connector (to read the task) and the Google Drive connector (to read the email copy doc). Resizing needs Python with Pillow.

**Flow:** find the email task, get the copy, produce the two prompts, ask for the generated images, then resize them.

## Rules that apply to every image
- **Never any logos.** No product, brand, sponsor or partner marks. Sponsor logo lines in the email source are ignored.
- **Clean and simple.** Not busy, not distracting. Few elements, plenty of space.
- **Keep the style.** The ChatGPT thread already holds the style. The image should emphasize that look.
- **No words or numbers** in the image.

## Step 1: Find the task
- If the user gives a task link or name, use it. It may be the **graphic subtask** ("Create email graphic design" or "Email Graphic") or the **email task itself**. If the task has a parent, the parent is the email request. If it has no parent, it is the email request.
- Otherwise call `get_my_tasks` (incomplete only) and keep tasks named like "Create email graphic design" or "Email Graphic". List them with their due dates and the parent email's name, and ask which one to do. Default to the earliest due date.
- Call `get_task` on the email request for its `notes`, comments, and due date. Email requests live in the "Email Calendar" project and come from the Email Requests form.

## Step 2: Get the email copy
Look in the email request's notes, in this order.

**A. Google Doc link** (usually under "Provide a description of request"). Read it with the Google Drive `read_file_content` tool.
- Many docs hold several emails, one per numbered `## ` heading (for example `## 10. Sessions Open for Registration — Registered Attendees Only`).
- Match the section to the email's title in the request ("Email Title / Name"). Ignore trailing request-form text such as ", Sarah Crowther". If the task quotes a number ("copy 11. ..."), that is the best match.
- Take only that section: from its `## ` heading up to the next `## ` heading.
- From the section keep: **Subject**, **Main Headline**, **Mini-paragraph**, **Copy**, and the CTA wording.
- Drop: the metadata table (Template, From, Reply-to, Audience, To, Suppress, Preview text), "Email From", sponsor and logo lines, and send date.
- **Suggested edits gotcha.** The plain-text read shows an original sentence and its suggested replacement run together with no space ("...the move.Book your ticket today..."). To get the single current version, call `download_file_content` with `exportMimeType: "text/html"`. The result is very large and is saved to a file, so parse it with `python3 -I` (decode base64 if needed, then find the section by heading). Use the HTML version of any sentence that appears twice, and mention it in the flags.

**B. Inline copy** in the task notes ("Subject line:" and "Body copy:" lines). Use those as written.

**C. Neither found.** Ask the user to paste the copy. Never invent email copy.

## Step 3: Clean the copy
- Remove raw URLs, bracketed placeholders for links, and hotel or address lists, since they add nothing to an image. Keep the sentence that mentions them.
- Remove "[Suggested]" tags but keep the wording.
- Keep numbered steps and bullet points, trimmed to plain text. Keep merge fields like `[Customer First Name]`.
- **Flag the copy status in the output.** If the section still has `[ Write body copy here ]`, a "Copy direction:" note, or an unresolved `[insert ...]` placeholder, it is a draft. Say so, and build the prompt from the headline, mini-paragraph and copy direction instead.

## Step 4: Pick the elements to show
The "All I want is pretty much a graphic showing ..." line is where you **pull a couple of elements out of the email** that (1) hint at what the email is about and (2) look good as a picture. Choose them yourself, and ask the user only if the email is hard to picture (for example a pure thank-you).

How to choose:
- **2 elements for the header icon** (1 is fine). **2 to 3 for the banner.** Fewer is better.
- Each element is a **concrete, drawable thing or action** taken from the email: a phone with an agenda, a calendar, a checkmark, a ticket, a person at a laptop, a piece of equipment. Not an abstract idea ("modernisation") and not a list of features.
- Together they should **hint at the main message** of the email, not summarize all of it.
- Make the icon one simple idea. Give the banner a scene with a different composition from the icon.
- Prefer elements that read cleanly in a soft, simple style.
- Never choose a logo, brand or sponsor mark, a screenshot with readable text, a number or date, a chart that needs labels, or a crowded scene.

Write them as a plain noun phrase that fits after "showing", for example "a phone with a personal agenda being built and a one-to-one expert slot being picked".

## Step 5: Output
Show, in this order:
1. The task and email name, its send date, and where the copy came from (doc section or task notes).
2. **Prompt 1 (Pointillism thread: header icon)** in a code block.
3. **Prompt 2 (Banner thread)** in a code block.
4. A short "Elements chosen" line for each image, saying what was picked and the email idea it hints at.
5. A short "Flags" list: draft or placeholder copy, anything trimmed, and any sentence that had a suggested edit.
6. **Always end with this ask** (adjust the wording, keep the substance): "When you have generated the icon PNG and the banner, send them back here and I'll resize them (icon 800x800, banner 1200 px wide, both under 200 KB)." Then stop and wait. Do not resize anything until the images are provided.

Do not add commentary inside the code blocks. The blocks are pasted as is.

## Step 6: Resize the finished images (once the user sends them back)
This step starts when the user provides the generated images, in the same chat or a later one. They may send both together or one at a time. Do it right away, without asking more questions.

1. **Identify each file.** A square image is the header icon. A wide image (about 3:1) is the banner. If several emails are in play, pair files with the right email by content (for example a phone with session cards belongs with a sign-up email) and say how you paired them. Ask only if a pairing is genuinely unclear.
2. **Find the files.** Use the paths the conversation gives for the uploaded images (png, webp or jpg all work).
3. **Resize with the bundled script** (below), once per file.
4. **Check the icon** by compositing it on a dark background and viewing it, to confirm the transparency survived and the palette reduction left it clean.
5. **Return the files** and report, per file: pixel size, KB, and the method the script used. Say if only one of the two images has been received and that the other is still needed.

Specs:

| Image | Size | File size | Format |
|---|---|---|---|
| Header icon | **800 x 800 px** | **under 200 KB** | PNG, transparency kept |
| Banner | **max width 1200 px**, aspect ratio kept (a 3:1 banner becomes 1200 x 400) | **under 200 KB** | PNG, or JPEG only if PNG cannot fit |

Run the bundled script rather than resizing by hand. The path is relative to this skill's folder, wherever it is installed:

```
python3 -I <skill folder>/scripts/resize_email_images.py icon   <input> <output.png>
python3 -I <skill folder>/scripts/resize_email_images.py banner <input> <output.png>
```

It needs the Pillow library. If `import PIL` fails, install it with `pip install pillow` and run again.

It resizes with LANCZOS, tries a plain PNG, then reduces the palette (256, 192, 128, ... colours) until the file is under 200 KB, and only falls back to JPEG for a banner. It prints the final size, KB and method. Report those back, and view the icon on a dark background to confirm the transparency survived. Name outputs `<email-slug>-icon-800.png` and `<email-slug>-banner-1200.png`.

## Prompt templates
Fill the `{...}` fields. Everything else is verbatim, and the wording is deliberate. "I love this style a lot can you make one again" relies on the style already established in that ChatGPT thread.

### Prompt 1: header icon (pointillism)
```
I love this style a lot can you make one again different focus. All I want is pretty much a graphic showing {ELEMENTS}, maybe floating UI elements and nice movement in the graphic. Keep it clean and simple, not too busy or distracting, and keep the style so the look really comes through. 1:1 is the aspect ratio, png transparent background. No words or numbers needed. No logos.

Subject line: {SUBJECT}

Body copy: {BODY}
```

### Prompt 2: banner (clay, sometimes pointillism mixed in)
```
I love this style a lot can you make one again different focus. All I want is pretty much a graphic showing {ELEMENTS}, maybe floating UI elements and nice movement in the graphic. Professional, clean vibes. Keep it simple, not too busy or distracting, and keep the style so the look really comes through. 3:1 is the aspect ratio, off white background. No words or numbers needed. No logos. No need to show all the features, pick a couple to represent easily:

Subject: {SUBJECT}

{BODY}
```

For the banner, use the full cleaned email body. For the icon, the same body is fine, or a shortened version if the email is very long.

See `examples.md` for the two original prompts this was built from.

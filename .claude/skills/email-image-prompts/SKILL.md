---
name: email-image-prompts
description: Build the two ChatGPT image prompts for an upcoming email graphic task in Asana, a pointillism header icon (1:1, transparent PNG) and an email banner (3:1, off-white background). Use when asked for email graphic prompts, header icon or banner prompts, or to "do the email image prompts" for an Asana email task. Pulls the email copy from the task's Google Doc or description and returns both prompts ready to paste into the two ChatGPT threads.
---

# Email image prompts

Turns an Asana email task into two copy-paste prompts for ChatGPT image generation.

| Output | ChatGPT thread | Use in email | Aspect ratio | Background |
|---|---|---|---|---|
| **Prompt 1: header icon** | Pointillism thread | Email header | 1:1 | transparent PNG |
| **Prompt 2: banner** | Clay thread (sometimes pointillism mixed in) | Inside the email body | 3:1 | off-white |

This skill cannot send anything to ChatGPT. It only produces the text to paste.

## Step 1: Find the task
- If the user gives a task link or name, use it.
- Otherwise call `get_my_tasks` (incomplete only) and keep tasks named like "Create email graphic design" or "Email Graphic". List them with their due dates and the parent email's name, and ask which one to do. Default to the earliest due date.
- Call `get_task` on the graphic task with `parent.name`. The **parent** is the email request (in the "Email Calendar" project). The graphic task itself has no copy.
- Call `get_task` on the parent for its `notes`, comments, and due date.

## Step 2: Get the email copy
Look in the parent task's notes, in this order.

**A. Google Doc link** (usually under "Provide a description of request"). Read it with the Google Drive `read_file_content` tool.
- Many docs hold several emails, one per numbered `## ` heading (for example `## 10. Sessions Open for Registration — Registered Attendees Only`).
- Match the section to the email's title in the request ("Email Title / Name"). Ignore trailing request-form text such as ", Sarah Crowther". The number in the doc may be quoted in the task ("copy 11. ..."), and that is the best match.
- Take only that section: from its `## ` heading up to the next `## ` heading.
- From the section keep: **Subject**, **Main Headline**, **Mini-paragraph**, **Copy**, and the CTA wording.
- Drop: the metadata table (Template, From, Reply-to, Audience, To, Suppress, Preview text), "Email From", sponsor and logo lines, and send date.

**B. Inline copy** in the task notes ("Subject line:" and "Body copy:" lines). Use those as written.

**C. Neither found.** Ask the user to paste the copy. Never invent email copy.

## Step 3: Clean the copy
- Remove raw URLs, bracketed placeholders for links, and hotel or address lists, since they add nothing to an image. Keep the sentence that mentions them.
- Remove "[Suggested]" tags but keep the wording.
- Keep numbered steps and bullet points, trimmed to plain text. Keep merge fields like `[Customer First Name]`.
- **Flag the copy status in the output.** If the section still has `[ Write body copy here ]`, a "Copy direction:" note, or an unresolved `[insert ...]` placeholder, it is a draft. Say so, and build the prompt from the headline, mini-paragraph and copy direction instead.

## Step 4: Pick a focus for each image
Each prompt has a "graphic showing ..." line, and that is the only part that changes between emails. Propose one for each image and let the user change it.
- **Header icon:** one simple, single idea a person can read at a glance (for example "someone booking their seats for a session"). Make it different from the last icon where you can.
- **Banner:** a scene that stands for the whole email's message, naming only a couple of features or points. The templates say "pick a couple to represent easily", so do not list everything.
- Ask the user once if the email is hard to picture (for example a pure thank-you email).

## Step 5: Output
Show, in this order:
1. The task and email name, its send date, and where the copy came from (doc section or task notes).
2. **Prompt 1 (Pointillism thread: header icon)** in a code block.
3. **Prompt 2 (Banner thread)** in a code block.
4. A short "Flags" list: draft or placeholder copy, anything trimmed, and any assumption made about the focus.

Do not add commentary inside the code blocks. The blocks are pasted as is.

## Prompt templates
Fill the `{...}` fields. Everything else is verbatim, and the wording is deliberate. "I love this style a lot can you make one again" relies on the style already established in that ChatGPT thread.

### Prompt 1: header icon (pointillism)
```
I love this style a lot can you make one again different focus. All I want is pretty much a graphic showing {ICON_FOCUS}, maybe floating UI elements and nice movement in the graphic. 1:1 is the aspect ratio, png transparent background. No words or numbers needed

Subject line: {SUBJECT}

Body copy: {BODY}
```

### Prompt 2: banner (clay, sometimes pointillism mixed in)
```
I love this style a lot can you make one again different focus. All I want is pretty much a graphic showing {BANNER_FOCUS}, maybe floating UI elements and nice movement in the graphic. Professional, clean vibes. 3:1 is the aspect ratio, off white background. No words or numbers needed. No need to show all the features, pick a couple to represent easily:

Subject: {SUBJECT}

{BODY}
```

For the banner, use the full cleaned email body. For the icon, the same body is fine, or a shortened version if the email is very long.

See `examples.md` for the two original prompts this was built from.

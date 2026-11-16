---
name: social-post-package
description: Turn an approved social carousel brief into the tracked package, UTM rows in the Social Media UTM Tracker sheet (one row per channel) and a draft Asana review task in the Social Media Calendar project with reviewers named in the description. Use when asked to package a post, create the UTM links and the Asana task for a social post, or log a post in the UTM sheet. Never posts or schedules anything, and asks before writing to the sheet or Asana.
---

# Social post package

Takes a brief from `social-carousel-brief` (or an equivalent description) and produces: UTM rows for the sheet, the tracked links, and a draft Asana task ready for review.

**Needs:** Google Sheets connector (sheet id in `CLAUDE.md`), Asana connector (load `create_tasks` and `search_objects` with ToolSearch). Read `references/asana.md` for ids and the description template.

## Step 1: Gather
From the brief: brand, campaign slug, format, angle, landing URL, channels, captions, asset links, claims and flags, test id. Missing landing URL or channel list: ask. Channels follow `social-carousel-brief/references/channels.md`.

## Step 2: Build the UTM rows
One row per channel, tab by brand (`Point of Rental` gid 0, `Record360` gid 1).
- Columns to write: A Post ID (Asana task id, fill after the task exists), B Date (planned), C Campaign / Initiative, D Format (`carousel`, `image`, `reel`, `video`, `link`, `story`, `text`), E Content ID (the angle, e.g. `fleet-secrets`), F Channel (dropdown values from the `Lists` tab), G Landing page URL, N CTA, O Status, P Asana task, R Notes.
- Never write columns H to M. They are array formulas in row 2 that fill down on their own (source, medium, campaign, content, Final URL, check).
- The landing URL keeps its original path and case.
- Row 2 starts as an example row (Post ID `EXAMPLE`). If A2 is `EXAMPLE`, overwrite its input cells for the first real row and set the note, but never delete the row, it holds the formulas.
- Find the next empty row by reading column G of the tab. Read first, write second, then read back and confirm column M says `OK` for every new row.
- For a test, put the variant in Content ID (for example `robot-fleet-secrets`) and the test id in Notes.

Show the planned rows and ask before writing.

## Step 3: Draft the Asana task
Ask before creating. Project and field ids are in `references/asana.md`. Create one task per post (not per channel) in the section `In Development`, with:
- Name: `{Brand} | {working title} | {format}`.
- Custom fields: Brand, Campaign / Initiative, Post Format, Primary Objective, Social Channel (Threads and YouTube have no option yet, name them in the description), Run Dates.
- Description from the template in `references/asana.md`. Reviewers are named in the description with what each reviews. Do not create subtasks and do not assign reviewers.
- Link the sheet row with `.../edit#gid=<tab gid>&range=A<row>`.

Then write the Asana task id back to column A and the task link to column P of each row.

## Step 4: Hand back
Summarize in chat: task link, rows written (tab and row numbers), the Final URL per channel in a short list, the reviewers named, open flags. Remind the user that scheduling in Metricool is a manual step for now: captions and links are in the task, assets go in as attachments.

## Never
Post, schedule, send Slack messages or change existing tasks without being asked. Delete or overwrite sheet rows other than the example row.

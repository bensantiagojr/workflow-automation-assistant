# Social media system: Point of Rental and Record360

Goal: turn real source material (blogs, site pages, case studies) into posts that can perform, with tracked links, and get better each week from the results.

## Where things live
- UTM tracker (Google Sheet): https://docs.google.com/spreadsheets/d/1PTOy9FugrZuvV58SasqIIHqjSJLEhBUBDdFZLQsv9gg/edit
  Tabs: `Point of Rental` (gid 0), `Record360` (gid 1), `Lists`, `Rules`. Convention and reviewer routing are on the `Rules` tab.
- Asana project: Social Media Calendar (digital), gid 1202855667985941. Field and section ids are in `.claude/skills/social-post-package/references/asana.md`.
- Scheduling: Metricool (manual for now, no connector).
- Brand: `Point of Rental Rebrand 2026` is the current Canva brand kit for Point of Rental. Record360 has its own kit.

## Skills
- `social-carousel-brief`: source URL(s) to a brief with slide copy, illustration prompts, a Claude Design layout spec and captions. Can generate the images with the OpenAI API.
- `social-post-package`: approved brief to UTM rows in the sheet plus an Asana review task.
- `email-image-prompts`: email graphics (separate workflow).

## Rules
- Draft only. Never post, schedule, send or publish. Ask before creating or changing Asana tasks, sending Slack messages or editing the UTM sheet.
- Never invent a statistic, quote or product claim. Every claim in a post traces to a source URL and an exact quote in the brief.
- Illustration for concepts, real images for proof. AI art is fine for stories about what the software can do. Never use photoreal AI imagery for product proof, damage, people or events. Record every generated image in the manifest. If a photoreal AI image is ever used, say so in the caption.
- Reviewers go in the Asana task description, not subtasks. Design: Andrew Sherrington (every post). Copy: Michael Peck (every post). Product posts: Andy Lynch for Point of Rental, Bryan Osuszek for Record360.
- Measure success by non-employee engagement, UTM sessions and demo requests. Reactions alone do not count, because most LinkedIn followers are employees.
- UTM values: `utm_source` is the platform, `utm_medium` is `organic_social`, `utm_campaign` is the initiative slug with year, `utm_content` is `format_angle`. Never touch the path of the landing URL.
- Secrets: the OpenAI key is read from the `OPENAI_API_KEY` environment variable. Never print, log, commit or ask for it in chat.
- Performance findings and open tests live in `.claude/skills/social-carousel-brief/references/playbook.md`. Read it before ideating and update it after each weekly report.

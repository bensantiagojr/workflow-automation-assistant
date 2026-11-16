# Numbers that look complete can still mislead

- Brand: Point of Rental
- Campaign / initiative: rental-intelligence-2026
- Angle: Data without context misleads. Rental Intelligence Suite adds the context, and a closed beta customer says what that saved.
- Test id: T2 (LinkedIn link in first comment; the next post uses the body link)
- Primary objective: Lead Capture / Demo Request
- Landing page: https://www.point-of-rental.com/rental-intelligence/
- Date drafted: 2026-11-16
- Mode: prompts only (no OPENAI_API_KEY). Images are made by pasting the prompts below into the pointillism ChatGPT thread.

Alternate angle for a later post: lead with the customer result ("like six hours" to "about 15 minutes") and put the problem second. It needs the quote permission below cleared first.

## Sources and claims
Source article: https://www.point-of-rental.com/rental-intelligence-suite-data-truth/ (A). Product page: https://www.point-of-rental.com/rental-intelligence/ (P). Both were read through a fetch tool that returns short excerpts, so confirm each quote on the live page before the post goes out.

| id | Exact quote | Source | Status |
|---|---|---|---|
| c1 | "Without context, data doesn’t just fall short—it actively misleads." | A | verified |
| c2 | "It can make a profitable asset look weak." | A | verified |
| c3 | "It can hide repair costs, outdated reports, and missed opportunities behind numbers that look complete." | A | verified |
| c4 | "…into clearer decisions around ROI, utilization, fleet health, disposition, and future planning." | A | verified |
| c5 | Michael Isakson, Total Rentals: "like six hours… With this, it was about 15 minutes to see everything I was looking for." (the page has bracketed words before "like six hours", exact text not captured) | A | verified in part, confirm full quote |
| c6 | "But rather than explain it ourselves, we’d rather let the people using Rental Intelligence Suite in closed beta do the talking." | A | verified |
| c7 | "Dashboard lets you ask a plain-language question and get back a customizable, explainable answer" and Type "show my highest ROI items" or "what’s my maintenance spend this month" | P | verified |
| c8 | "AI Insights reviews your fleet every night and flags underused equipment, rising maintenance costs" (excerpt ends there) | P | verified |
| c9 | "Powered by AI and built on your existing Point of Rental data" | P | verified |
| c10 | "Available now on Point of Rental Elite, with more of the platform coming soon." and "available today for Point of Rental Elite customers" | P | verified |
| c11 | CTA text "See it in action" | P | verified |
| x1 | "Monthly" reporting time (appeared only in a summary, not in the quote) | A | unverified, not used |
| x2 | Descriptions of Fleet Advisor, Voice Agent, Disposition Agent | P | not on page, not used |
| x3 | Seasonal demand shifts, keep/fix/sell lifecycle flags (appear in the earlier robot samples) | P | not confirmed in the excerpt, not used |

Product review needed: yes, by Andy Lynch (nightly AI Insights, plain-language questions, Elite-only availability, and the customer result).

## Slides
| # | Headline | Support line | Claim | Art |
|---|---|---|---|---|
| 1 | Numbers that look complete can still mislead. | Without context, data actively misleads. | c1, c3 | 01-cover |
| 2 | A profitable asset can look weak. | Without context, a number can point you the wrong way. | c2, c1 | 02-weak-asset |
| 3 | Repair costs hide behind clean totals. | Outdated reports and missed opportunities hide there too. | c3 | 03-hidden-costs |
| 4 | Same data. Clearer decisions. | Built on your existing Point of Rental data, for ROI, utilization, fleet health, disposition and planning. | c4, c9 | 04-same-data |
| 5 | How it works | Ask in plain language: "show my highest ROI items". Nightly AI Insights: your fleet is reviewed every night. | c7, c8 | 05-how-it-works |
| 6 | “…about 15 minutes to see everything I was looking for.” | Michael Isakson, Total Rentals. Before: “like six hours.” Closed beta user. | c5, c6 | none, or a real screenshot |
| 7 | See it in action. | Available now for Point of Rental Elite customers. point-of-rental.com/rental-intelligence | c10, c11 | 07-cta |

Slide 6 headline is 10 words because it is a verbatim customer quote, which is exempt from the 8 word limit.

Slide 5 is better with a real Rental Intelligence Suite screenshot (Dashboard or AI Insights) in place of the illustration, if one is cleared for use.

## Illustration prompts (paste into the pointillism ChatGPT thread)
One prompt per image, one image each. Files are `images.json` for the API later.

Template used for every prompt:
```
I love this style a lot can you make one again different focus. All I want is pretty much a graphic showing {ELEMENTS}, maybe floating UI elements and nice movement in the graphic. Keep it clean and simple, not too busy or distracting, and keep the style so the look really comes through. 1:1 is the aspect ratio, png transparent background. No words or numbers needed. No logos.
```

| Image | {ELEMENTS} |
|---|---|
| 01-cover | a bar chart that looks complete and tidy, with a few loose dots drifting away from one of the bars |
| 02-weak-asset | a compact tracked loader next to a small line chart sloping downward, with a soft glow around the loader |
| 03-hidden-costs | a wrench partly hidden behind a tall stacked bar that looks neat and complete |
| 04-same-data | scattered dots on one side flowing into an orderly arrow and a few clean checklist cards on the other |
| 05-how-it-works | a speech bubble and a crescent moon with a few stars, floating over a small loader |
| 07-cta | a laptop showing a dashboard made of simple dot shapes |

Generate all six, then send them back. I will name them, record them in `art/manifest.json` as AI-generated (tool: ChatGPT, thread: pointillism) and check them against the slop checklist. Illustration only: no real equipment photos, people or invented app screens.

### Review round 1 (2026-11-16)
Received 01 to 05 and 07 (05 was only seen as an inline image, so its transparency is unchecked). All have true transparent backgrounds, so no white boxes on the off-white layout, and none has text, numbers or logos. Fixes needed:
- **Two styles in one carousel.** 03, 04, 05 and 07 are bold: dense dots, soft 3D volume. 01 and 02 are light and airy, and 01 is faint (about 12% coverage, semi-transparent), so the hook slide would wash out on a phone. Re-roll 01 and 02 in the bold style.
- **03 does not show the idea.** The wrench is fully visible and the bars rise, so it reads as growth, not as repair costs hiding. Re-roll with the wrench mostly hidden.
- **Aspect ratios.** 03, 04, 05 and 07 came back 16:9 or 2:1, not 1:1, so the layout spec now places art as a strip and the re-rolls ask for 16:9.

Re-roll prompts (paste into the pointillism thread and attach the laptop image, 07, as the style anchor):
```
Same style as the laptop image: dense dots, soft rounded 3D volume, bold brand greens. All I want is pretty much a graphic showing a bar chart that looks complete and tidy, with a few loose dots drifting away from one of the bars, maybe floating UI elements and nice movement in the graphic. Keep it clean and simple, not too busy or distracting. 16:9 is the aspect ratio, png transparent background. No words or numbers needed. No logos.
```
(01-cover)
```
Same style as the laptop image: dense dots, soft rounded 3D volume, bold brand greens. All I want is pretty much a graphic showing a compact tracked loader next to a small line chart sloping downward, with a soft glow around the loader, maybe floating UI elements and nice movement in the graphic. Keep it clean and simple, not too busy or distracting. 16:9 is the aspect ratio, png transparent background. No words or numbers needed. No logos.
```
(02-weak-asset)
```
Same style as the laptop image: dense dots, soft rounded 3D volume, bold brand greens. All I want is pretty much a graphic showing a wrench almost completely hidden behind a tall, neat stacked bar, with only the wrench head peeking out above it, maybe floating UI elements and nice movement in the graphic. Keep it clean and simple, not too busy or distracting. 16:9 is the aspect ratio, png transparent background. No words or numbers needed. No logos.
```
(03-hidden-costs)

After the re-rolls I will convert the six to PNG, name them `rental-intelligence-data-misleads-art-<id>.png` and record them in `art/manifest.json`.

## Layout spec (Claude Design)
```
Canvas: 1080 x 1350 px (4:5), 7 slides. The generated art is 16:9 or 2:1 with a transparent background: place it as a strip at the full content width (936 px), keep the area above it clear for type, and never stretch or crop the dots. Use the Point of Rental Rebrand 2026 design system. Light off-white background, dark text, brand green as the highlight. The generated pointillism art has a transparent background and sits on the light background.

Every slide: "Rental Intelligence Suite" lockup top left, 7-segment page indicator top right (current slide filled). Margins 72 px. Type: headline at least 64 px bold, support text at least 30 px, nothing under 24 px. "SWIPE →" cue bottom right on slides 1 to 6, none on slide 7. Highlight the key phrase of each headline with the brand green underline.

1 Cover: headline top (max 3 lines), support line under it, art 01-cover as a strip in the lower 40%.
2 Headline top, support line, art 02-weak-asset as a strip in the lower 40%.
3 Headline top, support line, art 03-hidden-costs as a strip in the lower 40%.
4 Headline top, support line, art 04-same-data as a strip in the lower 40%.
5 How it works: headline "How it works", two stacked cards. Card 1: "Ask in plain language" with the line  "show my highest ROI items". Card 2: "Nightly AI Insights" with "Your fleet is reviewed every night." Art 05-how-it-works as a strip at the bottom, or a real product screenshot if cleared.
6 Quote: the quote is the headline, large, left aligned with a green quotation mark. Support line below it. No art. Optionally a small dot motif in a corner.
7 Closing: headline "See it in action." Support line, then the URL point-of-rental.com/rental-intelligence as plain text (no button graphic). Art 07-cta as a strip in the lower 40%.

Export: PNG per slide named rental-intelligence-data-misleads-01.png to -07.png, plus one PDF with all 7 slides in order for LinkedIn. X gets slides 1, 2, 5 and 6 only.
```

## Captions
Link placement: LinkedIn in the first comment (test T2). Facebook, X and Threads in the post. Instagram uses the tagged link on the bio or Linktree.

### LinkedIn
```
Which of your assets looks weak on paper but is actually profitable?

Without context, a number can mislead. It can hide repair costs, outdated reports and missed opportunities behind numbers that look complete.

Rental Intelligence Suite is built on your existing Point of Rental data. You can ask a plain-language question, like "show my highest ROI items," and AI Insights reviews your fleet every night.

One closed beta user, Michael Isakson of Total Rentals: "…like six hours… With this, it was about 15 minutes to see everything I was looking for."

Available now for Point of Rental Elite customers. Link in the first comment.

#RentalIndustry #FleetManagement
```
First comment: `See it in action: {LinkedIn link}`

### Facebook
```
Which of your assets looks weak on paper but is actually profitable? Without context, a number can hide repair costs and missed opportunities. Rental Intelligence Suite is built on your existing Point of Rental data and is available now for Point of Rental Elite customers. {Facebook link}
```

### Instagram
```
Which of your assets looks weak on paper but is actually profitable? Swipe to see how context changes the numbers, and what Rental Intelligence Suite does with your Point of Rental data. Available now for Point of Rental Elite customers. Link in bio.

#RentalIndustry #FleetManagement
```

### X (slides 1, 2, 5, 6)
```
Which of your assets looks weak on paper but is actually profitable? Context changes the numbers. Rental Intelligence Suite, built on your Point of Rental data, is available now for Elite customers. {X link}
```

### Threads (optional, cross-post only)
```
Which of your assets looks weak on paper but is actually profitable? Rental Intelligence Suite adds the context behind the numbers. Available now for Point of Rental Elite customers. {Threads link}
```

## UTM plan
Landing page: https://www.point-of-rental.com/rental-intelligence/ (path unchanged). Medium is `organic_social`, campaign `rental-intelligence-2026`, content `carousel_data-misleads`.

| Channel | utm_source | Final URL |
|---|---|---|
| LinkedIn | linkedin | https://www.point-of-rental.com/rental-intelligence/?utm_source=linkedin&utm_medium=organic_social&utm_campaign=rental-intelligence-2026&utm_content=carousel_data-misleads |
| Facebook | facebook | https://www.point-of-rental.com/rental-intelligence/?utm_source=facebook&utm_medium=organic_social&utm_campaign=rental-intelligence-2026&utm_content=carousel_data-misleads |
| Instagram | instagram | https://www.point-of-rental.com/rental-intelligence/?utm_source=instagram&utm_medium=organic_social&utm_campaign=rental-intelligence-2026&utm_content=carousel_data-misleads |
| X | x | https://www.point-of-rental.com/rental-intelligence/?utm_source=x&utm_medium=organic_social&utm_campaign=rental-intelligence-2026&utm_content=carousel_data-misleads |
| Threads | threads | https://www.point-of-rental.com/rental-intelligence/?utm_source=threads&utm_medium=organic_social&utm_campaign=rental-intelligence-2026&utm_content=carousel_data-misleads |

The URL typed on slide 7 carries no tags, so visits from it show up as direct.

## Review routing
- Design: Andrew Sherrington
- Copy: Michael Peck
- Product: Andy Lynch

## Flags
- Quote permission: Michael Isakson and Total Rentals appear in Point of Rental's own article, but permission to reuse the quote in social posts is not confirmed. Confirm with whoever collected the testimonials.
- Confirm the Isakson quote word for word on the live page, including the bracketed words before "like six hours". The fetch tool returned it in fragments. Slide 6 uses only a verbatim piece, "about 15 minutes to see everything I was looking for".
- Product claims for Andy Lynch: nightly AI Insights review, plain-language questions, and Elite-only availability. Nothing here implies other Point of Rental products have it.
- Dropped as unverified: "monthly" reporting, Fleet Advisor / Voice Agent / Disposition Agent descriptions, seasonal demand and keep/fix/sell flags.
- AI imagery: pointillism illustration only, to be recorded in the manifest when the images come back.
- Slide 5 would be stronger with a real product screenshot.
- LinkedIn followers are mostly employees: ask sales and customer success to share it with Elite customers (a suggested note goes in the Asana task).
- No reference images are stored in the repo yet, since the ChatGPT thread carries the style.

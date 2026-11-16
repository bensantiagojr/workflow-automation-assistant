# Performance playbook

Seed source: Metricool report for Point of Rental, 17 Nov 2025 to 15 Nov 2026. Format figures come from the top ~95 posts per network (the report lists only the top 100), so groups are small and the numbers are directional. Update this file after every weekly report.

## What the data says
- LinkedIn does the work: 32.9K of 36K followers, 85% of interactions, about 110 interactions per post (Facebook 14, Instagram 3, YouTube 1, Threads 0.07).
- Carousels beat single images:
  - LinkedIn document (PDF carousel): 27 posts, 137 avg clicks, 21.5% engagement. Single image: 41 posts, 40 clicks, 6.0%. Multi-image: 9 posts, 92 clicks, 13.2%. Video: 16 posts, 55 clicks, 7.3%.
  - Facebook multi-image: 16 clicks vs 9 for single image.
  - Instagram carousel: 134 views vs 94 for single image, 3.6 likes vs 1.6.
  - LinkedIn "clicks" include opening and swiping the document. This shows attention, not site visits. Confirm with UTM sessions.
- Top posts by interactions were people, team, event and milestone posts (Record360 teams post 1,373, APAC recognition 1,094, original-software find 834, Executive Hire Show Day One 779, IC26 recaps 420 to 560). Product and feature posts sat well below. The Rental Intelligence Suite launch post got 51 interactions on 381 impressions.
- Audience caution: only 1.8% of LinkedIn followers work in equipment rental, 36% are entry level, 39% are in engineering or IT. Much of the engagement is likely employees and partners.
- Threads: 116 posts produced about 1,000 impressions in total. YouTube: half of traffic is search, Shorts are 0.5%. Facebook and Instagram headline impression jumps do not reconcile with post-level numbers (about 143 reach per Facebook post, about 55 to 60 per Instagram post).
- Record360 LinkedIn sample (3 posts): the real event photo had 21 reactions, the settle-it image 10, the four-shots carousel 5.

## Defaults this implies
1. Build for LinkedIn first as a PDF document carousel, then repurpose the same slides as an image set for Instagram, Facebook and Threads. X gets the cover plus three slides (4 image limit).
2. Slide 1 carries the hook. The caption's first line must add something the slide does not say.
3. Use real photos for people and event posts. Use illustration for stories about the software.
4. Put the tracked link where it can be tested (see open tests), and use a different `utm_content` for each variant.
5. Report non-employee engagement, UTM sessions and demo requests, not reactions alone.

## Open tests
| ID | Question | Variants (`utm_content`) | Status |
|---|---|---|---|
| T1 | Robot vs icon style on the same Rental Intelligence Suite topic | `carousel_robot-fleet-secrets`, `carousel_icons-ai-insights` | not started |
| T2 | LinkedIn link in first comment vs in post body | same post type, alternate | not started |
| T3 | Record360 four-shots, equipment lead vs vehicle lead | `carousel_four-shots-equipment`, `carousel_four-shots-vehicle` | not started |

## Results log
| Date | Test | Result | Decision |
|---|---|---|---|
| | | | |

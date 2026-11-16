# Asana: Social Media Calendar (digital)

Project gid `1202855667985941` (Marketing team). Read from the live project when in doubt, ids below were read on 2026-11-16.

## Sections
| Section | gid |
|---|---|
| Ideas | 1202855667985943 |
| In Development | 1206394188977283 |
| Campaign Tasks | 1207806834889646 |
| Unscheduled | 1202855667985960 |
| Scheduled this week | 1202855667985957 |
| Scheduled next week | 1202855667985958 |
| Later this month | 1202855667985959 |
| No Action Needed | 1206394188977285 |
| Complete | 1204638300293532 |

## Custom fields
| Field | gid | Options (gid) |
|---|---|---|
| Brand (enum) | 1214999357262881 | PoR 1214999357262882, R360 1214999357262883 |
| Campaign / Initiative (text) | 1215046885517472 | use the same slug as `utm_campaign` |
| Post Format (enum) | 1205236026737673 | Live Video ...674, Produced Video ...675, Photo ...676, Carousel ...677, Webinar ...678, Article ...679, GIF ...680, Campaign ...681 (prefix 1205236026737) |
| Primary Objective (multi) | 1215046885517492 | Event Promotion 1215046885517493, Webinar / Content Promotion 1215046885517494, Product / Feature Launch 1215046885517495, Customer Story / Case Study 1215046885517496, Thought Leadership 1215046885517497, Hiring / Employer Brand 1215046885517498, Holiday / Seasonal 1215031362650130, Community / Charity 1215031362650131, Brand Awareness 1215031362650132, Traffic to Site 1215031362650133, Lead Capture / Demo Request 1215031362650134 |
| Social Channel (multi) | 1206394539982247 | Facebook 1206394539982248, Instagram 1206394539982249, LinkedIn 1206394539982250, Tik-Tok 1206394539982251, X (Twitter) 1206394539982252, Google Display 1206394539982253. No Threads or YouTube option. |
| Run Dates (date) | 1205234616627381 | |
| More than one Channel (enum) | 1205234616627339 | Yes 1205234616627340, No 1205234616627341 |

## Reviewers
Named in the description. Not subtasks, not assignees.
- Design: Andrew Sherrington (user gid 738358058072759), every post.
- Copy: Michael Peck, every post.
- Product: Andy Lynch (user gid 1204499320846955) for Point of Rental product posts, Bryan Osuszek for Record360 posts, especially product-related.
Michael Peck and Bryan Osuszek were not in the project member list on 2026-11-16. Look them up with `search_objects` (resource_type user) before mentioning them with a link.

## Description template
```
REVIEW NEEDED
Design: Andrew Sherrington
Copy: Michael Peck
Product accuracy: {Andy Lynch | Bryan Osuszek | not applicable}

POST
Brand: {Point of Rental | Record360}
Campaign: {slug}
Format: {carousel | image | video}
Channels: {list, including Threads or YouTube if used}
Angle: {one sentence}
Test: {T1... | none}

TRACKING
UTM sheet row: {sheet url}#gid={tab gid}&range=A{row}
Final links are in column L of the rows above, one per channel.

ASSETS
{Drive or Canva link to the slides, PDF and PNG set}
AI imagery: {none | illustration, see manifest}

SOURCES
{source URLs}
Claims to check: {list, or none}

CAPTIONS
LinkedIn:
{text}

Facebook:
{text}

Instagram:
{text}

X:
{text}

Threads:
{text}

SCHEDULING
Scheduled manually in Metricool after approval.
```

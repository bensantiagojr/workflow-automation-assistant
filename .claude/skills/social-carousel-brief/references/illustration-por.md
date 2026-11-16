# Point of Rental illustration style: pointillism

Use for stories about what the software can do. Not for people, events or product proof (use real photos and screenshots).

## Style description (stateless, for the API)
The ChatGPT thread already knows this look, but the API starts fresh every call, so every prompt carries this paragraph and, when available, reference images.

> Pointillism illustration built from small round dots of varied size, forming clean simple shapes with flowing movement. Brand greens with a few lighter and darker tones, soft and bright, on a clean background. Few elements, plenty of space, calm composition. Abstract floating interface shapes with no readable text. No words, no numbers, no logos.

## Reference images
Put 3 to 5 approved examples from the pointillism thread (the email header icons work well) in `assets/style-refs/por-pointillism/`. `generate_images.py` sends them with each request so the look stays consistent. Without them, expect drift.

## Prompt skeleton
```
{STYLE PARAGRAPH}

Show {ELEMENTS}. {COMPOSITION}. {BACKGROUND}.
```
- ELEMENTS: 2 to 3 concrete, drawable things from the source (a delivery truck, a calendar, a tent, a dashboard card as shapes), as in `email-image-prompts` step 4.
- COMPOSITION: one focal element, the rest supporting. Leave empty space where the headline will sit in the layout.
- BACKGROUND: "transparent background" for icons placed in a layout, "off-white background" for full-bleed art.

## Series consistency
Same style paragraph, same references, same palette across every slide in a series. Do not mix this style with the robot series or with photography inside one carousel. Exact hex values come from the `point-of-rental-brand` skill and the Rebrand 2026 kit.

## Do not
Logos, product brand marks, readable UI text, numbers, real people, photoreal equipment, busy scenes.

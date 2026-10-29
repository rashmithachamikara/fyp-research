Use case: infographic-diagram / scientific-educational.
Create ONE polished, exceptionally legible educational infographic, portrait A4 ratio (approximately 1808 x 2560 or higher). English. Complete flat page, no mockup, no desk, no frame. Use a warm ivory background, charcoal/navy typography and three restrained accents: A blue, B teal, C amber. Make it look like a meticulously designed illustrated field note, with crisp editorial typography, restrained friendly line illustrations and ample breathing room. A professional university explainer, easy for a beginner, with no ornamental filler. Large readable text and a clean top-to-bottom reading path. No photos, photorealism, decorative people, fake charts or invented results.

Layout: top 14% title and small conceptual road illustration; next 18% a single experiment strip; middle 54% THREE equal full-width horizontal panels A, B, C, each with a large meaningful mini-diagram at left and short text at right; bottom 14% a fair-evaluation strip and source note. Use rounded light-tinted panels, light rules, generous margins. Keep all labels fully inside the page. Each A/B/C panel has the same visual weight. Use a Bricolage Grotesque-like bold heading and clean humanist sans-serif body; body must be large enough to read at A4 size. Render only the specified copy, keeping short lines and bolding key phrases. Do not include this design guidance as image text.

TITLE, exact:
"Road damage, beyond borders"
Subtitle:
"Can a model trained elsewhere detect small or thin road damage?"
Small challenge caption by road illustration:
"New country: different roads, cameras and lighting."
Illustration: two simple road surfaces with a narrow crack and a pothole, detector bounding boxes, a subtle directional arrow. Do not imply a measured before/after improvement.

EXPERIMENT STRIP:
Heading "One shared experiment"
Three clear stages with arrows:
"Train on 3 countries" -> "Freeze settings" -> "Test on the 4th"
Under it: "Japan / India / United States / Czech Republic"
Then: "Repeat four times. No target-country data for training or tuning."
Small label: "Public data: RDD2022 | Shared detector: YOLO11"
Illustrate three source photo tiles entering a neural-model icon and one separated test tile. The country names are the set of four, not a fifth country. No country flags are necessary.

PANEL A, blue:
Large letter "A"
Heading "Match thin boxes differently"
Text "Match and weight predictions using error relative to the box's short side."
Three concise labels:
"Train: modified YOLO"
"Compare: plain NWD"
"Measure: detection accuracy (mAP)"
Mini-diagram: a very narrow labelled ground-truth crack bounding box and an offset prediction box; a small double-ended arrow across the short side labelled "short side". A second larger box shows the same offset for comparison. This is a geometry illustration, not a result. Avoid suggesting it expands boxes or guarantees tolerance. No invented equation.

PANEL B, teal:
Large letter "B"
Heading "Learn across image scales"
Text "Show one image at two scales. Encourage agreement on visible small or thin damage."
Three labels:
"Train: YOLO + consistency loss"
"Compare: consistency on all eligible boxes"
"Measure: recall + false positives"
Mini-diagram: the same illustrated crack image once large, once half-sized, with matching coordinate boxes and a bidirectional agreement link. Teacher/student labels optional, do not introduce extra text.

PANEL C, amber:
Large letter "C"
Heading "Warn about likely misses"
Text "Freeze YOLO. Train a small CNN using internal features and weak detections."
Three labels:
"Train: separate CNN head"
"Compare: learned weak-map-only head"
"Measure: miss-location AUPRC"
Mini-diagram: a YOLO block with a small lock icon feeds internal features and a weak-detection map to a small CNN, which emits a grid with a few isolated highlighted cells. Label "40 x 40 warning grid". Grid is schematic; highlighted cells mark likely missed-box centres, not crack extent. A small readable caution below the panel text: "Warnings do not recover missed cracks."

BOTTOM:
Heading "What makes the test fair?"
Four concise chips: "3 seeds" / "Matched controls" / "Ablations" / "Untouched test countries"
Bold takeaway: "All three train neural models. Each has its own research question."
Small but readable footer: "Based on proposal v8 | Proposed studies; improvements are not yet demonstrated."

Ensure accurate spelling, clean typography and uncluttered scientific content. Do not add model-performance values, accuracy arrows, claims of novelty, results or claims about Sri Lanka.

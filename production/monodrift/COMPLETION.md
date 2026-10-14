# Monodrift → NILKEEPR: implementation record

Source: https://monodrift.framer.website/ (home, about, projects, contact, privacy policy).
Date: October 14, 2026. Owner selected a direct reconstruction, superseding Athletic Index.

## Implemented reference map
- Opening: six-panel desktop cascade, 40vw introductory column, clipped mint information panels, progress count, image scaling and ordered overlap. Under1200px: source-style vertical sticky image stack. Existing NIL film is panel1; this replaces the previous frame-scrub opening.
- Typography/navigation: Tektur500 display with Inter supporting UI; compact black header and expanding menu; black/mint highlight blocks, square geometry and oversized footer wordmark.
- Showreel: full-width image reveal into a native video dialog. NIL's genuine existing explainer, captions and transcript retained.
- Expertise: numbered expanding rows, one open at a time, paired description/image, dark expanded state.
- Manifesto: three pinned statements; per-character rotateX and depth with line-wave sequencing; mint progress fill; reverse scroll restores earlier states; directional skip. Mid-transition can intentionally contain an earlier lower line and a new upper line, matching the source's wave mechanism.
- Process: three participant tabs update paired numbered explanations. Keyboard arrows switch tabs.
- Moving columns: source testimonial-column behavior applied to illustrative NIL documents, not fictional testimonials. Pause control added.
- Floating notes: source Notes thumbnail motion and preview applied to six NIL resources. Dialogs include real route destinations. Pause control added.
- About/contact/editorial pages: source hierarchy and typography adapted to real NIL copy. The seven reading-document bodies are text-identical to the prior release.

## Motion measurements and limits
Existing validated Monodrift fixture supplied the primary cascade and manifesto reconstruction. Desktop cascade uses100vh lead,120vh crossover, .709/.884 edge relationships,40vw inset,1.1 zoom and1.375 thumbnail factor. Manifesto uses150vh per statement desktop/100vh phone,140px depth,90-degree rotation, line spread.6,jitter.03,inertia.1. These are implementation values from the verified reconstruction, not a claim of access to private Framer settings.
Secondary entrance650–700ms and menu/interaction easing are reconstructed estimates. Source private editor settings were not accessible. No separate UI sound effect was verified; no invented click or swoosh was added. The existing explainer retains its audio after a user clicks Play.

## Verification
-11routes × desktop1440×900, tablet820×1180, phone390×844; opening/middle/footer captures in local production/monodrift/build.
-21 repaired reading-page captures after independent reviewer found a nested-grid overlap. Policy navigation spacing and transient heading spacing repaired.
-Forward and reverse manifesto checked in browser; full athlete/guardian hold frames saved. Source-derived mixed-line intermediate state documented above.
-Expertise row switching, School participant tab, resource dialog open/close, native video playback (readyState4, unpaused), menu/Escape, phone form required-field validation and district query selection checked.
-Internal route/anchor validation repaired transcript→explainer link. No contact inquiry sent.
-No horizontal overflow in the original33 route/viewport checks; reading long-word wrapping subsequently strengthened.
-JS syntax checks pass. Reduced-motion/no-JS fallback rules inspected in source; environment emulation was not performed. No guarantee of all-device behavior is claimed.
-Independent rendered review closed all identified P1/P2 findings. Reviewer did not independently watch continuous motion; primary agent performed moving interaction checks.

## Content and assets
NIL assets and real service/policy content replace agency projects, pricing and testimonials. No Monodrift agency artwork or brand claims transplanted. Font OFL retained. No new paid media generation. Existing video and image bytes unchanged.

## Reproducibility
Canonical pages and mono*.css/js are the deployable build. scripts/build-monodrift.py uses the local reference-library fixture and production/monodrift/baseline snapshots; it is a workspace build utility, not a standalone distributed template. macOS offloaded project assets, so final verification used a hydrated /tmp mirror and release used a clean GitHub checkout. Original workspace edits remain intact.

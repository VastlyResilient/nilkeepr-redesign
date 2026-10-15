# Scoped mobile gallery review

Reviewed current mono-home.js / mono.css diff and full-mobile-gallery.png on 2026-10-14. Independent source and supplied rendered-image review; browser interaction and moving-sequence verification remain with the parent agent.

## Finding resolved in source

P1: Desktop still-introduction toggle now stops cascadeFrame while leaving the desktop cascade displayed. The existing desktop stylesheet hides #mstack, and the new rules only address html:not(.film-static). After selecting “Use still introduction”, fixed panels can remain frozen at their last transform and cover subsequent content. Resolved: independently verified final CSS explicitly hides #cascade and .phone-gallery-caption and shows #mstack under html.film-static, all with !important. This closes the source finding. Runtime toggle verification remains with the parent browser checks.

## Rendered observation

The supplied 390 × 844 screenshot shows a readable full-width green Consent First caption with counter and body copy; there is no overlapping caption text. The gallery image is partially clipped in the captured intermediate state and the next queued label is truncated. That state alone does not demonstrate a defect or establish the entire animation sequence is correct. Header/menu control remains visible.

## Source checks

- The <1200 early return is removed and the full cascade is enabled at phone and tablet widths.
- Fine-pointer gating leaves touch scrolling native while retaining desktop Lenis.
- Caption hyperlink targets come from the same gallery data. Pointer and keyboard access are disabled while the caption is hidden or transitioning.
- JavaScript syntax check passes (node --check mono-home.js).
- The new CSS and filmReduced-only guard override the previous OS reduced-motion gallery fallback. Parent confirmed that full desktop gallery motion on mobile is explicitly requested and is the intended default; the explicit still mode is retained. OS reduced-motion does not disable this gallery.

## Verification gaps

No independent browser execution, touch-device browser chrome resize test, slow/fast/reverse scroll sequence, orientation test, desktop regression screenshots, or keyboard traversal was performed in this scoped review. In particular, .pfix uses 100svh on mobile while JS geometry uses innerHeight; verify expanded and collapsed mobile browser chrome for bottom-edge gaps. Parent browser testing is required before publication.

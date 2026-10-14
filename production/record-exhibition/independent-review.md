# Independent rendered review — Record Exhibition

**Final status: PASSED for the reviewed rendered visual criteria.** All three actionable P2 findings have been visually rechecked and closed. No remaining P0–P2 visual finding was established in the inspected evidence. This is not an independent functional, accessibility-conformance, or deployed-site acceptance certification.

Date: 2026-10-14. Reviewer: independent review subagent; no product code edited.

## Scope and evidence

Inspected all 11 `captures/*-sheet.jpg` contact sheets, covering 390px mobile and 820px tablet opening/middle/footer states: index, platform, about, data-and-consent, contact, privacy, terms, communications-consent, email-policy, transcript, and 404. Also inspected all 11 desktop full captures. Long legal-page full captures are useful for composition only at displayed scale; the mobile/tablet sheets carry the legibility observations. Inspected the selected source `production/product-design-redesign/01-record-exhibition.png` alongside platform implementation. Saved `captures/independent-source-platform.jpg` as a comparative overview (different fit scales; not a pixel-match claim).

Deliberate corrections excluded from defects: blank conceptual records instead of invented student data/signatures; ruled capability index instead of three repeated icon cards; preserved landing film/staging rather than replacement by the inner-page hero.

This is an independent visual review of supplied browser renders. I did not operate the browser, exercise forms, inspect runtime focus, test links, scrub motion, or independently validate legal content. Main-agent functional evidence must cover those separately.

## Findings

No P0 or P1 product defect established by these renders.

### P2 — Email policy numbers detach from their headings

- Route/file: `email-policy.html`.
- Selectors: `.reading-document > p` containing `01`–`06`, followed by `.reading-document > h2`; spacing supplied by `.reading-document h2` in `exhibition.css`.
- Evidence: `email-policy-desktop-full.jpg`, `email-policy-sheet.jpg` mobile middle. `04` sits immediately after the prior paragraph, then a large blank interval precedes “Unsubscribe and preferences.” The number visually belongs to the previous section. The same pattern repeats for the other numbers.
- Repair: group each number with its heading or give numbered sections a wrapper. Put inter-section space before the number and keep number-to-title spacing close (roughly 12–20px at current type sizes). Recheck mobile and desktop.

### P2 — Initial journey proportion drift (repair reported; recapture pending)

- Routes/files: `platform.html`, `index.html`; `.ex-journey`, `.ex-roles article`, `.ex-record-art` in `exhibition.css`.
- Initial platform desktop capture has a much taller dark journey relative to its width than the selected source, leaving large gaps between role descriptions and a broad empty area beneath the short art. The large row minimum (`330px`) dominates the scene rather than the compact record/roles relationship.
- Main agent reports reducing desktop role minimum to 240px, tablet to 265px, and desktop section padding from 100px to 80px. That is a targeted repair. Updated in-view capture is required before closing this finding; sticky behavior is not assessed by the full-page image.

## Evidence gaps to close

1. Initial `index-desktop-full.jpg` has empty image blocks and a large white film runway. `route-checks.json` marks three unloaded index images. This is consistent with full-page capture of lazy images/pinned film, and is **not established as a broken product**. Capture the home exhibition sections in view after image decode and film release; retain the original evidence instead of silently replacing it.
2. Mobile contact opening/middle/footer sampling skips the inquiry form. Capture `contact.html #inquiry` at 390px, with all labels/controls and the email-draft note visible across successive viewports.
3. Tablet/mobile about sheets show only the initial audience and first three horizontal controls. Verify reachable Schools & districts and Parents & guardians controls, focus visibility, and each panel in the main functional pass.
4. The supplied screenshots do not establish scroll timing, reverse behavior, menu focus containment, reduced motion, JS/media failure paths, direct routes, input validation, or mailto draft correctness. Do not report those as independently passed from this review.

## Visual observations within scope

Inner-route opening headings and paragraphs fit the inspected mobile widths; no clipped headline or overlapping body text is apparent. The data/consent image, navy boundary pair, and ruled document layouts are coherent with the cobalt/white/navy identity. Contact desktop form labels and controls align clearly. Footer directory and legal links remain visible on the provided phone captures. Platform, data, about, contact, and document pages use appropriate different compositions; shared footer repetition is intentional. The reused cobalt-divider artwork across data, contact, and about is thematically consistent, though it should not be represented as distinct photography. Source fidelity is directional rather than exact, especially in background blending, type scale, and lower-page content length. Blank art is recognized as the explicit correction, not missing document data.

Acceptance remains with the owner after evidence gaps, functional checks, and targeted fixes.

## Independent recheck of corrected evidence

Reopened: `platform-desktop-full-fixed.jpg`, `platform-desktop-journey-fixed.jpg`, both `email-policy-*-numbering-fixed.jpg`, `contact-mobile-form.jpg`, `menu-mobile.jpg`, `index-desktop-full-loaded.jpg`, `index-desktop-exhibition.jpg`, `index-desktop-capability.jpg`, and `index-desktop-data.jpg`.

- Closed both original P2 findings. The in-view journey now brings art and all three role descriptions into a coherent scene without the prior excess spacing. Policy numbers 04 and 06 visibly attach to their following headings.
- Closed the home unloaded-art evidence gap: in-view artwork loads. Full-page pinned/fixed positioning remains an unsuitable source for assessing the film runway; its white void is a capture artifact, not a newly asserted product defect.
- Phone menu labels and primary controls are readable without horizontal clipping. The phone form's visible labels, inputs and select align correctly; focused name input has a clear blue focus boundary. Bottom form controls/notice remain outside this particular capture.
- Received main-agent reports of desktop film progress reversing 0 → .3704 → 0, phone frame 61 with ready=true, tool/privacy control updates, and Escape closing the menu. These are attributed main-agent functional checks, not independently performed by this reviewer.

### Newly visible P2 — Capability artwork crop loses its object silhouette

- Route/file: `index.html`; `.ex-tool-art img` in `exhibition.css`.
- Evidence: `index-desktop-capability.jpg`.
- The short landscape artwork window uses `object-fit: cover` on the portrait record stack. Both upper and lower paper boundaries are cropped, leaving mostly a large blank paper patch. Unlike the journey, this view no longer clearly reads as a stack of records.
- Repair: fit the whole stack within the stage-colored frame (e.g. contain with appropriate padding), or use an intentionally prepared wider composition that preserves recognizable paper edges. Inspect the desktop and mobile capability states after adjustment.

Current disposition: original visual repairs verified; final visual pass pending capability crop adjustment. This does not assert a functional failure. Functional and publication scope limits above remain in force.

Final recheck attempt: `contact-mobile-form-bottom.jpg` confirms the lower form fields, clear textarea focus, full-width email-draft button, explanatory no-storage note, and direct contact links without clipping. Mobile form visual coverage is complete. `index-desktop-capability-fixed.jpg` currently shows the landing film rather than capability artwork, so it cannot verify the crop repair. Correct in-view evidence requested; no new product defect asserted.


## Final visual disposition

Reopened the corrected `index-desktop-capability-fixed.jpg` after the capture-target correction. The stack is now fully visible and centered, with top edges, bottom edge, shadow, and surrounding stage preserved. It reads as a record exhibit again. Closed the capability-crop P2.

**Rendered visual review: PASSED within the inspected scope.** Original and follow-up evidence establish resolution of journey spacing, policy-number grouping, artwork loading, capability crop, and mobile form coverage. No remaining P0–P2 visual findings established. New desktop capability crop was verified; a separate corrected mobile capability screenshot was not supplied, so that exact responsive state is not independently certified. Main-agent reports cover functional control updates and film behavior; those remain explicitly attributed, not independently replayed. Owner acceptance and deployed verification remain separate.

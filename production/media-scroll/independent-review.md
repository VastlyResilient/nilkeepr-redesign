# Independent rendered review — media and scroll update

Reviewed 23 supplied PNG captures plus the current mono-home.js and mono.css. This is independent visual/code review; no live interaction tests or source/reference equivalence claims are made here. Parent-reported frame sequence tests were not independently rerun.

## Findings requiring repair

1. Resources title/description collide with text on semantic document tiles at desktop and tablet. The central word RESOURCES, eyebrow and supporting sentence are superimposed on Privacy policy and Oversight record text. Preserve diagonal movement but reserve a clear central reading area or give title copy a suitable opaque backdrop. Evidence: resources-desktop.png, resources-tablet.png.
2. Communications consent tile heading clips horizontally at desktop and tablet. The fixed small tile width combined with large unbreakable heading causes truncation. Allow a controlled word break, smaller type for the long heading, or wider tile. Evidence: resources-desktop.png, resources-tablet.png.
3. Screenshot state mismatch prevents responsive acceptance of capabilities and resources: capabilities-tablet.png shows Privacy policy page; capabilities-mobile.png and resources-mobile.png show open Privacy policy dialog. Recapture intended sections after closing dialogs and navigating to homepage explicitly.
4. Partial film frame failure is not handled after canvas activation. filmFrame() returns on unavailable image while canvas retains ready and CSS hides video. A failed target frame therefore leaves stale canvas visible indefinitely at that scroll position without the manual video fallback. Clear ready on actual image load error, allow successful subsequent frame recovery, and test one missing middle frame. Initial missing frames and reduced-motion do retain native video fallback by code inspection.

## Passing observations within supplied evidence

- Platform, About, Data & consent and Contact opening captures at desktop, tablet and mobile: legible typography, sensible wrapping, no horizontal clipping observed. Contact mobile screenshot stops before the form, so it is not form validation.
- Capabilities desktop: distinct semantic record panel fits the accordion composition; visible text readable.
- Privacy resource dialog at desktop, tablet and mobile: contents, close control and Read more CTA legible, no visible overlap.
- Desktop film middle: frame sits in existing cascade and opportunity card remains readable. Partial outgoing headline is consistent with an intermediate scroll state; not evaluated as opening state.
- Mobile film middle: frame fills the card, bottom copy remains readable, CTA is fully visible.
- Main illustrative image repetition has been removed in inspected active page sources, with bitmap use concentrated in unique cascade panels, About and Data & consent. Logo, video poster, mutually exclusive responsive media and thumbnail-to-dialog semantic record reuse excluded.

## Scope limits

This evidence does not establish whole-site footer/middle coverage, touch/keyboard behavior, direct-route behavior, all accordion states, all six resource dialogs, reduced-motion rendered result, JavaScript/media failure rendered result, or deployed verification. Owner acceptance remains separate.

## Follow-up review of nine `*-fixed.png` captures

- Resolved: desktop/tablet Resources central copy no longer collides with the moving covers; white reading field is clear.
- Resolved: cover title no longer overflows its own box. Remaining low-priority typography polish: Communications breaks mid-word into COMMUNICATIO / NS on desktop and COMMUNICATION / S on mobile. A concise cover label or slightly smaller fitted title would read better; full dialog title is correct and readable.
- Resolved: mobile Resources uses stable two-column covers; visible lower covers are legible and separated. Screenshot captures lower grid and footer, not the Resources heading/top two covers.
- Resolved: Communications consent dialog is legible at desktop/tablet/mobile; close and CTA visible.
- Resolved: capabilities mobile now shows intended heading and accordion; desktop intended section also captured. Visible content is legible.
- Still missing evidence: capabilities-tablet-fixed.png shows the explainer reel rather than capabilities, so tablet capability layout remains unverified.
- Partial film failure now removes canvas ready class to expose native video. One recovery edge case remains in code: after failure, returning directly to lastRendered frame triggers the equality early return before ready is restored. Only skip drawing for matching frame when canvas is already ready, or reset lastRendered on error. This is fallback persistence rather than a frozen-canvas failure.

All prior scope limits remain. Forward/stopped/reverse frame tests are parent-reported, not independently rerun.

## Final focused follow-up

All actionable findings from this independent media/scroll review are closed within the reviewed scope.

- capabilities-tablet-open.png now provides the missing tablet state: heading, Consent accordion text, CTA and semantic record panel are legible and fit without overlap.
- records-tablet.png shows readable dark text on light record tiles; the three-column moving composition remains intact. Edge masking is visible as intended; central cards are readable.
- Current filmFrame code requires canvas.ready before its matching-frame early return, fixing return-to-last-frame recovery. Parent reports browser failure fixture frame 0 ready → missing 72/native fallback visible → reverse 0 ready. Code change independently inspected; fixture execution not independently repeated.
- Current Communications thumbnail markup uses COMMUNICATIONS kicker plus Consent title, removing the long heading overflow/broken-word cause while keeping full dialog details.

This closes the review findings rather than granting whole-site or deployment acceptance. The previously stated live-interaction, full-route/state, failure-render and deployment coverage limits remain; no additional broad audit was performed.

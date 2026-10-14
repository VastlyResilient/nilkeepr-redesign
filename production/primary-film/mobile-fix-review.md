# Independent mobile fix review — 2026-10-14

Scope: read-only source review of `mono-home.js`, `mono.css`, `index.html` diffs and `mono.js` menu integration; independent visual inspection of `mobile-reduced-fixed.png`. No physical-device testing was performed by this reviewer. Parent is testing a forced-reduced-motion fixture in a real browser.

The screenshot at 390 × 844 shows a visible film frame, progress bar, kicker and a partially revealed first headline. It supports the intended intermediate reveal appearance, but a single screenshot cannot establish forward/reverse frame progression or mobile Safari behavior.

The JavaScript now separates the primary film from the OS reduced-motion preference, while retaining that preference for Lenis/cascade/manifesto effects. Local storage access is guarded. The menu focus trap queries links and buttons dynamically, so the newly appended film control participates correctly. The button labels describe their next action and the control preserves the visitor choice. Cache versions for the home stylesheet/script are updated.

## Findings requiring resolution

1. **P2 — Reduced-motion minimum height remains on short phones.** `html:not(.film-static) .landing-pin` restores sticky positioning and `height:100svh`, but does not override the existing reduced-motion `min-height:780px`. At a portrait viewport such as 375 × 667, the automatic film retains a pin taller than the viewport; final copy/CTA can extend below the fold. Reset the minimum height for the automatic branch to match the normal desktop/mobile/landscape values, and verify at a short portrait viewport.

2. **P2 — Still-introduction control can overflow the fixed menu.** The new control is appended below seven navigation links, the promotional feature and two contact links. `#mono-menu` is fixed between 70px and the viewport bottom, with no vertical scrolling. Its content can exceed the available height, especially at 375 × 667 or landscape, leaving the newly offered still control below the visible screen. Make the menu vertically scrollable, preserve adequate button size, and test reachability by touch and keyboard.

## Remaining evidence

Verify these repairs in rendered short-phone and landscape states, plus still/film toggling and persistence. Physical iPhone Safari and the deployed revision remain outside this review. This report is not owner acceptance.

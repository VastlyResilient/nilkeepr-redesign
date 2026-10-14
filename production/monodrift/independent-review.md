# Independent rendered review — 2026-10-14

Status: identified P1/P2 visual findings resolved in supplied repair evidence. No remaining blocking composition issue found in reviewed captures. This is limited static rendered review, not publication acceptance.

Reviewed the supplied browser captures for 11 routes (index, platform, data-and-consent, about, contact, privacy, terms, communications-consent, email-policy, transcript, 404) at desktop 1440 × 900, tablet 820 × 1180, and phone 390 × 844. Opening/middle/footer captures were composed into review/desktop-all.jpg, review/tablet-all.jpg, and review/mobile-all.jpg. Source desktop-sheet.jpg and inner-sheet.jpg were inspected, with a normalized source/build opening comparison saved as review/compare-opening.jpg. This comparison uses the lower-resolution source contact sheet because the source desktop-00.png could not be decoded during review.

## Findings

1. **P1 — TOC overlays the reading text on desktop and tablet.** Evidence: build/privacy-desktop-middle.png, build/privacy-tablet-middle.png, build/terms-tablet-middle.png, build/data-and-consent-tablet-middle.png. The document and its sticky table of contents occupy the same narrow left column while most of the page is blank. Text becomes unreadable where they intersect. mono.css line 3 applies the two-column grid to .inner-content, but the document and navigation are nested in .reading-layout; give that wrapper the intended columns or flatten its children. Recheck all reading routes, especially the long privacy/terms documents, at middle scroll and tablet width. Source privacy-policy-middle in inner-sheet.jpg separates the TOC and text; current build does not reproduce that structure.

2. **P2 — Policy navigation links run together.** Evidence: build/communications-consent-desktop-opening.png and mobile policy openings. The text renders as “PrivacyTermsCommunicationsEmail policy” without visible separation, making navigation hard to parse and touch targets cramped. Give the policy-link group layout, spacing, wrap and comfortable link padding; check all four policy pages on phone and desktop.

## Other observations

The 390px OPPORTUNITY heading fits within its highlighted box without clipping. Contact tablet opening has readable labels and a clearly differentiated form; phone opening stacks the introduction correctly. The opening comparison retains the source left-column proportion, Tektur display type, mint CTA and dark/mint highlight treatment while substituting NIL content and film. That substitution was explicitly part of this review brief. Footers are consistently composed across the route screenshots, and no separate P1 was found in their static captured states.

No code was edited. This is an independent screenshot review, not a claim that interactions, moving sequences, navigation, keyboard operation, mail client behavior, reduced motion, JS/media failure or deployed behavior were tested. The supplied index opening/middle/footer sampling does not include every late home section; manifesto sequence captures were still pending. Whole-site regression and those state checks remain separate gates.


## Follow-up rendered review

Reviewed all 21 `*-{desktop,tablet,mobile}-repaired.png` captures covering platform, data-and-consent, communications-consent, email-policy, privacy, terms, and transcript. New montage evidence: review/desktop-repaired.jpg, review/tablet-repaired.jpg, review/mobile-repaired.jpg.

- **P1 reading overlap: resolved in supplied repaired captures.** Desktop/tablet TOC now occupies its own left column and the document uses the right column. Phone documents remain stacked. Long privacy hash text wraps within its column. The captures verify the separation visually; they do not verify keyboard/wheel access to every TOC item.
- **P2 policy-link spacing: implementation corrected; rendered closure pending.** mono.css lines 10–11 now give .reading-nav wrapping, horizontal/vertical gaps and margin. The supplied repaired policy captures start below that group, so they do not directly show the fixed policy links.
- **P2 home licensing heading/body collision:** build/index-mobile-footer.png shows the highlighted second heading line extending to approximately y600 while the supporting description begins approximately y594. Add normal flow clearance below the heading and verify after reveal settles. The closely related FAQ heading/description in index-tablet-footer.png also warrants a settled-state spacing check.
- **Manifesto state concern, not yet assigned defect priority:** manifesto-start.png is readable and centered. manifesto-mid.png combines new “PARENTS CONSENT.” / “RECORDED. TIMESTAMPED.” lines with preceding “WITH THEIR STORY.” text. manifesto-reverse.png shows empty dark highlight rectangles above the remaining old lines. These can be transition frames, but a static review cannot distinguish deliberate stagger from stale content. Verify a moving forward/reverse sequence and settled holds; ensure no obsolete line or empty highlight remains at hold. Do not treat these three captures alone as motion acceptance.

Other home captures preserve the intended source-inspired large type, mint highlights, monochrome record panels and contrasting dark/light sections. The index-desktop-footer capture is actually an intermediate record-wall state, and the phone/tablet footer captures are licensing/FAQ states; therefore these are not independent evidence of the actual home footer. No additional blocker found within those sampled states.


## Final repair evidence

Inspected build/licensing-mobile-repaired.png, build/policy-nav-repaired.png, build/manifesto-guardian-hold.png and build/manifesto-athlete-reverse-hold.png.

- **Licensing collision resolved:** phone heading/highlight now has a clear approximately 54px gap to its description. The heading, support text, licensing card, list and CTA are legible and distinct.
- **Policy navigation resolved in supplied tablet capture:** all four links now have distinct spacing and the document/TOC remain separated. This directly closes the observed joined-label problem; phone touch interaction was not independently exercised.
- **Manifesto holds are complete:** guardian hold displays the full consent statement including “REVOCABLE.”; reverse athlete hold restores the full original report/story statement with filled highlight blocks. No stale line or empty highlight remains in these hold captures. The implementer identifies the mixed intermediate lines as the intentionally staggered source-fixture wave, not a timed stale-text defect. The reviewed holds support that explanation.

I did not independently watch the continuous moving sequence, operate its scroll controls, or compare source/build timing frame by frame. The screenshots establish coherent supplied hold states and readable composition; they do not establish independent motion fidelity. Prior findings remain above as repair history, not unresolved current defects. No additional blocking composition issue is visible in the reviewed repair captures. Final owner acceptance, whole-site interaction regression and deployed revision verification remain outside this static review.

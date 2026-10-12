# Independent concept review — 12 October 2026

Reviewer: separate review agent, with no implementation edits. Scope: three NILKEEPr direction previews, not a production website, compliance assessment, or complete accessibility audit.

## Evidence inspected

Read `research/DIRECTION-RECORD.md`. Visually inspected all nine `output/playwright/{one,two,three}-{desktop,tablet,phone}-full.jpg` captures. Inspected native-size detail captures spanning top, middle, and footer: One phone top and desktop middle; Two tablet top and phone middle; Three tablet middle and phone footer. Opened all three localhost routes in the in-app browser and exercised each protected-information selector. Two was also switched back to school-visible information.

## Findings

1. **Concept presentation is coherent at all three sizes.** No overlapping headings, obscured primary buttons, or obvious viewport-level horizontal clipping was visible. Phone sections and license options stack in reading order. The Three footer remains legible at the native phone capture size. One communicates an illustrative record; Two presents a relationship diagram; Three has an editorial chapter index. The concepts are sufficiently distinct to support selection.
2. **The selectors work on all three routes.** Clicking Protected information changed the selected state, heading, explanation and five-item list to full dates of birth, parent contact information, private communications, financial account details, and exact compensation figures. Two returned to the original five school-visible items. The settled Two and Three browser screenshots show dark, readable data-list text on light backgrounds. No submission or external communication was performed.
3. **Initial full-page screenshots captured incomplete data-list entrance animations.** In Two/Three, several rows are pale or absent in the initial full-page image even though browser interaction proves they render. This is a capture-evidence issue rather than a demonstrated persistent selector failure. Selection screenshots should be regenerated after entrance animation completion. The implementation agent reports a capture-wait correction; refreshed evidence is addressed below.
4. **Initial workflow content is visually faint before scroll activation.** The original full-page captures show the four role explanations at reduced opacity. This can hamper skimming during movement. The implementation agent reports increasing the minimum opacity from .55 to .8; refreshed evidence is addressed below.
5. **Minor production refinement: clarify the demo action's destination.** Request a school demo is a mailto link, with the published school email nearby and an explicit footer note that booking integration follows selection. This is acceptable for the stated concept stage; the selected build should integrate booking or label the action as an email request so visitors with no mail client are not surprised.
6. **Claims remain appropriately bounded for a concept.** No fabricated student records, invented testimonials, numeric prices, performance promises, or certification seals were observed. One visibly labels the record as illustrative; the common footer distinguishes illustrations from live product screens. Two explicitly separates school oversight from deal-making. This review does not independently validate every company-source feature statement; production claims still require the source/content review identified in the direction record.

## Scope limits

This review did not test authentication, booking delivery, email sending, legal compliance, every keyboard interaction, every viewport width, or a complete production route/content inventory. Browser selector tests used the current desktop viewport; phone/tablet findings are visual screenshot inspection. No full-site release approval is implied.

## Recheck status

Freshly reopened `one-phone-top.jpg`, `two-desktop-full.jpg`, and `three-tablet-full.jpg` after regeneration (file times 15:04–15:05 local). One’s phone heading now has comfortable right-side clearance. Two desktop and Three tablet show all five data rows at readable opacity, and the workflow role text is visibly stronger. The earlier capture/readability findings are resolved in these representative refreshed checks. No remaining blocker to concept selection was found. This is approval for direction discussion only, with the production scope limits above.

Read the implementation agent’s `research/resilience.json` as supplementary evidence: all twelve route/width cases (320, 390, 1024, 1440) report no viewport or heading overflow, reduced-motion sampled elements report opacity 1 and transform none, and no-JS cases report four workflow steps. These checks were not independently rerun by this reviewer. The implementation agent also plans the clearer mailto CTA label “Email for a school demo”; the original wording observation above documents the reviewed state.

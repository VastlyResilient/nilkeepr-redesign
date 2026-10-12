# NILKEEPR school-compliance cinematic redesign

Published at https://vastlyresilient.github.io/nilkeepr-redesign/.

The home page uses a generated eight-second 2K film, delivered as matched desktop and portrait WebP sequences. Native scrolling controls the frames and staged HTML. A still preference is available inside the menu. Source-company explainer, captions, and transcript remain distinct from conceptual artwork.

The school-service journey includes platform, data/consent, About, Contact and source policy pages. The contact form opens an email draft; it does not submit to a backend. Authentication and account privacy controls remain genuine external integrations.

`cinematic.css` and `cinematic.js` are the shared runtime. `scripts/verify-cinematic.mjs` checks frame progression/reversal, interaction states, and responsive content. `scripts/resilience-film.mjs` covers Chromium/WebKit, failed frame fallback, no-JS and explicit still preference. Research/source ledgers and generation receipts remain local and are not distributed with the site.

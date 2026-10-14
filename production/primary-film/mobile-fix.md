# Mobile film correction
Root cause found in source: prefers-reduced-motion caused early return in filmFrame, hid canvas and collapsed hero scroll track. This reproduced the reported static behavior, but the owner phone setting is not directly observed.
Core film now defaults to scroll progression independently of OS decorative-motion preference. Explicit still introduction remains in menu and persists. CSS preserves pinned travel and canvas under reduced rules.
Browser fixture forces the production reduced branches and CSS media blocks active; 390x844 frame0→32→21 with corresponding text progression. 375x667 pinheight667; menu still/scroll toggles operable after overflow repair. Physical iOS/Android device not tested.
Public normal-path verification follows deployment. New asset query film4 prevents stale CSS/JS combination. No content or visual direction change.

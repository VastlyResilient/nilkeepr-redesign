
(() => {
const P = [{"t": "THE OPPORTUNITY", "l": "Opportunity", "m": "Athlete led", "n": "Student-led opportunity. A clearly defined school role.", "img": "assets/film/desktop/000.webp", "video": "assets/film/film.mp4", "href": "about.html"}, {"t": "THE DISCLOSURE", "l": "Disclosures", "m": "Start with the record", "n": "Self-reported activity, eligibility context and disclosure history.", "img": "assets/athletic/disclosure.webp", "href": "platform.html"}, {"t": "CONSENT FIRST", "l": "Consent", "m": "Recorded. Revocable.", "n": "Parent or guardian consent governs the school view for minors.", "img": "assets/athletic/access.webp", "href": "data-and-consent.html"}, {"t": "A DEFINED VIEW", "l": "School access", "m": "Read-only oversight", "n": "Schools observe relevant records. They do not manage the deal.", "img": "assets/athletic/court-index.webp", "href": "data-and-consent.html"}, {"t": "THE AUDIT TRAIL", "l": "Documentation", "m": "Context and continuity", "n": "Disclosure history, logged access and documentation for review.", "img": "assets/athletic/audit.webp", "href": "platform.html#capabilities"}, {"t": "YOUR NEXT STEP", "l": "Your institution", "m": "Make the connection", "n": "Explore the service with the NILKEEPR school team.", "img": "assets/exhibition/opportunity.webp", "href": "contact.html"}];
const ARR = '<svg viewBox="0 0 22 34" fill="none"><path fill="#161616" d="M21.155 18.385 5.54 34H0l16.344-16.344h4.811zm0-2.77v.73h-4.81L0 0h5.54z"/></svg>';
let filmReduced=false;try{filmReduced=localStorage.getItem('nil-film-static')==='true'}catch{}
document.documentElement.classList.toggle('film-static',filmReduced);
const reduced = filmReduced;document.documentElement.classList.toggle('motion-reduced',reduced);
const params = new URLSearchParams(location.search);
const noLoader = params.has('noloader');

/* ---------- Lenis (Framer Lenis component: intensity 18 -> duration 1.8) ---------- */
let lenis = null;
if (window.Lenis && !reduced && matchMedia('(hover: hover) and (pointer: fine)').matches) { lenis = new Lenis({ duration: 1.8, smoothWheel: true }); window.lenis = lenis; const raf = (t) => { lenis.raf(t); requestAnimationFrame(raf); }; requestAnimationFrame(raf); }

const root = document.documentElement;
P.shift(); // Film now owns the opening; do not repeat it in the gallery.
/* ---------- Nav accent dot cycles the template's swatches (estimated cadence) ---------- */
/* ---------- Cascade ---------- */
const casc = document.getElementById('cascade');
const G = { leadVh: 100, crossVh: 120, edge1: .709, edge2: .884, leadInset: 0, zoom: 1.1, thumbAspect: 1.375, settle: .05 };
const clamp = (e) => e < 0 ? 0 : e > 1 ? 1 : e, lerp = (a, b, t) => a + (b - a) * t, eio = (e) => e < .5 ? 2 * e * e : 1 - (-2 * e + 2) ** 2 / 2;
const panels = P.map((p, i) => {
  const wrap = document.createElement('div'); wrap.className = 'pwrap';
  const media = p.video ? `<canvas class="scroll-film" aria-label="NIL opportunity film controlled by scrolling"></canvas><video src="${p.video}" poster="${p.img}" muted playsinline controls preload="none"></video>` : `<img src="${p.img}" alt="" ${i < 2 ? 'loading="eager"' : ''} decoding="async" draggable="false">`;
  wrap.innerHTML = `<div class="pfix" style="z-index:${2 + i}"><div class="pclip" style="transform:translate3d(${i ? 100 : 0}vw,0,0)"><div class="pintro ">
    <div class="scrim"></div>
    <div class="win"><div class="media">${media}</div></div>
    ${i > 0 ? `<div class="queue"><span class="qlabel">${p.l}</span><span class="qnum">${i + 1}</span></div>` : ''}
    <div class="counter"><div class="" style="position:absolute;inset:0"><a class="card" href="${p.href}"><div class="cwrap"><span class="cnt">${i + 1}<i></i>${P.length}</span><span class="ttl">${p.t}</span><span class="note">${p.n}</span></div><span class="arr">${ARR}</span></a></div></div>
  </div></div></div>`;
  casc.appendChild(wrap);
  return { wrap, fix: wrap.querySelector('.pfix'), clip: wrap.querySelector('.pclip'), win: wrap.querySelector('.win'), media: wrap.querySelector('.media'), queue: wrap.querySelector('.queue'), label: wrap.querySelector('.qlabel'), counter: wrap.querySelector('.counter') };
});
const phoneCaption=document.createElement('div');phoneCaption.className='phone-gallery-caption';casc.appendChild(phoneCaption);let captionIndex=-1;
const nav = document.getElementById('nav');
let docTop0 = 0;
function measure() { docTop0 = casc.getBoundingClientRect().top + scrollY; }
function cascadeFrame() {
  if (filmReduced) return;
  const vh = innerHeight, vw = innerWidth, M = vh + 1, N = G.leadVh / 100 * vh, Pc = G.crossVh / 100 * vh, r = P.length, F = N + (r - 1) * Pc;
  panels.forEach((pn, n) => { const h = n === 0 ? N : n === r - 1 ? Pc + vh : Pc; if (pn._h !== h) { pn._h = h; pn.wrap.style.height = h + 'px'; } });
  const maxS = Math.max(0, document.documentElement.scrollHeight - vh);
  let z = Math.min(Math.max(scrollY, 0), maxS) - docTop0;
  let H = 0; if (z < 0) H = -z; else if (z > F) H = -(z - F);
  const a = Math.max(0, Math.min(F, z));
  const U = Math.min(a / (1 - G.settle), F);
  const W = (e) => { const s = e === 0 ? 0 : N + (e - 1) * Pc, L = e === 0 ? N : Pc; return eio(clamp((U - s) / L)); };
  if(innerWidth<1200){let active=0;for(let i=1;i<r;i++)if(W(i)>.8)active=i;if(active!==captionIndex){const p=P[active];phoneCaption.innerHTML=`<a class="card" href="${p.href}"><span class="cnt">${active+1} / ${r}</span><span class="ttl">${p.t}</span><span class="note">${p.n}</span></a>`;captionIndex=active;}const opacity=(active<r-1?1-clamp(W(active+1)/.3):1);phoneCaption.style.opacity=z<0||z>F?0:opacity;phoneCaption.style.pointerEvents=z>=0&&z<=F&&opacity>.95?'auto':'none';phoneCaption.querySelector('a').tabIndex=z>=0&&z<=F&&opacity>.95?0:-1;}
  const ae = (e) => { if (e <= 0) return 0; let t; if (e === 1) { t = lerp(1, G.edge1, W(0)); t = lerp(t, 0, W(1)); } else { t = lerp(1, G.edge2, W(e - 2)); t = lerp(t, G.edge1, W(e - 1)); t = lerp(t, 0, W(e)); } return t; };
  const oe = Math.round(G.leadInset / 100 * vw * (1 - W(0))), Gw = Math.max(1, vw - oe);
  root.style.setProperty('--cascade-inset', oe + 'px'); root.style.setProperty('--cascade-lead', W(0).toFixed(4));
  panels.forEach((pn, n) => {
    pn.fix.style.width = Gw + 'px';
    pn.fix.style.transform = `translate3d(${oe}px, ${Math.round(H)}px, 0)`;
    const K = ae(n), q = K * Gw;
    pn.clip.style.transform = `translate3d(${q}px, 0, 0)`; pn.clip.style.pointerEvents = K < .98 ? 'auto' : 'none';
    pn.counter.style.transform = `translate3d(${-q}px, 0, 0)`;
    const caption=innerWidth<1200?(n===0?1:clamp((W(n)-.65)/.2))*(n<r-1?1-clamp(W(n+1)/.3):1):1;pn.counter.style.opacity=caption;pn.counter.querySelector('a').tabIndex=caption>.95?0:-1;pn.counter.querySelector('a').style.pointerEvents=caption>.95?'auto':'none';
    const ce = n === 0 ? 1 : W(n), le = clamp(ce / .35), ue = le * le * (3 - 2 * le), de = n === 0 ? W(0) : ce, J = lerp(G.zoom, 1, de);
    pn.media.style.width = vw + 'px'; pn.media.style.height = M + 'px';
    let w = Gw, h = M, s = (Gw - vw) / 2;
    if (n > 0) {
      const e = n + 1 < r ? ae(n + 1) : 1;
      w = Math.max(0, (e - K) * Gw); h = lerp(w / G.thumbAspect, M, ue); s = lerp((w - vw) / 2, -q, ue);
      pn.label.style.transform = `translate3d(12px, ${h + 14}px, 0)`; pn.label.style.maxWidth = Math.max(0, w - 24) + 'px';
      pn.queue.style.opacity = String(1 - clamp(ce / .4));
    }
    pn.win.style.width = w + 'px'; pn.win.style.height = h + 'px';
    pn.media.style.transform = `translate3d(${s}px, 0, 0) scale(${J})`;
  });
}

/* ---------- Mobile stacked cards ---------- */
const ms = document.getElementById('mstack');
ms.innerHTML = P.map(p => `<article class="mcard">${p.video ? `<canvas class="scroll-film" aria-label="NIL opportunity film controlled by scrolling"></canvas><video src="${p.video}" poster="${p.img}" muted playsinline controls></video>` : `<img src="${p.img.replace('width=2000&height=1500', 'width=1000')}" alt="" loading="lazy">`}<div class="mc"><div class="ml">${p.l}</div><div class="mt">${p.m}</div><div class="md">${p.n}</div><a class="mb" href="${p.href}">${ARR}${p.m}</a></div></article>`).join('');

/* Primary film: scroll drives frames AND separated copy windows. */
const hero=document.getElementById('landing-film'), pin=hero.querySelector('.landing-pin'), can=hero.querySelector('canvas');
const beats=[...hero.querySelectorAll('.film-kicker,.film-line,.film-description,.film-action')];
const windows=[[.08,.14],[.17,.25],[.30,.39],[.44,.55],[.61,.72],[.80,.88]];
const frameCache=new Map();let lastRendered=-1,lastMode='';
function getFrame(i,mode){const key=mode+'/'+i;if(frameCache.has(key))return frameCache.get(key);const im=new Image();im.decoding='async';im.onerror=()=>{im.failed=true};im.src=`assets/film/${mode}/${String(i).padStart(3,'0')}.webp`;frameCache.set(key,im);if(frameCache.size>48)frameCache.delete(frameCache.keys().next().value);return im;}
function filmFrame(){
 const rect=hero.getBoundingClientRect(), p=clamp(-rect.top/Math.max(1,hero.offsetHeight-pin.offsetHeight));
 hero.dataset.progress=p.toFixed(4);
 beats.forEach((el,i)=>{const [a,b]=windows[i],t=filmReduced?1:clamp((p-a)/(b-a));el.style.opacity=t;el.style.transform=`translateY(${(1-t)*20}px)`;el.style.clipPath=`inset(${(1-t)*100}% 0 0 0)`;if(el.matches('a')){el.tabIndex=t===1?0:-1;el.style.pointerEvents=t===1?'auto':'none';}});
 hero.querySelector('.film-cue').style.opacity=filmReduced||p>.12?'0':'1';hero.querySelector('.film-progress').style.transform=`scaleX(${p})`;
 if(filmReduced)return;
 const mode=innerWidth/innerHeight<1?'mobile':'desktop',frame=Math.round(clamp(p/.9)*143);can.dataset.targetFrame=frame;
 const im=getFrame(frame,mode);[-2,-1,1,2,3,4].forEach(n=>getFrame(Math.max(0,Math.min(143,frame+n)),mode));
 if(im.failed){can.classList.remove('ready');return;}if(!im.complete||!im.naturalWidth)return;
 if(frame===lastRendered&&mode===lastMode&&can.classList.contains('ready'))return;
 can.width=im.naturalWidth;can.height=im.naturalHeight;can.getContext('2d').drawImage(im,0,0);can.classList.add('ready');can.dataset.frame=frame;lastRendered=frame;lastMode=mode;
}

const motionButton=document.createElement('button');motionButton.className='film-motion-choice';motionButton.textContent=filmReduced?'Enable full motion':'Reduce motion';motionButton.addEventListener('click',()=>{filmReduced=!filmReduced;try{localStorage.setItem('nil-film-static',String(filmReduced))}catch{}document.documentElement.classList.toggle('film-static',filmReduced);motionButton.textContent=filmReduced?'Enable full motion':'Reduce motion';location.reload();});document.querySelector('#mono-menu').appendChild(motionButton);

/* ---------- Manifesto ---------- */
const MAN = { track: innerWidth < 1200 ? 100 : 150, hold: .4, angle: 90, depth: 140, inertia: .1, jitter: .03, spread: .6, enter: 300, enterDur: 2, counterInset: 80 };
const STM = [{"label": "\u2014 THE ATHLETE", "text": "[[STUDENTS REPORT.]]\nTHE RECORD STARTS\nWITH THEIR STORY."}, {"label": "\u2014 THE GUARDIAN", "text": "[[PARENTS CONSENT.]]\nRECORDED. TIMESTAMPED.\n[[REVOCABLE.]]"}, {"label": "\u2014 THE INSTITUTION", "text": "[[SCHOOLS OBSERVE.]]\nA READ-ONLY VIEW.\n[[A DEFINED ROLE.]]"}];
const man = document.getElementById('manifesto'), block = man.querySelector('.m-block'), prog = man.querySelector('.m-progress'), idx = man.querySelector('.m-index'), skip = man.querySelector('.m-skip');
if(!reduced)man.style.height = STM.length * MAN.track + 'vh';
const chars = [], lineOf = [], boxes = [];
STM.forEach((st, si) => {
  chars[si] = []; lineOf[si] = []; boxes[si] = [];
  const el = document.createElement('div'); el.className = 'm-stmt' + (si ? ' abs' : '');
  let ci = 0;
  st.text.split('\n').forEach((line, li) => {
    const ln = document.createElement('span'); ln.className = 'm-line';
    const re = /\[\[([^\]]*)\]\]|([^\[]+)|(\[)/g; let m;
    while ((m = re.exec(line))) {
      const boxed = m[1] !== undefined, txt = boxed ? m[1] : (m[2] ?? m[3] ?? '');
      txt.split(/(\s+)/).forEach(word => {
        if (!word) return;
        const isSpace = /^\s+$/.test(word); const w = isSpace ? ' ' : word;
        const holder = document.createElement('span');
        if (boxed && !isSpace) { holder.className = 'm-box'; const bg = document.createElement('span'); bg.className = 'bg'; holder.appendChild(bg); }
        [...w].forEach(c => { const s = document.createElement('span'); s.className = 'm-ch'; s.textContent = c; holder.appendChild(s); chars[si][ci] = s; lineOf[si][ci] = li; ci++; });
        if (boxed && !isSpace) boxes[si].push({ el: holder, lastChar: ci - 1 });
        ln.appendChild(holder);
      });
    }
    el.appendChild(ln);
  });
  block.appendChild(el);
});
const nS = STM.length, segE = 1 / Math.max(1, nS - 1);
const segs = Array.from({ length: nS - 1 }, (_, n) => [n * segE + segE * MAN.hold * .5, (n + 1) * segE - segE * MAN.hold * .5]);
let maxLines = 1; lineOf.forEach(a => a.forEach(l => { if (l + 1 > maxLines) maxLines = l + 1; }));
const hash = (e) => e * 7919 % 104729 / 104729;
const Mr = (e) => 1 + 2.2 * (e - 1) ** 3 + 1.2 * (e - 1) ** 2, jr = (e) => e * e * e * (e * (e * 6 - 15) + 10), Nr = (e) => e * e * e;
const delayOf = (si, t) => clamp(lineOf[si][t] / Math.max(1, maxLines - 1) + (hash(t) - .5) * MAN.jitter);
const cache = new Map();
const setT = (el, tf, op) => { const k = tf + '|' + op; if (cache.get(el) !== k) { cache.set(el, k); el.style.transform = tf; el.style.opacity = op; } };
function stmtState(si, mode, x) {
  const sp = MAN.spread, loc = (t) => clamp((x - delayOf(si, t) * sp) / (1 - sp));
  chars[si].forEach((el, t) => {
    if (mode === 'shown') return setT(el, 'none', '1');
    if (mode === 'hidden') return setT(el, `rotateX(${MAN.angle}deg)`, '0');
    const s = loc(t);
    if (mode === 'out') { const r = clamp(s / .5), i = Nr(r); setT(el, `translate3d(0, ${i * .12}em, ${-i * MAN.depth}px) rotateX(${-i * MAN.angle}deg) scale(${1 - i * .08})`, String(1 - clamp((r - .2) / .5))); }
    else { const r = clamp((s - .5) / .5), i = Mr(r), a = jr(r); setT(el, `translate3d(0, ${(1 - a) * .14}em, ${-(1 - a) * MAN.depth}px) rotateX(${(1 - i) * MAN.angle}deg) scale(${.92 + a * .08})`, String(clamp(r / .45))); }
  });
  boxes[si].forEach(b => { let r = 0; if (mode === 'shown') r = 1; else if (mode === 'in') { const t = clamp((loc(b.lastChar) - .5) / .5); r = clamp((t - .6) / .4); } else if (mode === 'out') r = 1 - clamp(x / .2); b.el.style.setProperty('--sweep', r.toFixed(3)); });
}
let mSm = 0, mLast = 0, mPrevTop = NaN, mDir = 1, entered = null;
function manifestoFrame(ts) {
 if(reduced)return;
  const vh = innerHeight, rect = man.getBoundingClientRect(), d = Math.max(1, rect.height - vh), f = clamp(-rect.top / d);
  if (!Number.isNaN(mPrevTop) && Math.abs(rect.top - mPrevTop) > .5) mDir = rect.top < mPrevTop ? 1 : -1; mPrevTop = rect.top;
  const p = mLast ? Math.min((ts - mLast) / 1000, .1) : 1 / 60; mLast = ts;
  const k = 1 - Math.exp(-p * 60 * Math.log(1 / (1 - MAN.inertia)));
  mSm += (f - mSm) * k; if (Math.abs(f - mSm) < 5e-4) mSm = f;
  const h = mSm; let shown = 0, act = -1, x = 0;
  segs.forEach(([a, b], n) => { if (h >= b) shown = n + 1; else if (h >= a) { act = n; x = (h - a) / (b - a); } });
  for (let e = 0; e < nS; e++) { if (act >= 0) stmtState(e, e === act + 1 ? 'in' : e === act ? 'out' : 'hidden', x); else stmtState(e, e === shown ? 'shown' : 'hidden', 0); }
  prog.style.transform = `scaleX(${h.toFixed(4)})`;
  const br = block.getBoundingClientRect(), vis = rect.top < vh * .65 && rect.bottom > vh * .35, gone = rect.bottom <= 0 || rect.top >= vh;
  if (entered === null && vis) { block.style.transform='translate3d(0,0,0)';block.style.opacity='1';entered=true; }
  if (entered === null) { if (!vis) { block.style.transition = 'none'; block.style.transform = `translate3d(0, ${MAN.enter}px, 0)`; block.style.opacity = '0'; } entered = vis; }
  else if (vis && !entered) { block.style.transition = `transform ${MAN.enterDur}s cubic-bezier(0.16, 1, 0.3, 1), opacity ${MAN.enterDur * .8}s ease-out`; block.style.transform = 'translate3d(0,0,0)'; block.style.opacity = '1'; entered = true; }
  else if (gone && entered) { block.style.transition = 'none'; block.style.transform = `translate3d(0, ${MAN.enter}px, 0)`; block.style.opacity = '0'; entered = false; }
  const on = f > .01 && f < .99; skip.style.opacity = on ? '1' : '0'; skip.style.pointerEvents = on ? 'auto' : 'none';
  skip.querySelector('[data-arrow]').textContent = mDir === 1 ? 'Next' : 'Back';skip.setAttribute('aria-label',mDir===1?'Skip to the next section':'Back to the previous section');
  const li = act >= 0 ? (x >= .5 ? act + 1 : act) : shown; if (idx.textContent !== STM[li].label) idx.textContent = STM[li].label;
  idx.style.opacity = (.15 + .85 * (act >= 0 ? Math.abs(x - .5) * 2 : 1)).toFixed(3);
  idx.style.transform = `translate3d(${(h * rect.width - MAN.counterInset).toFixed(1)}px, 0, 0)`;
}
skip.addEventListener('click', () => { const r = man.getBoundingClientRect(), top = r.top + scrollY, to = mDir === 1 ? top + r.height - innerHeight : top; lenis ? lenis.scrollTo(to, { duration: 1.1 }) : scrollTo({ top: to, behavior: 'smooth' }); });

/* ---------- Loop ---------- */
measure(); addEventListener('resize', () => { measure(); panels.forEach(p => p._h = 0); }); addEventListener('load', measure);
function loop(ts) { cascadeFrame(); filmFrame(); manifestoFrame(ts); requestAnimationFrame(loop); }
requestAnimationFrame(loop);
setTimeout(measure, 300);
})();

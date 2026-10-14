from pathlib import Path
from bs4 import BeautifulSoup
import json
R=Path(__file__).resolve().parents[1];B=R/'production/record-exhibition/baseline'
names=['index','platform','data-and-consent','about','contact','privacy','terms','communications-consent','email-policy','transcript','404']
def frag(x):return BeautifulSoup(x,'html.parser')
def art(name,alt,cls=''):
 return f'<figure class="ex-art {cls}" data-ex-art><img src="assets/exhibition/{name}.webp" alt="{alt}" width="1086" height="1448" loading="lazy" decoding="async"></figure>'
def journey():
 return '''<section class="ex-journey" data-tone="dark" aria-labelledby="journey-title"><div class="ex-journey-heading"><p class="eyebrow">The record exhibition</p><h2 id="journey-title" data-ex-heading>Follow<br>one record.</h2><p>From disclosure to school visibility. Different responsibilities at every step.</p></div>'''+art('record','Blank paper sculpture under blue studio light','ex-record-art')+'''<div class="ex-roles"><article data-ex-role="0"><span class="eyebrow">Student reported</span><h3>Athlete disclosure</h3><p>The student-athlete reports NIL activity and academic eligibility information. The school does not create the record.</p></article><article data-ex-role="1"><span class="eyebrow">Consent before visibility</span><h3>Guardian consent</h3><p>For minors, a parent or guardian provides recorded, timestamped consent. Consent is reviewable and revocable.</p></article><article data-ex-role="2"><span class="eyebrow">A defined institutional role</span><h3>Read-only school view</h3><p>Authorized school users view relevant information. They do not edit student disclosures, approve deals, or manage the athlete’s opportunity.</p><a class="text-link" href="data-and-consent.html">Explore access boundaries</a></article></div></section>'''
for name in names:
 s=BeautifulSoup((B/(name+'.html')).read_text(),'html.parser');main=s.select_one('main')
 s.body['data-exhibition']='true'
 s.head.append(s.new_tag('link',rel='stylesheet',href='exhibition.css?v=ex1'))
 s.body.append(s.new_tag('script',src='exhibition.js?v=ex1',defer=''))
 header=s.select_one('.site-header');context=header.select_one('.header-context')
 nav=frag('<nav class="ex-top-nav" aria-label="Primary"><a href="platform.html">Platform</a><a href="data-and-consent.html">Data &amp; consent</a><a href="about.html">About</a><a href="contact.html">Request a demo</a></nav>')
 context.replace_with(nav)
 for a in header.select('nav a'):
  if a['href']==name+'.html':a['aria-current']='page'
 if name=='platform':
  s.select_one('.page-opening').replace_with(frag('''<section class="ex-opening" data-tone="light"><div class="ex-opening-copy"><p class="eyebrow">School compliance platform</p><h1>Opportunity.<br><span>Clearly<br>documented.</span></h1><p class="lead">Student-led disclosures.<br>Parent-consented access.<br>A defined school role.</p><a class="button" href="contact.html">Request a demo</a><p class="ex-footnote">Clarity supports opportunity</p></div>'''+art('frame','Silver exhibition frame displaying a blank paper record','ex-hero-art')+'</section>'))
  s.select_one('.platform-map').replace_with(frag(journey()))
  d=s.select_one('.capability-directory'); hs=list(d.select('h3')); d['class']=['ex-capability-index']
  for i,h in enumerate(hs):
   p=h.find_next_sibling('p');row=s.new_tag('article',attrs={'class':'ex-index-row'});h.insert_before(row);row.append(h.extract());row.append(p.extract());h['data-ex-heading']=''
 elif name=='index':
  intro=s.select_one('.record-intro');intro.replace_with(frag('''<section class="ex-home-intro" id="oversight" data-tone="light"><div><p class="eyebrow">NILKEEPR / School compliance</p><h2 data-ex-heading>Keep opportunity open.<br><span>Keep oversight clear.</span></h2><p>Disclosures, consent, and documentation, connected in one school-facing service. Without getting involved in the deal.</p><a class="button" href="platform.html">Explore the platform</a></div>'''+art('frame','Silver frame holding a blank record in a sunlit gallery')+'</section>'+journey()))
  # Replace illustrated HTML paper with generated material; existing feature controls retain their information.
  v=s.select_one('.lab-visual');v.insert_before(frag(art('record','Blank paper sculpture representing documentation','ex-tool-art')));v['hidden']=''
  access=s.select_one('.access-section');access.insert_before(frag('''<section class="ex-boundary-scene" data-tone="light">'''+art('consent','Blank paper sheets separated by a cobalt glass partition')+'''<div><p class="eyebrow">Data &amp; consent</p><h2 data-ex-heading>The right information.<br>Within clear boundaries.</h2><p>School visibility is limited to relevant oversight information. Consent and personal privacy stay part of the picture.</p><a class="text-link" href="data-and-consent.html">See what schools can view</a></div></section>'''))
 elif name=='data-and-consent':
  op=s.select_one('.page-opening');op['class']=['page-opening','ex-data-opening'];op.append(frag(art('consent','Cobalt glass boundary separating blank records')))
  op.select_one('h1')['data-ex-heading']=''
  # Keep practical access facts fully visible; animate only their headings.
 elif name=='about':
  op=s.select_one('.page-opening');op.select_one('img').decompose();op.append(frag(art('opportunity','Unbranded basketball and folded jersey on an exhibition plinth')));op['class']=['page-opening','about-opening','ex-about-opening']
  s.select_one('.about-mission').insert_after(frag('<div class="ex-about-detail">'+art('consent','A transparent cobalt boundary over blank paper')+'<p>Opportunity belongs to the athlete.<br>Oversight has its own role.</p></div>'))
 elif name=='contact':
  intro=s.select_one('.contact-intro');intro.append(frag(art('consent','Blank records and a translucent cobalt divider','ex-contact-art')))
 else:
  s.body['class']=s.body.get('class',[])+['ex-document']
  if name=='404':s.select_one('.page-opening').append(frag(art('frame','Silver frame with a blank page','ex-404-art')))
 for p in main.select('.reading-document > p'):
  if p.get_text(strip=True).isdigit() and p.find_next_sibling('h2'):
   p['class']=p.get('class',[])+['ex-section-number']
 for h in main.select('h2'):
  if not h.find_parent(class_='film-runway'):h['data-ex-heading']=''
 (R/(name+'.html')).write_text(str(s))
# Keep redirect aliases intact; they lead to updated canonical routes.
print('Built',len(names),'canonical routes. Film subtree preserved.')

from pathlib import Path
from bs4 import BeautifulSoup
import sys,json
R=Path(__file__).resolve().parents[1];B=R/'production/record-exhibition/baseline';out=R/'production/athletic-index'
names=['index','platform','data-and-consent','about','contact','privacy','terms','communications-consent','email-policy','transcript','404']
def html(x):return BeautifulSoup(x,'html.parser')
def image(name,alt,cls=''):
 return f'<figure class="ath-image {cls}" data-motion="image"><a href="assets/athletic/{name}.webp" target="_blank" aria-label="View full {alt.lower()}"><img src="assets/athletic/{name}.webp" alt="{alt}" loading="lazy" decoding="async"></a></figure>'
def opening():return '''<section class="ath-opening" data-tone="light" data-motion="opening"><img class="ath-court" src="assets/athletic/court-index.webp" alt="" fetchpriority="high"><div><p class="eyebrow">School compliance platform</p><h1>A clear view.<br>A defined role.</h1><p>Tools for schools to follow self-reported<br class="desktop-break"> NIL activity without managing the deal.</p><a class="text-link" href="contact.html">Request a school demo</a></div></section>'''
def index():return '''<section class="ath-index" data-tone="light" data-motion="index" aria-label="Platform overview">'''+''.join(f'<a class="ath-index-row" href="platform.html#capabilities" data-motion="row"><h2>{title}</h2><p>{copy}</p></a>' for title,copy in [('Disclosures','Track self-reported NIL activity in one place.'),('Consent records','Document parent or guardian consent.'),('Audit history','Follow timestamped disclosure and access history.'),('Report exports','Prepare documentation for institutional review.')])+'</section>'
def roles():return '''<section class="ath-role-track" data-tone="dark" data-motion="roles"><div class="ath-role-stage"><div class="ath-role-lines"><h2><span data-role-word="0">Students report.</span><span data-role-word="1">Parents consent.</span><span data-role-word="2">Schools observe.</span></h2></div><div class="ath-role-detail"><p class="eyebrow">Different access. Different roles.</p><article data-role-note="0"><h3>Start with the athlete.</h3><p>Student-athletes self-report NIL activity and academic eligibility information.</p></article><article data-role-note="1"><h3>Consent comes first.</h3><p>For minors, guardian consent is recorded, timestamped, and revocable.</p></article><article data-role-note="2"><h3>Keep oversight separate.</h3><p>Schools have a read-only view. They do not edit student disclosures or approve the athlete’s deal.</p></article></div><div class="ath-role-rule" aria-hidden="true"></div></div></section>'''
def docstory():return '<section class="ath-document-story" data-tone="light" data-motion="document">'+image('disclosure','Disclosure overview: student-reported information, NIL activity summary, reported eligibility, school and class year, consent status, disclosure history, read-only school access')+'''<div><p class="eyebrow">The information behind the record</p><h2>Context.<br>Consent.<br>Continuity.</h2><p>Disclosures are more useful when the school can understand where the information came from, the consent behind it, and its history.</p><a class="button" href="platform.html">Explore the school platform</a></div></section>'''
ledger={}
for name in names:
 s=BeautifulSoup((B/(name+'.html')).read_text(),'html.parser');main=s.select_one('main');main['data-tone']='light';s.body['data-design']='athletic-index'
 s.head.append(s.new_tag('link',rel='stylesheet',href='athletic.css?v=a2'));s.body.append(s.new_tag('script',src='athletic.js?v=a2',defer=''))
 h=s.select_one('.site-header');h.select_one('.header-context').replace_with(html('<nav class="ath-nav" aria-label="Primary"><a href="platform.html">Platform</a><a href="data-and-consent.html">Data &amp; consent</a><a href="about.html">About</a><a href="contact.html">Request a demo</a></nav>'))
 for a in h.select('nav a'):
  if a['href']==name+'.html':a['aria-current']='page'
 if name=='index':
  s.select_one('.record-intro').replace_with(html('<div id="oversight">'+index()+roles()+docstory()+'</div>'))
  v=s.select_one('.lab-visual');v['hidden']='';v.insert_before(html(image('audit','Oversight record: disclosure history, consent record, logged school access, incident documentation, compliance summary, report export','ath-tool-art')))
  s.select_one('.access-section').insert_before(html('<section class="ath-access-art" data-tone="light" data-motion="document"><div><p class="eyebrow">Visibility has limits</p><h2>The right view.<br>Not every detail.</h2><p>Read-only school access brings relevant information together. Private communications, financial accounts, and exact compensation remain outside that view.</p></div>'+image('access','Consent and access overview: recorded, timestamped and revocable guardian consent; school view versus kept-private information')+'</section>'))
 elif name=='platform':
  s.select_one('.page-opening').replace_with(html(opening()+index()));s.select_one('.platform-map').replace_with(html(roles()+docstory()))
  group=s.select_one('.capability-directory');group['class']=['ath-capability-directory']
  for h in list(group.select('h3')):
   p=h.find_next_sibling('p');row=s.new_tag('article',attrs={'class':'ath-capability-row','data-motion':'row'});h.insert_before(row);row.append(h.extract());row.append(p.extract())
 elif name=='data-and-consent':
  op=s.select_one('.page-opening');op['class']=['page-opening','ath-data-opening'];op.append(html(image('access','Consent and access: an illustrated guide to guardian consent and school visibility')));op.select_one('h1').string='A clear boundary. At every step.'
 elif name=='about':
  op=s.select_one('.page-opening');op.select_one('img')['src']='assets/athletic/court-index.webp';op.select_one('img')['alt']='Conceptual basketball court and silver sideline bench';op['class']=['page-opening','about-opening','ath-about-opening'];op.select_one('h1').string='Opportunity moves. Responsibility stays clear.'
  s.select_one('.about-mission').insert_after(html('<section class="ath-about-document" data-motion="document">'+image('disclosure','NILKEEPR disclosure overview with source-supported fields')+'<div><p class="eyebrow">For schools and districts</p><h2>Know the record.<br>Respect the role.</h2><p>The school service is built around student-led information and a defined institutional view. It supports oversight without managing the opportunity.</p><a class="text-link" href="platform.html">Read the school overview</a></div></section>'))
 elif name=='contact':
  s.select_one('.contact-intro').append(html(image('audit','Institutional oversight overview','ath-contact-art')))
 else:s.body['class']=s.body.get('class',[])+['ath-document-page']
 for title in main.select('h1,h2,h3'):
  if not title.find_parent(class_='film-runway'):title['class']=title.get('class',[])+['ath-title']
 # Group full reading passages into individually sequenced semantic chapters.
 for doc in s.select('.reading-document'):
  current=None
  for child in list(doc.children):
   if not getattr(child,'name',None):continue
   if child.name=='h2' or (child.name=='p' and child.get_text(strip=True).isdigit()):
    if child.name=='h2' and current is not None and len(current.find_all(recursive=False))==1 and current.select_one('.ath-number'):
     current.append(child.extract());continue
    if child.name=='p':child['class']=child.get('class',[])+['ath-number']
    current=s.new_tag('section',attrs={'class':'ath-reading-chapter','data-motion':'chapter'});child.insert_before(current)
   if current is not None:current.append(child.extract())
 for p in main.select('p'):
  if p.get_text(strip=True).isdigit() and p.find_next_sibling('h2'):p['class']=p.get('class',[])+['ath-number']
 for sec in main.select('section'):
  if sec.find_parent(class_='film-runway') or 'film-runway' in sec.get('class',[]):continue
  if not sec.has_attr('data-motion'):sec['data-motion']='section'
 for a in main.select('.scope-pair article,.license-options article,.audience-workbench article'):a['data-motion']='row'
 footer=s.select_one('.site-footer');footer['data-motion']='footer'
 for x in footer.select('.footer-directory > div'):x['data-motion']='footer-column'
 ledger[name]=[{'tag':x.name,'class':x.get('class',[]),'motion':x['data-motion']} for x in s.select('[data-motion]')]
 if '--fixture' in sys.argv:
  if name=='platform':
   s.head.insert(0,s.new_tag('base',href='/'));(out/'fixture.html').write_text(str(s))
 else:(R/(name+'.html')).write_text(str(s))
(out/'motion-coverage.json').write_text(json.dumps(ledger,indent=2))
print('Fixture prepared' if '--fixture' in sys.argv else 'Built 11 routes with assigned section motion')

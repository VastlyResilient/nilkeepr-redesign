from pathlib import Path
from bs4 import BeautifulSoup
import subprocess,html
R=Path(__file__).resolve().parents[1]
subprocess.run(['python3',str(R/'scripts/build-supporting.py')],check=True)
E=html.escape
links=[('platform.html','Platform'),('data-and-consent.html','Data & consent'),('about.html','About'),('contact.html','Contact')]
footer='''<footer class="site-footer record-footer" data-tone="dark"><a class="footer-brand" href="index.html"><img src="assets/logo.png" alt="NILKEEPR"></a><div class="footer-directory"><div><h2>For your institution</h2><a href="platform.html">School platform</a><a href="data-and-consent.html">Data & consent</a><a href="index.html#licensing">Licensing</a></div><div><h2>Start a conversation</h2><a href="mailto:schools@nilkeepr.net">schools@nilkeepr.net</a><a href="tel:+18774197715">1-877-419-7715</a><a href="contact.html">Contact the school team</a></div><div><h2>Already connected?</h2><a href="https://nilkeepr.net/institutional/signin">School account sign-in</a><a href="about.html">About NILKEEPR</a></div></div><div class="footer-legal"><span>© 2026 NILKEEPr inc.</span><a href="privacy.html">Privacy</a><a href="privacy.html#privacy-choices">Privacy choices</a><a href="terms.html">Terms</a><a href="communications-consent.html">Communications consent</a><a href="email-policy.html">Email policy</a></div><p class="art-credit">Film and editorial artwork are illustrative concepts, not NILKEEPR premises or product screens. Workflow diagrams explain the service; they are not product screenshots.</p></footer>'''
workflow='''<div class="workflow-board" aria-label="How disclosure reaches the school view"><div class="board-top"><span>THE DISCLOSURE PATH</span><span>Explanatory diagram</span></div><div class="path-tabs" role="group" aria-label="Explore the disclosure path"><button data-step="0" aria-pressed="true">Athlete disclosure</button><button data-step="1" aria-pressed="false">Guardian consent</button><button data-step="2" aria-pressed="false">School visibility</button></div><div class="record-stack"><div class="record-sheet"><span class="sheet-label">START WITH THE SOURCE</span><h3 id="path-title">The athlete tells<br>their story.</h3><p id="path-copy">Student-athletes self-report their NIL activity and academic eligibility information. The school does not create the record.</p><div class="record-fields"><span>NIL activity</span><span>Reported eligibility</span><span>Disclosure history</span></div></div><div class="sheet-edge"></div></div><div class="board-bottom"><span id="path-status">Student-reported information</span><i aria-hidden="true"></i></div></div>'''
roles=[('The athlete','Student-athletes self-submit NIL activity and reported academic eligibility information. The student remains the source of truth.'),('The parent','For minors, guardian consent is recorded, timestamped, and revocable. Parents can review what schools can access.'),('The school','Administrators view relevant information in a read-only capacity. They do not create, edit, or control student records.')]
# Home: preserve only approved film structure and authentic source video.
p=R/'index.html';s=BeautifulSoup(p.read_text(),'html.parser');film=s.select_one('.film-runway');film.select_one('h1').clear();film.select_one('h1').append(BeautifulSoup('<span data-start=".21" data-end=".34">Opportunity.</span><span data-start=".40" data-end=".55">On the record.</span>','html.parser'));film.select_one('.film-intro').string='A clearer view of NIL activity. A defined role for your school.'
caption=film.select_one('.film-caption');caption.attrs.pop('data-start',None);caption.attrs.pop('data-end',None)
for i,span in enumerate(caption.select('span')):
 span['data-start']=str([.82,.88,.93][i]);span['data-end']=str([.87,.92,.97][i])
explainer=s.select_one('#explainer');explainer.select_one('h2').clear();explainer.select_one('h2').append('The school workflow, explained.');explainer['class']=['explainer','section','record-explainer']
licensing=s.select_one('#licensing');licensing.select_one('h2').clear();licensing.select_one('h2').append('Built for your institution.');licensing.select_one('.eyebrow').string='LICENSING';
for e in licensing.select('h3'): e.string=e.get_text(' ',strip=True)
body=f'''{film}<section class="record-intro" id="oversight" data-tone="light"><div class="intro-ticket"><p class="eyebrow">NILKEEPR / SCHOOL COMPLIANCE</p><h2>Keep opportunity open.<br>Keep oversight clear.</h2><div class="intro-bottom"><p>Disclosures, consent, and documentation—connected in one school-facing service. Without getting involved in the deal.</p><a class="button" href="platform.html">Explore the platform</a></div></div><div class="path-story"><div class="path-copy"><span class="section-tag">HOW IT CONNECTS</span><h2>One record.<br>Three distinct roles.</h2><p>The information changes hands.<br>The responsibilities stay clear.</p><div class="role-passages">{''.join(f'<article data-path-section="{i}"><h3>{t}</h3><p>{c}</p></article>' for i,(t,c) in enumerate(roles))}</div></div>{workflow}</div></section>
<section class="capability-lab" id="tools" data-tone="dark"><div class="lab-heading"><p class="eyebrow">THE SCHOOL WORKSPACE</p><h2>From disclosure<br>to documentation.</h2><p>Choose a capability to see where it fits.</p></div><div class="lab-grid"><div class="tool-list">{''.join(f'<button class="tool-select" data-tool="{i}" aria-pressed="{str(i==0).lower()}"><span>{t}</span></button>' for i,t in enumerate(['Disclosure intake','Consent records','Academic visibility','Audit history','Incident documentation','Compliance summaries','Report exports']))}</div><article class="tool-detail"><div class="lab-visual" aria-hidden="true"><div class="lab-document"><span class="lab-doc-label">DISCLOSURE RECORD</span><b class="lab-doc-title">Activity.<br>Context.<br>History.</b><i></i><i></i><i></i><span class="lab-stamp">STUDENT REPORTED</span></div><div class="lab-destination">SCHOOL VIEW</div></div><span class="tool-number" hidden>01</span><h3 id="tool-title">Disclosure intake</h3><p id="tool-copy">Bring self-reported NIL activity into one centralized view.</p><a class="text-link" href="platform.html">Read the platform overview</a></article></div></section>
{explainer}
<section class="access-section" id="data" data-tone="dark"><div class="access-title"><span class="section-tag">ACCESS, WITH BOUNDARIES</span><h2>Useful visibility.<br>Not unrestricted access.</h2><a class="button white" href="data-and-consent.html">Understand data & consent</a></div><div class="access-console"><div class="privacy-controls" role="group" aria-label="Information visibility"><button data-scope="visible" aria-pressed="true">School view</button><button data-scope="private" aria-pressed="false">Excluded information</button></div><div class="privacy-view"><div><span class="scope-word">Visible.</span><p id="scope-description">Read-only information, provided by the athlete and supported by consent.</p></div><ul id="scope-list"><li>School name and class year</li><li>Reported academic eligibility status</li><li>NIL disclosure summaries, without exact dollar amounts</li><li>Active or expired consent status</li><li>Disclosure timestamps and audit history</li></ul></div></div></section>
<section class="boundary-banner" data-tone="light"><p class="section-tag">A DEFINED ROLE</p><h2>Observe. Document.<br><span>Stay independent of the deal.</span></h2><p>No deal negotiation, athlete valuation, NIL commissions, or recruiting influence. No replacement for the school’s SIS, gradebook, or eligibility authority.</p></section>{licensing}'''
s.select_one('main').clear();s.select_one('main').append(BeautifulSoup(body,'html.parser'));p.write_text(str(s))
# Page-specific main compositions retain substantive existing text.
for name in ['about','platform','data-and-consent','contact','transcript','privacy','terms','communications-consent','email-policy','404']:
 p=R/(name+'.html');s=BeautifulSoup(p.read_text(),'html.parser');main=s.select_one('main');main['class']=['route-'+name]
 if name=='platform':
  op=s.select_one('.page-opening');op.select_one('h1').string='The school’s view of NIL.';op.append(BeautifulSoup('<a class="button" href="contact.html">Request a walkthrough</a>','html.parser'))
  op.insert_after(BeautifulSoup('<section class="platform-map" data-tone="light"><div><span class="section-tag">INFORMATION, NOT INTERVENTION</span><h2>Follow the record.</h2><p>Explore the three roles behind institutional oversight.</p></div>'+workflow+'</section>','html.parser'))
  doc=s.select_one('.reading-document');h=doc.select_one('#capabilities');group=s.new_tag('div',attrs={'class':'capability-directory'});current=h.find_next_sibling()
  while current and current.name!='h2':
   nextel=current.find_next_sibling();group.append(current.extract());current=nextel
  h.insert_after(group)
 if name=='data-and-consent':
  op=s.select_one('.page-opening');op.select_one('h1').string='A boundary around every record.'
  op.insert_after(BeautifulSoup('''<section class="scope-pair" data-tone="light"><article><span class="section-tag">IN THE SCHOOL VIEW</span><h2>Oversight information.</h2><p>School and class year. Reported eligibility. Disclosure summaries. Consent status. Timestamped history.</p><span class="scope-seal">Read-only access</span></article><article><span class="section-tag">OUTSIDE THE SCHOOL VIEW</span><h2>Personal details.</h2><p>Full birth dates. Parent contact details. Private messages. Financial accounts. Exact compensation figures.</p><span class="scope-seal">Excluded information</span></article></section>''','html.parser'))
 if name=='about':
  op=s.select_one('.page-opening');op.select_one('h1').string='Different roles. A shared ecosystem.'
  image=s.select_one('.about-split img').extract();op.append(image);op['class']=['page-opening','about-opening']
  s.select_one('.about-split')['class']=['about-mission']
  audiences=s.select_one('.audience-list');audiences['class']=['audience-workbench'];articles=audiences.select('article');nav=s.new_tag('div',attrs={'class':'audience-tabs','role':'group','aria-label':'Explore NILKEEPR audiences'})
  for i,a in enumerate(articles):
   b=s.new_tag('button',attrs={'data-audience':str(i),'aria-pressed':str(i==0).lower()});b.string=a.h3.get_text();nav.append(b);a['data-audience-panel']=str(i)
  audiences.insert(0,nav)
 if name=='contact':
  s.select_one('h1').string='Let’s talk about your school.';s.select_one('.contact-intro .eyebrow').string='SCHOOL & DISTRICT INQUIRIES';s.select_one('.contact-panel h2').string='Your inquiry';s.select_one('.contact-panel')['class']=['contact-panel','inquiry-sheet']
 if name in ['privacy','terms','communications-consent','email-policy','transcript']:
  main['class'].append('document-route');s.select_one('.page-opening .eyebrow').string='NILKEEPR / DOCUMENT LIBRARY'
  if not s.select_one('.reading-nav'):
   doc=s.select_one('.reading-document');doc.wrap(s.new_tag('div',attrs={'class':'reading-layout'}))
  s.select_one('.reading-document')['id']='document-body'
 p.write_text(str(s))
# Shared identity, compact directory navigation and footer.
for name in ['index','about','platform','data-and-consent','contact','transcript','privacy','terms','communications-consent','email-policy','404']:
 p=R/(name+'.html');s=BeautifulSoup(p.read_text(),'html.parser');s.body['data-design']='record';s.body['data-route']=name
 if name=='404':
  dev=s.new_tag('script');dev.string="if(['localhost','127.0.0.1'].includes(location.hostname))document.querySelector('base').href='/';";s.head.find('base').insert_after(dev)
 s.head.append(s.new_tag('link',attrs={'rel':'stylesheet','href':'exclusive.css?v=record1'}))
 s.body.append(s.new_tag('script',attrs={'src':'exclusive.js?v=record1','defer':''}))
 header=s.select_one('.site-header')
 if name!='index':header['class'].append('on-light')
 label=s.new_tag('span',attrs={'class':'header-context'});label.string='SCHOOL COMPLIANCE';header.select_one('.brand').insert_after(label)
 menu=s.select_one('.menu-layout');menu.clear();menu.append(BeautifulSoup('''<div class="menu-directory"><p class="section-tag">NILKEEPR / DIRECTORY</p><nav aria-label="Main navigation"><a href="index.html">Overview</a>'''+''.join(f'<a href="{url}">{label}</a>' for url,label in links)+'''<a href="index.html#licensing">Institutional licensing</a></nav></div><aside><span class="section-tag">YOUR NEXT STEP</span><h2>See what fits<br>your institution.</h2><a class="button white" href="contact.html">Talk to the school team</a><a class="text-link" href="https://nilkeepr.net/institutional/signin">School account sign-in</a><button class="motion-choice" aria-pressed="false">Use a still introduction</button></aside>''','html.parser'))
 s.select_one('.site-footer').replace_with(BeautifulSoup(footer,'html.parser'))
 # Remove inherited colored emphasis / forced line breaks outside film, preserving actual text.
 for e in s.select('main em'):
  if not e.find_parent(class_='film-runway'): e.unwrap()
 s.select_one('title').string=s.select_one('title').get_text().replace('School compliance. Athlete opportunity.','School oversight, clearly connected')
 p.write_text(str(s))
print('Built unique record direction across 11 pages')

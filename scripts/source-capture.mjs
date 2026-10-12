import {chromium} from '../../klcc/node_modules/playwright/index.mjs';
import fs from 'node:fs/promises';
const browser=await chromium.launch({channel:'chrome',headless:true});
const page=await browser.newPage({viewport:{width:1440,height:900}});
for(const path of ['school-compliance','about','contact','school-admin/pricing','']) {
 await page.goto('https://nilkeepr.net/'+path,{waitUntil:'domcontentloaded'}); await page.waitForTimeout(1600);
 const key=path.replaceAll('/','-')||'home';
 const data=await page.evaluate(()=>({url:location.href,text:document.body.innerText,links:[...document.querySelectorAll('a[href]')].map(a=>({text:a.textContent,url:a.href})),images:[...document.images].map(a=>({src:a.currentSrc,alt:a.alt})),media:[...document.querySelectorAll('video,track')].map(a=>({src:a.currentSrc||a.src,poster:a.poster}))}));
 await fs.writeFile('research/'+key+'.json',JSON.stringify(data,null,2));
 await page.screenshot({path:'output/playwright/source-'+key+'.jpg',fullPage:true});
 console.log(key,data.text.length,data.images.length);
}
await browser.close();

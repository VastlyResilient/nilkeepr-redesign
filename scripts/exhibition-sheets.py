from PIL import Image,ImageOps,ImageDraw
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'production/record-exhibition/captures'
for route in ['index','platform','data-and-consent','about','contact','privacy','terms','communications-consent','email-policy','transcript','404']:
 files=[p/f'{route}-{device}-{state}.jpg' for device in ['mobile','tablet'] for state in ['opening','middle','footer']]
 sheet=Image.new('RGB',(1800,1040),'#dce1e8');d=ImageDraw.Draw(sheet)
 for i,f in enumerate(files):
  if not f.exists():continue
  im=Image.open(f);im.thumbnail((290,990));x=i*300+(300-im.width)//2;sheet.paste(im,(x,35));d.text((i*300+5,8),f.stem.replace(route+'-',''),fill='black')
 sheet.save(p/(route+'-sheet.jpg'),quality=86)

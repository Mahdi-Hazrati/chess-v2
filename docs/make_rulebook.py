import reportlab
from pathlib import Path
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
FONT_DIR=Path(reportlab.__file__).parent/'fonts'
pdfmetrics.registerFont(TTFont('Classic',str(FONT_DIR/'Vera.ttf')))
pdfmetrics.registerFont(TTFont('ClassicBold',str(FONT_DIR/'VeraBd.ttf')))
import json,math,os
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from xml.sax.saxutils import escape
PAGES=json.load(open('docs/rulebook.json'));W,H=595.28,841.89;OUT='dist/Chess-V2-Rulebook.pdf'
c=canvas.Canvas(OUT,pagesize=(W,H));c.setTitle('Chess V2 - Complete Rulebook and Player Guide');c.setAuthor('Mahdi Hazrati')
ink='#30342d';muted='#53676a';accent='#57664a'
def para(txt,x,y,width,size=10.2,lead=14,color=ink,bold=False):
 st=ParagraphStyle('p',fontName='ClassicBold' if bold else 'Classic',fontSize=size,leading=lead,textColor=HexColor(color),spaceAfter=0)
 p=Paragraph(escape(txt),st);_,h=p.wrap(width,1000);p.drawOn(c,x,y-h);return y-h

def frame(n):
 c.setFillColor(HexColor('#f5f4ee'));c.rect(0,0,W,H,fill=1,stroke=0)
 c.setStrokeColor(HexColor('#c7d3cb'));c.line(40,52,W-40,52)
 c.setFont('Classic',8);c.setFillColor(HexColor(muted));c.drawString(40,35,'CHESS V2    /    RULES EDITION 3');c.drawRightString(W-40,35,f'{n:02d}')
 c.setFont('ClassicBold',9);c.setFillColor(HexColor(accent));c.drawString(40,H-40,'FIELD MANUAL / COMPLETE PLAYER GUIDE')
def board():
 R=18;cx=W/2;cy=447
 for r in range(-6,7):
  for q in range(-6,7):
   if abs(q+r)>6:continue
   x=cx+math.sqrt(3)*R*(q+r/2);y=cy-1.5*R*r
   col='#e9e7dd' if (q-r)%3==0 else '#c9c8b8' if (q-r)%3==1 else '#a8ae98'
   if q==r==0:col='#548978'
   c.setFillColor(HexColor(col));c.setStrokeColor(HexColor('#f5f4ee'));p=c.beginPath()
   for i in range(6):
    a=math.radians(60*i-30);xx=x+(R-1)*math.cos(a);yy=y+(R-1)*math.sin(a)
    if i==0:p.moveTo(xx,yy)
    else:p.lineTo(xx,yy)
   p.close();c.drawPath(p,fill=1,stroke=1)
   if (q,r)==(0,0):c.setFillColor(HexColor('#ffffff'));c.setFont('ClassicBold',8);c.drawCentredString(x,y-3,'G7')
 for text,y in [('BLACK',cy+198),('WHITE',cy-208)]:c.setFillColor(HexColor(ink));c.setFont('ClassicBold',9);c.drawCentredString(cx,y,text)
frame(1);c.setFont('ClassicBold',38);c.setFillColor(HexColor(ink));c.drawString(40,739,'Chess V2')
para('Concept & game design: Mahdi Hazrati',40,716,510,12,19,muted)
para('127 hexes. 17 roles. One capturable king.',40,682,510,12,17,accent,True);board()
y=207
for h,t in [('WIN','Capture the opposing King. There is no checkmate.'),('CHOOSE','One main action each turn. A Bee may add one swarm step.'),('LEARN','Learn every rule, follow the interactive lessons, or print a real set.')]:
 y=para(h,40,y,58,9,12,accent,True);para(t,110,y+12,440,10.5,15);y-=35
c.showPage()
for num,page in enumerate(PAGES,2):
 frame(num);title=page['title'].replace(' / ','  |  ');y=para(title,40,779,515,21,27,ink,True);y=para(page['intro'],40,y-14,515,11,15,muted)-25
 sections=page['sections'];split=(len(sections)+1)//2;starts=[40,310];width=245
 for x,items in zip(starts,[sections[:split],sections[split:]]):
  yy=y
  for h,t in items:
   yy=para(h,x,yy,width,11,15,accent,True)-6
   yy=para(t,x,yy,width,10,14,ink)-19
  if yy<65:raise RuntimeError(f'Content overflow page {num}: {yy}')
 c.showPage()
c.save();print(OUT)

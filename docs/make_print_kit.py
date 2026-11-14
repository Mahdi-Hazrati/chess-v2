import reportlab
from pathlib import Path
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
FONT_DIR=Path(reportlab.__file__).parent/'fonts'
pdfmetrics.registerFont(TTFont('Classic',str(FONT_DIR/'Vera.ttf')))
pdfmetrics.registerFont(TTFont('ClassicBold',str(FONT_DIR/'VeraBd.ttf')))
import math,json
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor,black,white
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
W,H=210*mm,297*mm
c=canvas.Canvas('dist/Chess-V2-Print-and-Play.pdf',pagesize=(W,H));c.setTitle('Chess V2 - Print and Play Board, Tokens and Tracking Sheet');c.setAuthor('Mahdi Hazrati')
codes={'p':'P','n':'N','b':'B','r':'R','q':'Q','k':'K','e':'BE','h':'HV','v':'HN','m':'MI','t':'AN','u':'CO','w':'WA','a':'AR','c':'CH','s':'BA','l':'LA'}
names={'p':'Pawn','n':'Knight','b':'Bishop','r':'Rook','q':'Queen','k':'King','e':'Bee','h':'Hive','v':'Hornet','m':'Mimic','t':'Anchor','u':'Courier','w':'Warden','a':'Archbishop','c':'Chancellor','s':'Bastion','l':'Lancer'}
def txt(t,x,y,size=10,bold=False):c.setFillColor(black);c.setFont('ClassicBold' if bold else 'Classic',size);c.drawString(x,y,t)
def center(t,x,y,size=10):c.setFillColor(black);c.setFont('Classic',size);c.drawCentredString(x,y,t)
def board(cx,cy,R):
 for r in range(-6,7):
  for q in range(-6,7):
   if abs(q+r)>6:continue
   x=cx+math.sqrt(3)*R*(q+r/2);y=cy-1.5*R*r
   c.setFillColor(HexColor(['#f6f3e9','#deded1','#bdc3af'][(q-r)%3]));c.setStrokeColor(HexColor('#77796c'));c.setLineWidth(.35);p=c.beginPath()
   for i in range(6):
    a=math.radians(60*i-30);xx=x+R*math.cos(a);yy=y+R*math.sin(a)
    if i==0:p.moveTo(xx,yy)
    else:p.lineTo(xx,yy)
   p.close();c.drawPath(p,fill=1,stroke=1)
   center(chr(71+q)+str(r+7),x,y-R*.68,6)
   if q==r==0:
    c.setStrokeColor(HexColor('#72775f'));c.circle(x,y+1,R*.5,fill=0,stroke=1);center('N',x,y-3,11)
def scale(x,y):
 c.setStrokeColor(black);c.setLineWidth(.7);c.line(x,y,x+50*mm,y);c.line(x,y-3,x,y+3);c.line(x+50*mm,y-3,x+50*mm,y+3);txt('50 mm at 100% print scale',x,y-13,8)
def header(title,subtitle):txt('CHESS V2 / PRINT & PLAY',15*mm,H-17*mm,10,True);txt(title,15*mm,H-29*mm,19,True);txt(subtitle,15*mm,H-38*mm,9)
# A3 all-in-one option.
c.setPageSize((420*mm,297*mm));txt('CHESS V2 / ONE-SHEET A3 BOARD',12*mm,285*mm,10,True);txt('Print at 100%. White starts at the bottom. Alternatively, use the four A4 tiles that follow.',12*mm,279*mm,8)
board(210*mm,144*mm,12.7*mm);scale(12*mm,18*mm);center('BLACK',210*mm,274*mm,9);center('WHITE',210*mm,12*mm,9);c.showPage();c.setPageSize((W,H))
# Four A4 tiles: cut to 180 mm squares, assemble 360 x 360 mm.
for row,col,title in [(0,0,'Top left / 1 of 4'),(0,1,'Top right / 2 of 4'),(1,0,'Bottom left / 3 of 4'),(1,1,'Bottom right / 4 of 4')]:
 header(title,'A4 board tiles. Print at 100%, cut around the square, and join matching edges.')
 x=15*mm;y=65*mm;size=180*mm
 c.saveState();p=c.beginPath();p.rect(x,y,size,size);c.clipPath(p,stroke=0,fill=0)
 c.translate(x-col*size,y-(1-row)*size);board(180*mm,180*mm,15.8*mm);c.restoreState()
 c.setStrokeColor(black);c.setLineWidth(.6);c.rect(x,y,size,size)
 for xx,yy in [(x,y),(x+size,y),(x,y+size),(x+size,y+size)]:c.line(xx-3,yy,xx+3,yy);c.line(xx,yy-3,xx,yy+3)
 scale(15*mm,45*mm);txt('Assembly: 1  2   /   3  4. The center joins at Nexus G7.',15*mm,20*mm,9);c.showPage()
# One token sheet per army: base, fusion forms and write-in spares.
base=['p']*9+['n']*3+['b']*2+['r']*2+['q','k']+['e']*3+['m','t','u']
extras=['h','v','w','a','c','s','l']*2+['q']*2+['r']*2+['n']*2+[None]*12
for army in ['White','Black']:
 header(army+' pieces','Cut the circles. Use blank discs for extra promotions or fusion results.')
 for i,t in enumerate(base+extras):
  col=i%8;row=i//8;x=(24+23*col)*mm;y=(236-27*row)*mm
  c.setFillColor(white if army=='White' else HexColor('#262824'));c.setStrokeColor(black);c.setLineWidth(.6);c.circle(x,y,9*mm,fill=1,stroke=1)
  c.setFillColor(black if army=='White' else white);c.setFont('ClassicBold',12);c.drawCentredString(x,y-4,codes.get(t,''));center(names.get(t,'Write-in'),x,y-13*mm,6)
 txt('Keep fusion ingredients off-board and record them on the tracking sheet.',15*mm,19*mm,8);c.showPage()
header('Markers & trackers','Cut the markers, or use coins and small sticks of the same size.')
y=230*mm
for row,labels in enumerate([['W gate 1','W gate 2','B gate 1','B gate 2'],['W guard','B guard','W royal','B royal'],['White turn','Black turn','Swarm','Nexus']]):
 for i,t in enumerate(labels):
  x=(37+i*46)*mm;yy=y-row*30*mm;c.setFillColor(HexColor('#efefe7'));c.setStrokeColor(black);c.circle(x,yy,11*mm,fill=1,stroke=1);center(t,x,yy-3,8)
for i,t in enumerate(['White wall 1','White wall 2','Black wall 1','Black wall 2']):
 x=(18+i*46)*mm;yy=130*mm;c.setFillColor(white if i<2 else HexColor('#262824'));c.setStrokeColor(black);c.rect(x,yy,30*mm,4*mm,fill=1,stroke=1);txt(t,x,yy-12,8)
for row,army in enumerate(['White flux','Black flux']):
 y=(103-row*25)*mm;txt(army,15*mm,y+45,9,True)
 for i in range(9):c.setStrokeColor(black);c.rect((15+i*20)*mm,y-12,18*mm,18*mm);center(str(i),(24+i*20)*mm,y+5,11)
txt('Start flux at 3. Cap at 8. Captures/pass +1; Nexus Harvest +3.',15*mm,38*mm,9)
txt('Royal markers: turn over after use. Guard: target marker plus origin record.',15*mm,30*mm,8);c.showPage()
header('Setup & tracking sheet','White moves first. Each army starts with 3 flux and one available Royal Exchange.')
# Exact mirrored initial setup.
rows=[('Rook','B13, F13','H1, L1'),('Knight','C13, E13','I1, K1'),('King','D13','J1'),('Bishop','B12, F12','H2, L2'),('Queen','D12','J2'),('Pawn','C12, E12, G12; C11–G11','G2, I2, K2; G3–K3'),('Bee','C10, D10','J4, K4'),('Mimic','E10','I4'),('Anchor','F10','H4'),('Courier','G10','G4'),('Reserve','P, N, BE','P, N, BE')]
y=244*mm
for i,t in enumerate(['Role','White squares','Black squares']):txt(t,[15,57,130][i]*mm,y,9,True)
for role,w,b in rows:
 y-=8*mm
 for i,t in enumerate([role,w,b]):txt(t.replace('–','-'),[15,57,130][i]*mm,y,8)
 c.setStrokeColor(HexColor('#cccccc'));c.line(15*mm,y-3,195*mm,y-3)
y-=17*mm;txt('Fusion ID / role / current square / original ingredients',15*mm,y,10,True)
for i in range(4):y-=10*mm;c.line(15*mm,y,195*mm,y)
y-=17*mm;txt('Courier / current square / passenger',15*mm,y,10,True)
for i in range(2):y-=10*mm;c.line(15*mm,y,195*mm,y)
y-=15*mm;txt('Guard origin + target: White ____________  Black ____________',15*mm,y,9)
y-=10*mm;txt('Quiet turns: ______ / 100     Consecutive passes: ______ / 4',15*mm,y,9)
txt('Concept & design: Mahdi Hazrati. Rules: Chess-V2-Rulebook.pdf.',15*mm,16*mm,8);c.showPage();c.save();print('dist/Chess-V2-Print-and-Play.pdf')

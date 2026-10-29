from pathlib import Path
import math
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from pypdf import PdfReader
import pypdfium2 as pdfium

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'output' / 'canvas-design'
OUT.mkdir(parents=True, exist_ok=True)
PDF = OUT / 'road-damage-canvas-note.pdf'
PNG = OUT / 'road-damage-canvas-note.png'
FONTS = Path('C:/Users/rashm/.agents/skills/canvas-design/canvas-fonts')
for name, filename in [('Display','BricolageGrotesque-Bold.ttf'), ('Body','InstrumentSans-Regular.ttf'), ('Bold','InstrumentSans-Bold.ttf'), ('Mono','DMMono-Regular.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONTS/filename)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='Bold',italic='Body',boldItalic='Bold')
W,H=A4
INK='#172D37'; MUTED='#536771'; PAPER='#F8F7F1'; RULE='#D3DCD7'
A='#275DB1'; B='#087B70'; C='#AA6318'
c=canvas.Canvas(str(PDF), pagesize=A4)
c.setTitle('Road damage. New country. - Proposal v8 visual note')
c.setAuthor('Research proposal explainer')
TEXT_BOUNDS=[]

def rect(x,t,w,h,fill=None,stroke=None,r=0,lw=1):
    c.setLineWidth(lw)
    if fill:c.setFillColor(HexColor(fill))
    if stroke:c.setStrokeColor(HexColor(stroke))
    if r:c.roundRect(x,H-t-h,w,h,r,stroke=bool(stroke),fill=bool(fill))
    else:c.rect(x,H-t-h,w,h,stroke=bool(stroke),fill=bool(fill))

def line(x,t,x2,t2,color=RULE,lw=1,dash=None):
    c.setStrokeColor(HexColor(color));c.setLineWidth(lw)
    c.setDash(dash or [])
    c.line(x,H-t,x2,H-t2);c.setDash([])

def txt(x,t,s,size=10,font='Body',color=INK):
    width=pdfmetrics.stringWidth(s,font,size)
    assert x>=0 and x+width<=W+0.5,(s,x,width)
    TEXT_BOUNDS.append((s,x,t,width,size))
    c.setFillColor(HexColor(color));c.setFont(font,size)
    c.drawString(x,H-t-size*.83,s)

def para(x,t,w,s,size=9.6,color=INK,font='Body',lead=None):
    p=Paragraph(s,ParagraphStyle('p',fontName=font,fontSize=size,leading=lead or size*1.28,textColor=HexColor(color)))
    _,ph=p.wrap(w,600)
    assert t+ph<H-16
    p.drawOn(c,x,H-t-ph)
    return ph

def arrow(x,t,x2,t2,color=INK,lw=1.1):
    line(x,t,x2,t2,color,lw)
    angle=math.atan2(t2-t,x2-x)
    for a in [-.48,.48]:
        line(x2,t2,x2-4.5*math.cos(angle+a),t2-4.5*math.sin(angle+a),color,lw)

def circle(x,t,r,fill):
    c.setFillColor(HexColor(fill));c.circle(x,H-t,r,fill=1,stroke=0)

def path(points,color=INK,lw=1):
    for p,q in zip(points,points[1:]):line(*p,*q,color,lw)

def crack(x,t,w,h,color=INK,lw=1.3):
    path([(x+w*.45,t),(x+w*.57,t+h*.2),(x+w*.35,t+h*.42),(x+w*.54,t+h*.65),(x+w*.4,t+h)],color,lw)
    path([(x+w*.35,t+h*.42),(x+w*.08,t+h*.32)],color,lw*.7)
    path([(x+w*.54,t+h*.65),(x+w*.85,t+h*.53)],color,lw*.7)

def badge(x,t,letter,color):
    circle(x+12,t+12,12,color);txt(x+4.8,t+2.6,letter,20,'Display','#FFFFFF')

def road(x,t,w,h):
    rect(x,t,w,h,'#E5EAE4',r=8)
    p=c.beginPath();p.moveTo(x+w*.28,H-t-7);p.lineTo(x+w*.72,H-t-7);p.lineTo(x+w*.95,H-t-h+7);p.lineTo(x+w*.05,H-t-h+7);p.close()
    c.setFillColor(HexColor('#526971'));c.drawPath(p,fill=1,stroke=0)
    for j in range(4):line(x+w*.5,t+14+j*22,x+w*.5,t+25+j*22,'#F3F0DB',2)
    crack(x+w*.23,t+43,w*.18,h*.40,'#20353E',1.5)
    rect(x+w*.2,t+40,w*.24,h*.47,stroke='#98D6BC',lw=1.6)
    crack(x+w*.67,t+70,w*.15,h*.24,'#F9E3BC',1.3)
    for j in range(3):
        for k in range(3):rect(x+w*.63+k*10,t+66+j*10,9,9,'#E9B771' if (j,k) in [(1,1),(2,1)] else None,stroke='#C99F6B',lw=.5)
    txt(x+10,t+h-16,'BOXES + MISS WARNINGS',7.2,'Mono','#FFFFFF')

def train_fields(t,train,compare,measure,color):
    for i,(lab,val) in enumerate([('TRAINS',train),('CONTROL',compare),('MEASURE',measure)]):
        yy=t+i*14
        txt(271,yy,lab,6.9,'Mono',color)
        txt(326,yy-1,val,9,'Body',INK)

rect(0,0,W,H,PAPER)
txt(32,23,'RESEARCH, EXPLAINED  /  PROPOSAL V8',7.8,'Mono',MUTED)
txt(32,47,'Road damage.',34,'Display')
txt(32,82,'New country.',34,'Display')
para(33,128,290,'Can a model trained elsewhere detect<br/>small or thin road damage?',11.7,lead=15)
road(359,47,204,119)
line(32,177,563,177,INK,.8)

txt(32,189,'01 / THE SHARED TEST',7.8,'Mono',MUTED)
txt(32,207,'Different roads. Different cameras. Same task.',14,'Display')
steps=[(32,'TRAIN','3 source countries'),(215,'FREEZE','Model + settings'),(398,'TEST','1 unseen country')]
for x,label,detail in steps:
    rect(x,234,165,41,'#E9EDE6',r=5)
    txt(x+11,242,label,7.5,'Mono',MUTED)
    txt(x+11,254,detail,11,'Bold')
arrow(201,255,211,255,MUTED);arrow(384,255,394,255,MUTED)
txt(32,285,'Rotate the test country four times. No target-country data for training or tuning.',9,'Body')
txt(32,301,'RDD2022  /  Japan, India, United States, Czech Republic  /  YOLO11',7.9,'Mono',MUTED)
line(32,321,563,321,INK,.8)
txt(32,332,'02 / THREE SEPARATE RESEARCH QUESTIONS',7.8,'Mono',MUTED)

# Member A: same displacement, different short-side reference.
badge(32,355,'A',A)
txt(66,355,'Match thin boxes differently',17,'Display',A)
rect(32,390,217,76,'#EDF1F7',r=5)
crack(46,400,33,48)
rect(57,397,14,55,stroke=A,lw=1.3)
rect(64,401,14,55,stroke=C,lw=1.1)
line(57,461,71,461,A,.8)
line(57,458,57,464,A,.8);line(71,458,71,464,A,.8)
txt(87,399,'same offset',7.2,'Mono',MUTED)
arrow(87,413,77,413,C,.8)
rect(154,399,50,53,stroke=A,lw=1.3)
rect(161,403,50,53,stroke=C,lw=1.1)
crack(160,405,37,39)
txt(86,440,'thin vs wide',7.5,'Body',MUTED)
para(271,386,292,'Measure matching error relative to a box\'s <b>short side</b>. Change which predictions learn from it, and their weights.',9.5,lead=12)
train_fields(429,'Modified YOLO','Equally tuned plain NWD','Detection accuracy (mAP)',A)
txt(33,472,'Blue: label box   /   Amber: prediction',7.5,'Body',MUTED)
line(32,489,563,489)

# Member B: a real scale change, not a cropped view.
badge(32,502,'B',B)
txt(66,502,'Learn across image scales',17,'Display',B)
rect(32,538,217,79,'#EAF1EB',r=5)
rect(45,548,68,54,'#D2DED5',r=3)
crack(65,557,28,35)
rect(71,554,15,41,stroke=B,lw=1.1)
rect(186,561,34,27,'#D2DED5',r=2)
crack(196,565,14,18)
rect(199,564,7.5,20.5,stroke=B,lw=.8)
arrow(123,575,175,575,B);arrow(175,575,123,575,B)
txt(128,560,'agree',7.4,'Mono',B)
txt(52,605,'640 px',7.5,'Mono',MUTED);txt(183,594,'320 px',7.5,'Mono',MUTED)
para(271,534,292,'Use two scales of the same image. Add a training loss that encourages agreement on <b>visible small or thin damage</b>.',9.5,lead=12)
train_fields(577,'YOLO + consistency loss','Same loss on all eligible boxes','Recall + false positives',B)
txt(33,624,'Extra views during training; one view at test time.',7.5,'Body',MUTED)
line(32,641,563,641)

# Member C: frozen detector, two inputs to a trainable CNN, sparse centre targets.
badge(32,654,'C',C)
txt(66,654,'Warn about likely misses',17,'Display',C)
rect(32,689,217,73,'#F4EEE2',r=5)
txt(43,697,'YOLO: FROZEN',7.1,'Mono',MUTED)
rect(44,713,45,22,'#DBE1DC',r=3);txt(48,718,'features',7.2)
rect(44,741,45,13,'#DBE1DC',r=2);txt(48,743,'weak map',6.8)
rect(111,717,44,30,'#F4D5A4',stroke=C,r=3,lw=.8)
txt(122,722,'CNN',9.6,'Bold',C);txt(117,734,'train',7,'Body',C)
arrow(90,724,109,727,C,.8);arrow(90,747,109,737,C,.8)
arrow(157,732,174,732,C,.8)
gx,gt=181,702
for j in range(7):
    for k in range(7):
        rect(gx+k*7,gt+j*7,7,7,'#D29133' if (j,k) in [(1,4),(4,1),(5,5)] else '#FAF7EF',stroke='#C5C7BD',lw=.35)
txt(179,754,'40 x 40',7.2,'Mono',MUTED)
para(271,686,292,'Keep YOLO fixed. Train a small <b>CNN</b> on its internal features and weak detections to flag likely missed-box centres.',9.5,lead=12)
train_fields(729,'Separate CNN head','Learned weak-map-only head','Miss-location AUPRC',C)
txt(33,770,'A warning grid, not recovered cracks.',7.5,'Bold',C)

line(32,789,563,789,INK,.8)
txt(32,800,'3 SEEDS  /  MATCHED CONTROLS  /  ABLATIONS  /  SOURCE-ONLY TUNING',7.1,'Mono',MUTED)
txt(32,815,'All three train neural models. Improvements remain to be tested.',9.3,'Bold')
txt(32,830,'Based on proposal v8. Diagrams are schematic; no results are shown.',6.9,'Body',MUTED)
c.showPage();c.save()
reader=PdfReader(PDF)
assert len(reader.pages)==1
content=reader.pages[0].extract_text()
for must in ['Match thin boxes','Learn across image','Warn about likely','plain NWD','AUPRC']:
    assert must in content,must
doc=pdfium.PdfDocument(str(PDF))
doc[0].render(scale=2.5).to_pil().save(PNG)
print(PDF)
print(PNG)
print('PASS: one A4 page, required labels present, all text within horizontal page bounds.')

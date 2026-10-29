from pathlib import Path
import math

from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color, white
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from pypdf import PdfReader
import pypdfium2 as pdfium


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "output" / "pdf"
OUT.mkdir(parents=True, exist_ok=True)
PDF = OUT / "road-damage-research-explained.pdf"
PNG = OUT / "road-damage-research-explained.png"

for name, file in [("UI", "segoeui.ttf"), ("UI-Bold", "segoeuib.ttf")]:
    pdfmetrics.registerFont(TTFont(name, str(Path("C:/Windows/Fonts") / file)))

W, H = A4
INK = "#14283C"
MUTED = "#526476"
BLUE = "#1769AA"
TEAL = "#087F80"
ORANGE = "#C35A12"
PAPER = "#FAFCFE"
c = canvas.Canvas(str(PDF), pagesize=A4)
c.setTitle("Road damage across countries - Research explained")
c.setAuthor("Research project explainer")


def box(x, top, w, h, fill, stroke=None, r=10):
    c.setFillColor(HexColor(fill))
    c.setStrokeColor(HexColor(stroke or fill))
    c.setLineWidth(0.7)
    c.roundRect(x, H - top - h, w, h, r, fill=1, stroke=bool(stroke))


def text(x, top, s, size=10, color=INK, bold=False):
    c.setFillColor(HexColor(color))
    c.setFont("UI-Bold" if bold else "UI", size)
    c.drawString(x, H - top - size * 0.83, s)


def para(x, top, w, s, size=10, color=INK, bold=False, leading=None):
    p = Paragraph(s, ParagraphStyle(
        "p", fontName="UI-Bold" if bold else "UI", fontSize=size,
        leading=leading or size * 1.36, textColor=HexColor(color),
        spaceBefore=0, spaceAfter=0,
    ))
    _, ph = p.wrap(w, 600)
    p.drawOn(c, x, H - top - ph)
    return ph


def line(x1, t1, x2, t2, color="#B9C9D8", width=1):
    c.setStrokeColor(HexColor(color))
    c.setLineWidth(width)
    c.line(x1, H - t1, x2, H - t2)


def arrow(x1, t, x2, color=MUTED):
    line(x1, t, x2, t, color, 1.2)
    line(x2 - 4, t - 3, x2, t, color, 1.2)
    line(x2 - 4, t + 3, x2, t, color, 1.2)


def poly(points, fill, stroke=None, width=1):
    p = c.beginPath()
    p.moveTo(points[0][0], H - points[0][1])
    for x, t in points[1:]:
        p.lineTo(x, H - t)
    p.close()
    c.setFillColor(HexColor(fill))
    c.setStrokeColor(HexColor(stroke or fill))
    c.setLineWidth(width)
    c.drawPath(p, fill=1, stroke=bool(stroke))


def crack(x, top, w, h, color="#24394A", width=1.3):
    pts = [(x + w*.45, top), (x + w*.60, top+h*.18),
           (x + w*.36, top+h*.38), (x+w*.55, top+h*.57),
           (x+w*.42, top+h*.75), (x+w*.56, top+h)]
    for a, b in zip(pts, pts[1:]):
        line(*a, *b, color, width)
    line(x+w*.36, top+h*.38, x+w*.12, top+h*.31, color, width*.75)
    line(x+w*.55, top+h*.57, x+w*.82, top+h*.47, color, width*.75)


def road_scene(x, top, w, h):
    box(x, top, w, h, "#DCE8E4", r=9)
    poly([(x+w*.26, top+4), (x+w*.75, top+4),
          (x+w*.96, top+h-4), (x+w*.04, top+h-4)], "#687D8D")
    for j in range(3):
        t = top + 8 + j * (h - 14) / 3
        line(x+w*.50, t, x+w*.50, t+7, "#EAF1F5", 2)
    crack(x+w*.17, top+h*.43, w*.18, h*.38, "#152D40", 1.2)
    c.setStrokeColor(HexColor("#9DE4C5"))
    c.setLineWidth(1.1)
    c.roundRect(x+w*.16, H-(top+h*.84), w*.22, h*.45, 3, fill=0, stroke=1)
    crack(x+w*.67, top+h*.62, w*.12, h*.25, "#FFF2CA", 1.4)
    c.setFillColor(Color(1, .66, .27, alpha=.27))
    c.circle(x+w*.735, H-(top+h*.75), 10, fill=1, stroke=0)


def flag(x, top, country, w=18, h=12):
    box(x, top, w, h, "#FFFFFF", stroke="#D7E1E8", r=1)
    if country == "Japan":
        c.setFillColor(HexColor("#C52A43"))
        c.circle(x+w/2, H-(top+h/2), 3.2, fill=1, stroke=0)
    elif country == "India":
        box(x, top, w, h/3, "#E9933D", r=0)
        box(x, top+2*h/3, w, h/3, "#348853", r=0)
        c.setStrokeColor(HexColor("#273E72")); c.setLineWidth(.6)
        c.circle(x+w/2, H-(top+h/2), 1.5, fill=0, stroke=1)
    elif country == "US":
        for j in range(7):
            box(x, top+2*j*h/13, w, h/13, "#BF4354", r=0)
        box(x, top, w*.45, h*7/13, "#294575", r=0)
    else:
        box(x, top+h/2, w, h/2, "#C8404B", r=0)
        poly([(x, top), (x+w*.48, top+h/2), (x, top+h)], "#2C5F93")


def icon_a(x, top, w, h):
    box(x, top, w, h, "#EAF3FB", r=7)
    box(x+36, top+9, 67, 43, "#D9E7F1", r=4)
    crack(x+59, top+13, 13, 34, "#31495B", 1.25)
    c.setStrokeColor(HexColor(BLUE)); c.setLineWidth(1)
    c.rect(x+61, H-(top+49), 11, 38, fill=0, stroke=1)
    for i in range(5):
        for j in range(3):
            selected = j == 1 and i in (1, 2, 3)
            c.setFillColor(HexColor(BLUE if selected else "#AEC4D8"))
            c.circle(x+49+j*18, H-(top+14+i*8), 2.2 if selected else 1.6, fill=1, stroke=0)
    text(x+13, top+59, "Which examples teach the model?", 8.2, BLUE)


def icon_b(x, top, w, h):
    box(x, top, w, h, "#E8F5F2", r=7)
    box(x+13, top+9, 54, 42, "#D2E6E0", r=4)
    crack(x+27, top+13, 18, 31, "#31534D", 1.3)
    c.setStrokeColor(HexColor(TEAL)); c.setLineWidth(.9)
    c.rect(x+31, H-(top+47), 14, 36, fill=0, stroke=1)
    box(x+93, top+20, 35, 28, "#D2E6E0", r=3)
    crack(x+102, top+23, 12, 20, "#31534D", 1)
    c.setStrokeColor(HexColor(TEAL))
    c.rect(x+105, H-(top+44), 9, 22, fill=0, stroke=1)
    arrow(x+73, top+32, x+87, TEAL)
    text(x+20, top+55, "Full view", 8.2, TEAL)
    text(x+91, top+55, "Small view", 8.2, TEAL)


def icon_c(x, top, w, h):
    box(x, top, w, h, "#FFF1E5", r=7)
    gx, gt, cell = x+38, top+8, 7.1
    for i in range(6):
        for j in range(9):
            d = math.hypot((j-5)*.85, i-3)
            fill = "#EDA45D" if d < 1.1 else "#F8CD9C" if d < 2 else "#FCE5CC"
            box(gx+j*cell, gt+i*cell, cell-0.7, cell-0.7, fill, r=.5)
    crack(gx+cell*4.9, gt+cell*1.5, 6.5, 25, "#7D3E17", 1)
    text(x+17, top+58, "Likely miss - not a new box", 8.3, ORANGE)


def member_card(x, top, w, letter, accent, tint, title, icon, body, model, compare, measure):
    height = 320
    box(x, top, w, height, "#FFFFFF", stroke="#DCE5ED", r=12)
    box(x, top, w, 7, accent, r=3)
    box(x+13, top+18, 25, 25, accent, r=7)
    text(x+20, top+22, letter, 17, "#FFFFFF", True)
    text(x+45, top+23, "MEMBER " + letter, 9.1, accent, True)
    para(x+13, top+55, w-26, title, 14.2, INK, True, 17)
    icon(x+12, top+99, w-24, 76)
    para(x+13, top+186, w-26, body, 9.6, INK, leading=13)
    text(x+13, top+245, model, 8.5, accent, True)
    para(x+13, top+266, w-26, "<b>Compare:</b> " + compare, 8.7, MUTED, leading=11.6)
    para(x+13, top+height+9, w-26, measure, 8.6, MUTED, leading=11.4)


box(0, 0, W, H, PAPER, r=0)
text(28, 22, "FINAL-YEAR RESEARCH  /  THE IDEA AT A GLANCE", 8.6, BLUE, True)
text(28, 43, "Road damage across countries", 25.2, INK, True)
text(29, 78, "Find more damage. Flag where the detector may have missed it.", 11.1, MUTED)
text(29, 94, "YOLO = the AI detector that draws boxes around damage.", 8.2, MUTED)

box(28, 105, W-56, 91, "#EAF1F7", r=12)
text(43, 118, "THE PROBLEM", 8.5, BLUE, True)
para(43, 136, 315,
     "Roads, cameras and lighting change between countries. "
     "An AI detector trained elsewhere may miss small or thin damage.",
     11.5, INK, leading=15.4)
road_scene(W-183, 116, 139, 68)

text(28, 214, "THE FAIR TEST", 9.4, INK, True)
test_top = 235
test_w = 162
for x, label, sub in [(28, "TRAIN ON 3 COUNTRIES", "Learn only from source data"),
                       (216, "FREEZE THE MODELS", "No tuning on the test country"),
                       (404, "TEST ON THE 4TH", "Measure unseen-country results")]:
    box(x, test_top, test_w, 47, "#FFFFFF", stroke="#DCE5ED", r=8)
    text(x+10, test_top+10, label, 8.7, BLUE, True)
    text(x+10, test_top+28, sub, 8.1, MUTED)
arrow(195, test_top+23, 210, BLUE)
arrow(383, test_top+23, 398, BLUE)

text(29, 293, "Rotate the test country:", 8.8, MUTED)
fx = 157
for country, advance in [("Japan", 70), ("India", 67), ("US", 54), ("Czech Republic", 100)]:
    flag(fx, 292, country)
    text(fx+24, 293, country, 8.5, INK)
    fx += advance

text(28, 326, "THREE IDEAS THE TEAM WILL TEST", 10, INK, True)
card_top, card_w, gap = 348, (W-56-20)/3, 10
member_card(28, card_top, card_w, "A", BLUE, "#EAF3FB",
            "Learn from\nthin boxes".replace("\n", "<br/>"), icon_a,
            "Changes how YOLO chooses and weights training examples for thin damage.",
            "DEEP LEARNING: retrains YOLO",
            "An existing assignment rule (plain NWD), tuned equally.",
            "MEASURE: detection accuracy, especially on small/thin boxes.")
member_card(28+card_w+gap, card_top, card_w, "B", TEAL, "#E8F5F2",
            "Compare two<br/>image scales", icon_b,
            "Trains YOLO to make consistent predictions from a full-size and smaller view.",
            "DEEP LEARNING: trains YOLO",
            "Consistency for small/thin damage vs all damage; random-subset check.",
            "MEASURE: how much small/thin damage is found, and false alarms.")
member_card(28+2*(card_w+gap), card_top, card_w, "C", ORANGE, "#FFF1E5",
            "Predict likely<br/>miss locations", icon_c,
            "Uses YOLO's visual features to train a small neural network. YOLO stays unchanged.",
            "DEEP LEARNING: trains a neural head",
            "Visual features + weak guesses vs a model using weak guesses alone.",
            "MEASURE: how well warnings identify locations with missed damage.")

box(28, 715, W-56, 53, "#14283C", r=10)
text(42, 726, "ONE BASELINE. THREE SEPARATELY TESTED CONTRIBUTIONS.", 10, "#FFFFFF", True)
text(42, 746, "A and B aim to improve detection. C aims to reveal likely misses.", 10.2, "#DBE8F2")

labels = [("PUBLIC DATA", "RDD2022; existing labels"),
          ("REPEAT RUNS", "3 seeds for main tests"),
          ("FAIR CONTROLS", "Baselines + ablations")]
for j, (label, desc) in enumerate(labels):
    x = 29+j*184
    text(x, 782, label, 8.3, BLUE, True)
    text(x, 796, desc, 8.3, MUTED)

text(29, 812, "These are proposed methods: improvements must be demonstrated, not assumed.", 7.9, MUTED)
text(29, 825, "Based on proposal v8. Dataset: Arya et al., RDD2022 (2024), DOI 10.1002/gdj3.260.", 7, MUTED)
c.linkURL("https://doi.org/10.1002/gdj3.260", (28, H-833, W-28, H-822), relative=0)
c.showPage()
c.save()

reader = PdfReader(str(PDF))
assert len(reader.pages) == 1
page_text = reader.pages[0].extract_text()
for required in ["MEMBER A", "MEMBER B", "MEMBER C", "TRAIN ON 3 COUNTRIES", "proposed methods"]:
    assert required in page_text, required
doc = pdfium.PdfDocument(str(PDF))
doc[0].render(scale=2.7).to_pil().save(PNG)
print(f"PDF: {PDF}")
print(f"PNG: {PNG}")
print(f"Verified pages: {len(reader.pages)}")

from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import black, HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from pypdf import PdfReader
import pypdfium2 as pdfium

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'output'/'pdf'; OUT.mkdir(parents=True,exist_ok=True)
PDF=OUT/'road-damage-research-summary.pdf'
QA=ROOT/'tmp'/'pdfs'/'academic-report-preview';QA.mkdir(parents=True,exist_ok=True)
for name,file in [('Academic','times.ttf'),('Academic-Bold','timesbd.ttf'),('Academic-Italic','timesi.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(Path('C:/Windows/Fonts')/file)))
pdfmetrics.registerFontFamily('Academic',normal='Academic',bold='Academic-Bold',italic='Academic-Italic',boldItalic='Academic-Bold')
styles={
 'title':ParagraphStyle('title',fontName='Academic-Bold',fontSize=17,leading=20,alignment=TA_CENTER,spaceAfter=9),
 'subtitle':ParagraphStyle('subtitle',fontName='Academic',fontSize=10.5,leading=13,alignment=TA_CENTER,spaceAfter=15),
 'heading':ParagraphStyle('heading',fontName='Academic-Bold',fontSize=13,leading=16,spaceBefore=10,spaceAfter=7,keepWithNext=True),
 'sub':ParagraphStyle('sub',fontName='Academic-Bold',fontSize=11.3,leading=14,spaceBefore=9,spaceAfter=5,keepWithNext=True),
 'body':ParagraphStyle('body',fontName='Academic',fontSize=11.3,leading=14.8,alignment=TA_JUSTIFY,spaceAfter=8),
 'note':ParagraphStyle('note',fontName='Academic-Italic',fontSize=9.6,leading=12.4,spaceAfter=9),
 'ref':ParagraphStyle('ref',fontName='Academic',fontSize=9.8,leading=12.5,spaceAfter=7,leftIndent=18,firstLineIndent=-18),
}
story=[]
def p(text,kind='body'):story.append(Paragraph(text,styles[kind]))
def h(text):p(text,'heading')
def sub(text):p(text,'sub')
def page():story.append(PageBreak())
def link(url,label):return f'<link href="{url}" color="#111111"><u>{label}</u></link>'

p('Small Road-Damage Detection That Transfers<br/>to Unseen Countries','title')
h('1. Problem and Motivation')
p('Road-damage detection uses computer vision to locate and classify defects such as longitudinal cracks, transverse cracks, alligator cracks and potholes. A detector trained on images from one country may perform poorly in another because road materials, cameras, viewpoints, lighting and damage appearance differ. Published road-damage domain-generalisation work explicitly addresses this problem [2].')
p('Small or thin damage creates an additional difficulty: a slight displacement of a predicted box can substantially change its overlap with a narrow label box. Tiny-object research motivates alternatives to overlap-based matching [4]. However, the claim that small or thin damage always suffers the largest country-transfer loss remains a hypothesis to measure in this project.')
p('Missed damage also creates a reliability problem. A crack that receives no accepted detection box has no displayed confidence score. The project therefore investigates both detection performance and a separate warning model that estimates where the detector may have missed small or thin damage. A warning is not a recovered detection or a guarantee of correctness.')
h('2. Research Aim and Shared Setting')
p('The aim is to determine whether geometry-aware matching and small-object-focused consistency improve detection on an unseen country, and whether a source-trained neural model can predict the locations of missed small or thin damage. Each member addresses a separate question using a shared detector and evaluation protocol.')
p('The planned dataset is the public RDD2022 release [1]. The core study uses labelled images from Japan, India, the United States and the Czech Republic, with four damage classes. Official unlabelled test images are excluded from scored evaluation. No new photographs, questionnaires or user studies are required.')
p('The shared baseline is a COCO-initialised YOLO11 model at 640-pixel input resolution. In each of four folds, three countries provide source data and the fourth is reserved for final evaluation. Training, hyperparameter selection and threshold selection use only the source countries. This is source-only domain generalisation; even unlabelled target-country images are unavailable during development.')

page()
h('3. Proposed Solution and Individual Contributions')
p('The three methods are evaluated independently before any optional combination. Their effectiveness is not assumed. Each study has a principal comparator so that improvements can be attributed to the proposed change rather than to extra tuning or computation.')
sub('3.1 Member A: Short-Side-Relative Assignment and Weighting')
p('Member A changes how YOLO matches training predictions to labelled boxes and assigns supervision weights. The method represents boxes using a Gaussian distance, following the general NWD approach [4], but normalises the distance by the labelled box\'s short side rather than a single dataset-wide constant. The same displacement therefore has a different significance for a thin box and a wide box.')
p('This rule is stricter for thin boxes in pixel terms; it must not be described as automatically more tolerant. A trains the modified detector and compares it with plain NWD under identical candidate eligibility and equal source-only tuning. Primary evaluation uses mAP50:95 on unchanged held-out labels. Assignment counts, boxes receiving no positive predictions and total supervision weight are analysed to explain the mechanism. Simulated annotation-noise experiments are optional extensions.')
sub('3.2 Member B: Small-Object-Anchored Scale Consistency')
p('Member B adds a consistency objective during detector training. A student model receives the normal supervised full-size image and an additional half-size view. An exponential-moving-average teacher receives the full-size image without gradients. The added loss encourages corresponding predictions to agree in class scores and box locations for eligible small or thin labelled objects.')
p('The principal comparison is against the same consistency objective applied to all eligible objects, with identical views and training budget. A count-matched random subset is a secondary control. Extremely thin boxes that become too small in the reduced view are excluded and their exclusion rate is reported. B measures small-or-thin recall together with precision and false positives; increased recall alone is insufficient evidence of success.')
sub('3.3 Member C: Neural Prediction of Missed Damage')
p('Member C keeps the detector frozen and trains a separate small convolutional neural network (CNN). It uses internal detector features and a map of low-confidence detections to predict a 40 by 40 warning grid. A positive training cell contains the centre of a labelled small-or-thin object that the detector failed to match at its frozen operating threshold.')
p('The principal comparator is a matched learned CNN using only the weak-detection map. This tests whether internal features add information beyond low-confidence detections. Training and selection use source images excluded from detector fitting, and cell-level area under the precision-recall curve (AUPRC) is evaluated on the held-out country. C predicts likely missed-object centres, not crack boundaries or recovered boxes. It remains a deep-learning contribution despite requiring much less GPU time than detector retraining.')

page()
h('4. Brief Literature Review')
p('The following review is selective. Paper identities and the stated high-level methods were checked against primary-source records, abstracts or accessible publisher previews on 30 October 2026. It is not a systematic review or a claim that all relevant work has been excluded. Unresolved references from earlier drafts are not relied upon here.','note')
sub('4.1 Multi-Country Data and Source-Only Generalisation')
p('Arya et al. introduced RDD2022, a multi-national dataset supporting road-damage detection across six countries [1]. It provides a common public resource for this project, but a dataset does not establish that a particular intervention will transfer. Chen et al.\'s MAMDG explicitly studies road-damage domain generalisation without target data, using multi-adversarial feature learning and a triplet-based metric constraint [2]. Consequently, source-only cross-country detection is established prior work; the four-country protocol is a testbed rather than the novelty claim.')
sub('4.2 Adaptation Using Target Images')
p('Xiao et al.\'s PROBE derives defect-aware visual prompts from unlabelled target data and aligns source and target representations [3]. Its target-data requirement distinguishes it from this proposal. It supports the relevance of cross-domain road inspection, but adaptation results must not be presented as directly comparable source-only results unless the data-access rules are matched.')
sub('4.3 Box Geometry and Tiny Objects')
p('Wang et al. model bounding boxes as Gaussian distributions and introduce Normalized Wasserstein Distance to reduce the sensitivity of tiny-object matching to positional deviations [4]. Therefore, using NWD or Gaussian boxes alone is not a new contribution. A\'s narrower question concerns short-side-relative normalisation, its effects on assignment and weighting, and its performance on unseen road-damage countries compared with equally tuned plain NWD.')
sub('4.4 Consistency and Generalised Detection')
p('Danish et al. combine source-domain diversification with alignment of classification and localisation outputs across views for single-domain-generalised detection [5]. This means source-only cross-view agreement is established. B must demonstrate the value of selecting small or thin objects for the consistency objective, using generic and count-matched controls, rather than claiming that multi-view consistency itself is novel.')
sub('4.5 Predicting Detector Failures')
p('Rahman et al. train a separate false-negative alarm model from traffic-sign detector features [6]. More recently, KGFP compares internal detector representations with foundation-model representations to flag likely missed safety-critical objects [7]. C therefore builds on an established failure-prediction idea. Its proposed distinction is a dense missed-centre target for small or thin road damage under held-out-country evaluation, with a learned weak-map-only comparator.')
p('The defensible contribution is three controlled, application-specific studies with distinct questions. Their originality remains bounded by the literature examined and must be reassessed if closely matching work is identified.')

page()
h('5. Evaluation, Feasibility and Expected Outcome')
p('Exact and near-duplicate groups must remain within one split. Each outer fold uses source-only inner validation, and held-out results are opened only after the methods and analysis rules are frozen. Principal contrasts use three training seeds. Report per-country, country-macro and worst-country outcomes, paired bootstrap intervals with images or duplicate groups as sampling units, and seed variation separately. C\'s grid cells must not be treated as independent bootstrap observations.')
p('The research workload consists of model design, training, matched controls, ablations and interpretation. Shared infrastructure and the demonstration interface do not count as individual research contributions. Feasibility is conditional on early runtime measurements and reliable GPU access. Prioritise the principal contrasts; retain annotation noise and the combined AB detector as optional extensions. Four countries cannot justify claims about all countries, and box geometry does not measure physical crack width or severity.')
p('Expected outputs are three evaluated methods, reproducible splits and scripts, and a documented account of when each method helps or fails. No performance gain, deployment readiness, cost saving or road-safety benefit is claimed before evidence is available.')
h('References')
refs=[
('[1]', 'Arya, D., Maeda, H., Ghosh, S. K., Toshniwal, D., and Sekimoto, Y. (2024). RDD2022: A multi-national image dataset for automatic road damage detection. <i>Geoscience Data Journal</i>, 11, 846-862. ', 'https://doi.org/10.1002/gdj3.260','doi:10.1002/gdj3.260'),
('[2]', 'Chen, Z., et al. (2026). Multi-Adversarial Metric-Constrained Domain Generalization for road damage detection. <i>Image and Vision Computing</i>. ', 'https://doi.org/10.1016/j.imavis.2026.106173','doi:10.1016/j.imavis.2026.106173'),
('[3]', 'Xiao, X., et al. (2026). Self-Supervised Visual Prompting for Cross-Domain Road Damage Detection. <i>WACV</i>; preprint posted 2025. ', 'https://arxiv.org/abs/2511.12410','arXiv:2511.12410'),
('[4]', 'Wang, J., Xu, C., Yang, W., and Yu, L. (2021). A Normalized Gaussian Wasserstein Distance for Tiny Object Detection. <i>arXiv preprint</i> (revised 2022). ', 'https://arxiv.org/abs/2110.13389','arXiv:2110.13389'),
('[5]', 'Danish, M. S., et al. (2024). Improving Single Domain-Generalized Object Detection: A Focus on Diversification and Alignment. <i>CVPR</i>. ', 'https://openaccess.thecvf.com/content/CVPR2024/papers/Danish_Improving_Single_Domain-Generalized_Object_Detection_A_Focus_on_Diversification_and_CVPR_2024_paper.pdf','CVF open-access paper'),
('[6]', 'Rahman, Q. M., Sunderhauf, N., and Dayoub, F. (2019). Did You Miss the Sign? A False Negative Alarm System for Traffic Sign Detectors. <i>IROS</i>. ', 'https://doi.org/10.1109/IROS40897.2019.8968525','doi:10.1109/IROS40897.2019.8968525'),
('[7]', 'Zimmermann, J., Holzbach, G., and Lerch, D. (2026). Knowledge-Guided Failure Prediction: Detecting When Object Detectors Miss Safety-Critical Objects. <i>CVPR Workshops</i>, 4312-4321. ', 'https://arxiv.org/abs/2603.25499','arXiv:2603.25499'),
]
for num,desc,url,label in refs:p(num+' '+desc+link(url,label)+'.','ref')

class NumberedCanvas(canvas.Canvas):
    def __init__(self,*a,**kw):super().__init__(*a,**kw);self.states=[]
    def showPage(self):self.states.append(dict(self.__dict__));self._startPage()
    def save(self):
        n=len(self.states)
        for state in self.states:
            self.__dict__.update(state)
            self.setFillColor(HexColor('#444444'));self.setFont('Academic',8.5)
            self.drawString(56,A4[1]-32,'Cross-Country Road-Damage Detection | Research Summary')
            self.drawRightString(A4[0]-56,30,f'{self._pageNumber} / {n}')
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

doc=SimpleDocTemplate(str(PDF),pagesize=A4,leftMargin=56,rightMargin=56,topMargin=51,bottomMargin=49,title='Small Road-Damage Detection That Transfers to Unseen Countries',author='Research proposal summary')
doc.build(story,canvasmaker=NumberedCanvas)
r=PdfReader(PDF)
print('Pages:',len(r.pages))
for i,pag in enumerate(r.pages):print('Page',i+1,'words:',len(pag.extract_text().split()))
assert len(r.pages)==4, 'Unexpected pagination; inspect and adjust.'
full='\n'.join(x.extract_text() for x in r.pages)
for required in ['Problem and Motivation','Proposed Solution','Brief Literature Review','References','40 by 40','AUPRC']:assert required in full,required
assert sum(len(pag.get('/Annots',[])) for pag in r.pages)>=7
render=pdfium.PdfDocument(str(PDF))
for i in range(len(render)):render[i].render(scale=1.45).to_pil().save(QA/f'page-{i+1}.png')
print(PDF)

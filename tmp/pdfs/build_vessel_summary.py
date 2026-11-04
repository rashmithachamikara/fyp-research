from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'output/pdf/sri_lanka_satellite_vessel_research_summary.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)
pdfmetrics.registerFont(TTFont('Arial', 'C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold', 'C:/Windows/Fonts/arialbd.ttf'))
pdfmetrics.registerFontFamily('Arial', normal='Arial', bold='Arial-Bold', italic='Arial', boldItalic='Arial-Bold')
NAVY = colors.HexColor('#12304A')
TEAL = colors.HexColor('#087F8C')
INK = colors.HexColor('#243746')
MUTED = colors.HexColor('#526575')
PALE = colors.HexColor('#EDF5F7')
W, H = A4
WIDTH = W-88
S = {
 'title': ParagraphStyle('title',fontName='Arial-Bold',fontSize=26,leading=31,textColor=NAVY,spaceAfter=15),
 'sub': ParagraphStyle('sub',fontName='Arial',fontSize=12,leading=17,textColor=MUTED,spaceAfter=16),
 'h1': ParagraphStyle('h1',fontName='Arial-Bold',fontSize=20,leading=25,textColor=NAVY,spaceAfter=16),
 'h2': ParagraphStyle('h2',fontName='Arial-Bold',fontSize=11.5,leading=15,textColor=TEAL,spaceBefore=12,spaceAfter=7),
 'body': ParagraphStyle('body',fontName='Arial',fontSize=10,leading=14.5,textColor=INK,spaceAfter=9),
 'small': ParagraphStyle('small',fontName='Arial',fontSize=8.8,leading=12.5,textColor=MUTED,spaceAfter=7),
 'cell': ParagraphStyle('cell',fontName='Arial',fontSize=9,leading=12.5,textColor=INK),
 'head': ParagraphStyle('head',fontName='Arial-Bold',fontSize=9,leading=12,textColor=colors.white),
 'ref': ParagraphStyle('ref',fontName='Arial',fontSize=9.5,leading=13.5,textColor=INK,spaceAfter=10),
}
URL = {
1:'https://arxiv.org/abs/2206.00897',
2:'https://www.nature.com/articles/s41598-022-23688-7',
3:'https://www.nature.com/articles/s41586-023-06825-8',
4:'https://doi.org/10.1016/j.patrec.2025.02.022',
5:'https://doi.org/10.3390/rs13214255',
6:'https://doi.org/10.1016/j.isprsjprs.2025.10.027',
7:'https://doi.org/10.1016/j.oceaneng.2026.127531',
8:'https://arxiv.org/abs/2608.01963',
9:'https://github.com/chaozhong2010/HRSID',
10:'https://globalfishingwatch.org/global-fishing-watch-data-availability/',
11:'https://dataspace.copernicus.eu/explore-data',
12:'https://globalfishingwatch.org/press-release/analysis-shows-vessels-identification-switched-off/',
13:'https://www.cabinetoffice.gov.lk/cab/index.php?Itemid=49&dID=14049&id=16&lang=en&option=com_content&view=article',
14:'https://globalfishingwatch.org/faqs/how-can-i-interpret-night-light-detections-viirs-data/',
15:'https://sentiwiki.copernicus.eu/web/s1-products',
}
def link(label,url):
 return '<a href="'+escape(url, {'"':'&quot;'})+'" color="#087F8C">'+escape(label)+'</a>'
def cite(*nums):
 return ' ' + ' '.join(link('['+str(n)+']', URL[n]) for n in nums)
def p(t,kind='body'): return Paragraph(t,S[kind])
story=[]
def add(t,kind='body'): story.append(p(t,kind))
def heading(t): add(t,'h2')
def table(headers,rows,widths):
 data=[[p(x,'head') for x in headers]]+[[p(x,'cell') for x in row] for row in rows]
 t=Table(data,colWidths=[WIDTH*x for x in widths],hAlign='LEFT',repeatRows=1)
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),NAVY),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),9),('RIGHTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9),('ROWBACKGROUNDS',(0,1),(-1,-1),[PALE,colors.white]),('LINEBELOW',(0,-1),(-1,-1),0.5,colors.HexColor('#CCDCE2'))]))
 story.extend([t,Spacer(1,10)])
def callout(t):
 t=Table([[p(t)]],colWidths=[WIDTH])
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),PALE),('BOX',(0,0),(-1,-1),0.6,colors.HexColor('#C7E0E5')),('LEFTPADDING',(0,0),(-1,-1),13),('RIGHTPADDING',(0,0),(-1,-1),13),('TOPPADDING',(0,0),(-1,-1),11),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
 story.extend([t,Spacer(1,10)])
def page(title): story.append(PageBreak()); add(title,'h1')

add('RESEARCH BRIEF  |  02 NOVEMBER 2026','small')
add('Satellite vessel detection<br/>for Sri Lanka','title')
add('A beginner-friendly summary of methods, datasets, existing research and realistic project opportunities.','sub')
callout('<b>Yes, this is technically possible.</b> Satellite imagery can reveal vessels around Sri Lanka and help flag suspected illegal fishing. Establishing illegality also requires evidence about activity, identity and the rules or permissions that apply.')
heading('Three different questions')
table(['Question','Evidence needed'],[
('1. Is a boat here?','Satellite imagery and an object detector: software that finds boats in an image.'),
('2. Which boat is it, and what is it doing?','Tracking messages, vessel records and observations over time. A single image usually provides limited activity evidence.'),
('3. Is the activity illegal?','The observed activity, relevant restrictions and authorisations; sometimes inspection or other corroborating evidence.')
],[.35,.65])
add('An unmatched satellite detection means the boat could not be associated with the available tracking data. It does not by itself show that the boat is operating illegally. Missing messages can reflect reception problems, equipment issues or deliberate disabling.'+cite(12))
heading('What is already researched?')
add('Optical and radar ship detection, matching satellite detections to AIS, combining sensors, learning with few labels and transferring models between environments all have prior research. Simply combining SAR, optical imagery and AIS is not a new research contribution.'+cite(1,2,4,5,6,7))
heading('The abbreviations in plain language')
add('<b>SAR</b> = synthetic aperture radar, an imaging radar carried by a satellite.<br/><b>AIS</b> = Automatic Identification System, which broadcasts vessel identity and position.<br/><b>VMS</b> = Vessel Monitoring System, used for fisheries tracking.<br/><b>VIIRS</b> = Visible Infrared Imaging Radiometer Suite; its low-light observations can reveal brightly lit vessels.','small')
heading('How to use this report')
add('Pages 2-4 compare technologies, representative studies and training data. Page 5 explains a feasible Sri Lankan project. Pages 6-7 provide clickable paper and dataset links. This is a selected literature summary, not a systematic review or a certification that a proposed gap is novel.','small')

page('1 / Compare the technologies')
table(['Input / method','What it contributes','Main limitations'],[
('Optical imagery<br/>(e.g. Sentinel-2)','A camera-like view. Useful for vessel appearance, coastline context and checking detections.','Clouds and daylight restrict observations. Small boats occupy few pixels. High-resolution commercial imagery can add cost.'),
('SAR imagery<br/>(e.g. Sentinel-1)','Radar detects reflections and works at night and through clouds. A useful starting point for independent vessel detection.','Waves, rocks, ports and structures can resemble vessels. Small or weakly reflecting boats are difficult; results vary with sea state and acquisition geometry.'),
('AIS tracks','Broadcast position and identity information. Tracks support movement analysis and association with image detections.','Covers broadcasting vessels captured by the available receivers. Gaps, inaccurate messages and restricted historical access complicate analysis.'),
('SAR + AIS','Finds visible targets that do or do not match tracking records. Helps prioritise investigation.','Time gaps and uncertain positions cause incorrect matches. No match is an observation about data, not a verdict of illegality.'),
('SAR + optical + AIS','Combines independent detection, visual detail and tracking information. Can support cross-checking.','Different observation times mean the boat may move. Spatial alignment, missing images and data preparation add complexity.'),
('VIIRS night lights','Detects bright lights at night, including some fishing activity that is absent from AIS.','Misses vessels with no lights or dim lights; cloud affects visibility. It is not a complete census of boats.'),
('VMS','A vessel-borne monitoring device reports positions to fisheries monitoring systems. Can support compliance checks.','Requires installed, functioning equipment and access to the records. It is distinct from independent satellite imaging.')
],[.23,.35,.42])
add('Sources: vessel detection and tracking [1-4]; optical learning [5]; image fusion [6]; VMS context [13]; VIIRS [14].'+cite(1,2,3,4,5,6,13,14),'small')
callout('<b>Resolution is not the same as pixel spacing.</b> For example, a common Sentinel-1 IW GRD product has 10 m pixel spacing but approximately 20 x 22 m spatial resolution. A small bright target can still appear, but that does not guarantee reliable detection or recognisable vessel detail.'+cite(15))

page('2 / What existing studies demonstrate')
add('The limitations below distinguish the scope of reported evidence from practical implications for a Sri Lankan project. A method tested elsewhere is not automatically unreliable in Sri Lanka; its local reliability remains to be measured.','small')
table(['Study','Contribution','Limits / implication for your project'],[
('xView3-SAR<br/>Paolo et al., 2022'+cite(1),'Large Sentinel-1 benchmark for vessel detection, fishing-vessel characterisation and length estimation.','Labels combine automated and manual analysis. It is not a dataset of independently confirmed illegal acts.'),
('Revealing the global longline fleet<br/>Kroodsma et al., 2022'+cite(2),'Probabilistic radar-AIS matching: estimates plausible vessel positions instead of simply using the nearest AIS point.','Study used 24 RADARSAT-2 scenes in selected regions, with analyst review of ambiguous matches. The same reliability is not established for every coast or fleet.'),
('Satellite mapping of industrial activity<br/>Paolo et al., 2024'+cite(3),'Large-scale radar detection combined with AIS and models to characterise maritime activity.','Small boats remain difficult. The analysis excluded fishing classification within 1 km of shore. Fishing classification does not establish illegal fishing.'),
('Multimodal AI-enhanced ship detection<br/>Galdelli et al., 2025'+cite(4),'Combines SAR/optical detection with AIS matching to highlight potentially suspicious vessels.','Its Ancona case study is geographically limited. Suspicious or unmatched detections are not independently confirmed offences.'),
('Sentinel-2 self-supervised learning<br/>Ciocarlan &amp; Stoian, 2021'+cite(5),'Learns useful image features from unlabelled imagery, then trains a detector using labelled examples.','Small harbour-based dataset. Reduces label requirements; does not eliminate labels or demonstrate transfer to all coastal conditions.'),
('MHFNet<br/>Zhang et al., 2026'+cite(6),'Studies SAR-optical fusion when paired images are spatially misaligned.','Alignment handling does not establish that a moving vessel remains the same target across widely separated observation times. Assessment here is based on the publisher abstract/preview.'),
('GDOS<br/>2026'+cite(7),'Studies generalisation to unseen SAR environments using multiple training domains and sea-clutter modelling.','Confirms that cross-environment generalisation is already researched. Benchmark success alone does not establish performance in Sri Lankan waters; preview-level assessment here.')
],[.25,.34,.41])
add('<b>Do not rank these studies by their headline accuracy.</b> They use different sensors, datasets, target sizes, geographic splits and tasks. Compare models on the same held-out scenes and report both missed vessels and false detections.','small')

page('3 / Datasets you can start with')
table(['Dataset / source','Useful for','What to check'],[
('xView3-SAR'+cite(1),'Nearly 1,000 large Sentinel-1 scenes, with vessel/object annotations and environmental layers. Strong fit for medium-resolution SAR research.','Large storage/processing requirement. Different splits and annotation confidence levels matter; original competition holdout data are not equivalent to public training data.'),
('HRSID'+cite(9),'5,604 high-resolution SAR image chips and 16,951 ship instances. Useful for detection and segmentation experiments.','Its 0.5-3 m imagery differs from ordinary Sentinel-1 GRD. Good results here do not imply equally good small-boat detection in coarser imagery.'),
('OSSDD'+cite(8),'15,197 Sentinel-1 patches with 55,759 ships; masks and bounding boxes. A practical alternative for patch-based experiments.','2026 preprint. Inspect annotation construction, split independence, licence and download requirements before selecting it.'),
('S2-SHIPS'+cite(5),'16 Sentinel-2 harbour images with 1,053 annotated ships. Suitable for an optical pilot and learning with limited labels.','Small geographic and scene sample; not representative of all offshore or Sri Lankan conditions.'),
('Global Fishing Watch'+cite(10),'Fishing-activity products, satellite detections and other vessel/event datasets, depending on product and access.','Derived products are not automatically unrestricted raw AIS histories. Check coverage, access terms and whether exact observation times and vessel identifiers are available.'),
('Copernicus Data Space'+cite(11),'Existing Sentinel-1 and Sentinel-2 imagery for Sri Lankan study areas. Can supply deployment or evaluation scenes.','Raw imagery is not a labelled boat dataset. Cloud screening, image preparation and evaluation annotations may still be needed.')
],[.23,.39,.38])
heading('What these datasets do not provide')
add('A ship label means that an object was annotated as a ship. A fishing-vessel label describes vessel type or inferred activity. Neither is automatically a verified illegal-fishing label. A model trained on these labels should not be evaluated as if it predicts confirmed offences.')
heading('Training data and test data have different jobs')
add('<b>Training data</b> teaches the model. <b>Test data</b> measures whether it works on unfamiliar examples. Keep entire scenes, locations and dates separate where appropriate: nearby crops from one image can otherwise make the test artificially easy.')
add('Direct download or repository links are collected on pages 6-7. Dataset availability does not guarantee matching AIS or legal-authorisation records for the same images.','small')

page('4 / A realistic project for Sri Lanka')
heading('Can you do this without collecting Sri Lankan data?')
table(['Constraint','What is feasible'],[
('No field surveys or boat-mounted sensors','Yes. Train on existing datasets and use archived satellite imagery.'),
('No Sri Lankan training labels','Yes, as a transfer experiment. Train elsewhere and evaluate on separate Sri Lankan examples.'),
('No Sri Lankan observations or evaluation at all','A general prototype is possible, but you cannot substantiate a claim of reliable performance in Sri Lanka.')
],[.43,.57])
add('Sri Lanka already has vessel monitoring infrastructure. A July 2026 Cabinet announcement reported 4,200 registered multi-day vessels equipped with monitoring systems and approved further expansion. This does not imply that those records are publicly available or that every boat is covered.'+cite(13))
heading('Recommended starting scope')
add('<b>Detect vessels in selected Sri Lankan coastal scenes and explain which need review.</b> Define one sensor, area, period and vessel-size range. Add AIS matching after confirming access to suitably timed records.')
callout('<b>Example output:</b> "Vessel detected at this location and time; no matching AIS record in the available dataset; activity unknown; review recommended." Add a restricted-area flag only when the applicable boundary, rule and observation time have been checked.')
heading('Possible research questions - novelty still needs checking')
add('<b>A. Transfer reliability:</b> Can a model trained outside Sri Lanka retain vessel recall while controlling false alarms in unfamiliar coastal scenes?<br/><b>B. Matching uncertainty:</b> Can a method reduce incorrect unmatched-vessel alerts when AIS messages are sparse?<br/><b>C. Small-vessel performance:</b> Can a method improve detection in a defined size range without creating excessive coastal false alarms?')
add('All three areas have prior work. A contribution needs a specific improvement or evaluation that existing studies do not provide. A Sri Lankan application alone does not establish methodological novelty.')
heading('How to evaluate it')
add('Measure <b>precision</b> (the proportion of detections that are real vessels), <b>recall</b> (the proportion of real vessels found), and <b>false alerts per scene or area</b>. Break down results by size and distance from shore. Evaluate incorrect AIS matches and unmatched alerts. Missing AIS cannot establish "no boat".')
add('<b>Practical contribution:</b> a transparent decision-support tool that helps prioritise investigation. Claims about confirmed illegal fishing require additional labelled evidence about offences.','small')

page('5 / Papers and reading links')
add('Numbers match the citations throughout the report. Paper titles and access links are clickable. Read the first four for the central detection-to-investigation workflow.','small')
refs=[
(1,'Paolo, F., et al. (2022). xView3-SAR: Detecting Dark Fishing Activity Using Synthetic Aperture Radar Imagery. NeurIPS 2022.','Paper and public benchmark; useful starting point for SAR training.', [('Dataset portal','https://iuu.xview.us/')]),
(2,'Kroodsma, D., et al. (2022). Revealing the global longline fleet with satellite radar. Scientific Reports.','Radar-AIS matching and limits of vessel visibility.', [('Code and derived data','https://github.com/GlobalFishingWatch/paper-longline-ais-sar-matching')]),
(3,'Paolo, F. S., et al. (2024). Satellite mapping reveals extensive industrial activity at sea. Nature, 625, 85-91.','Large-scale detection and characterisation of maritime activity.', []),
(4,'Galdelli, A., et al. (2025). Multimodal AI-enhanced ship detection for mapping fishing vessels and informing on suspicious activities. Pattern Recognition Letters, 191, 15-22.','Multi-source imagery plus AIS; distinguishes potential suspicion from confirmed wrongdoing.', [('Institutional record','https://iris.univpm.it/handle/11566/344341')]),
(5,'Ciocarlan, A., & Stoian, A. (2021). Ship Detection in Sentinel 2 Multi-Spectral Images with Self-Supervised Learning. Remote Sensing, 13(21), 4255.','Optical detection with limited labelled examples.', [('Code and S2-SHIPS','https://github.com/alina2204/contrastive_SSL_ship_detection')]),
(6,'Zhang, W., et al. (2026). MHFNet: Multimodal hybrid fusion framework for misaligned SAR-Optical ship detection. ISPRS Journal of Photogrammetry and Remote Sensing, 231, 151-166.','Further reading on image fusion. Abstract/preview reviewed; no independent replication.', []),
(7,'Multi-source domain generalization SAR ship detection via gated disentanglement and open-set sea clutter modeling (2026). Ocean Engineering. DOI: 10.1016/j.oceaneng.2026.127531.','Further reading on GDOS and unseen environments. Publisher preview reviewed.', []),
(8,'Hammer, H., et al. (2026). OSSDD - a New Open Dataset for Sentinel-1 Ship Detection. arXiv:2608.01963.','Preprint; data source and benchmark, not confirmed-offence labels.', [('Dataset','https://huggingface.co/datasets/sylviaHoch/OpenSARShip-Ship-Detection-Dataset')]),
]
for n,title,note,extras in refs:
 add('<b>['+str(n)+'] '+link(title,URL[n])+'</b><br/>'+escape(note)+(('<br/>'+' | '.join(link(l,u) for l,u in extras)) if extras else ''),'ref')

page('6 / Data, context and source notes')
refs2=[
(9,'HRSID official dataset repository.','High-resolution SAR benchmark, annotations and associated paper information.'),
(10,'Global Fishing Watch: Data Availability.','Check available datasets, terms and routes to data access before designing an AIS-dependent project.'),
(11,'Copernicus Data Space: Explore Data.','Access existing Sentinel imagery; search the actual study area and dates before promising coverage.'),
(12,'Global Fishing Watch (2022): Global analysis shows where fishing vessels\' identification devices have been switched off.','Research-team explanation of the Science Advances study Hotspots of Unseen Fishing Vessels. Explains why missing AIS and deliberate disabling require careful interpretation.'),
(13,'Sri Lanka Cabinet (6 July 2026): Further expansion of the Vessel Monitoring System for Multi-Day Fishing Vessels and IDAY Fishing Vessels in Sri Lanka.','Official announcement supporting the local monitoring context. This is a policy announcement, not a public VMS dataset or evidence of complete coverage.'),
(14,'Global Fishing Watch: How can I interpret night light detections (VIIRS) data in the map?','Explains what the night-light product captures and what it misses.'),
(15,'Copernicus SentiWiki: Sentinel-1 Products.','Technical documentation for product modes, spatial resolution and pixel spacing.'),
]
for n,title,note in refs2:
 add('<b>['+str(n)+'] '+link(title,URL[n])+'</b><br/>'+escape(note),'ref')
heading('Evidence boundaries')
add('This report summarises selected research and official sources discussed in the conversation, with links checked during preparation on 2 November 2026. It does not claim to cover every relevant paper. Recent methods reviewed only through abstracts or publisher previews are identified on page 3.')
add('The proposed project questions and evaluation recommendations are synthesis and research-design suggestions. They are not findings that a new system has already achieved, and they are not a completed novelty assessment.')
add('A higher detection score on a benchmark is not proof of better performance on Sri Lankan small boats. An unmatched target is not proof of deliberate concealment. A likely fishing vessel is not proof of illegal fishing. These distinctions should remain visible in the final project and its user interface.')

def chrome(c,doc):
 c.saveState()
 c.setFillColor(TEAL); c.rect(0,H-8,W,8,fill=1,stroke=0)
 c.setFont('Arial',8); c.setFillColor(MUTED)
 c.drawString(44,H-31,'SATELLITE VESSEL DETECTION  /  SRI LANKA')
 c.setStrokeColor(colors.HexColor('#D9E4E9')); c.line(44,43,W-44,43)
 c.drawString(44,29,'Research summary | 2 November 2026')
 c.drawRightString(W-44,29,str(doc.page))
 c.restoreState()
doc=SimpleDocTemplate(str(OUT),pagesize=A4,rightMargin=44,leftMargin=44,topMargin=57,bottomMargin=57,title='Satellite vessel detection for Sri Lanka - Research summary',author='Research summary prepared with Codex',subject='Methods, datasets, limitations and research opportunities')
doc.build(story,onFirstPage=chrome,onLaterPages=chrome)
print(OUT)

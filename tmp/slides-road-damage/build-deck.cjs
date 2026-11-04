const pptxgen = require('pptxgenjs');
const fs = require('fs');
const path = require('path');
const pptx = new pptxgen();
pptx.layout = 'LAYOUT_WIDE';
pptx.author = 'University of Moratuwa | Research proposal team';
pptx.subject = 'IS 4990 proposal evaluation | Road-damage research proposal v8';
pptx.title = 'Small Road-Damage Detection Across Unseen Countries';
pptx.company = 'Faculty of Information Technology, University of Moratuwa';
pptx.lang = 'en-GB';
pptx.theme = {headFontFace:'Arial',bodyFontFace:'Arial',lang:'en-GB'};
const C={ink:'202A31',muted:'59666F',paper:'FFFFFF',pale:'F0F3F5',line:'D6DEE2',yellow:'F2B134',teal:'117D75',tealPale:'E9F4F1',rust:'B44E37',rustPale:'FAEEEA',dark:'172127',white:'FFFFFF'};
const W=13.333333,H=7.5;
const root=process.cwd(),out=path.join(root,'output','presentations');
fs.mkdirSync(out,{recursive:true});
const slidesMeta=[];
function txt(s,t,x,y,w,h,size=20,color=C.ink,extra={}){const minimumHeight=(size/72)*1.28*(String(t).split('\n').length);s.addText(t,{x,y,w,h:Math.max(h,minimumHeight),fontFace:'Arial',fontSize:size,color,margin:0,breakLine:false,vertAnchor:'mid',...extra});}
function rect(s,x,y,w,h,fill,line=fill,extra={}){s.addShape(pptx.ShapeType.rect,{x,y,w,h,fill:{color:fill},line:{color:line,width:1},...extra});}
function line(s,x1,y1,x2,y2,color=C.line,width=1,arrow=false){s.addShape(pptx.ShapeType.line,{x:Math.min(x1,x2),y:Math.min(y1,y2),w:Math.abs(x2-x1),h:Math.abs(y2-y1),flipH:x2<x1,flipV:y2<y1,line:{color,width,...(arrow?{beginArrowType:'none',endArrowType:'triangle'}:{})}});}
function circle(s,x,y,d,fill){s.addShape(pptx.ShapeType.ellipse,{x,y,w:d,h:d,fill:{color:fill},line:{color:fill}});}
function label(s,t,x,y,w,color=C.muted){txt(s,t.toUpperCase(),x,y,w,.25,11,color,{bold:true,charSpacing:1.4});}
function para(s,head,body,x,y,w,color=C.ink){txt(s,head,x,y,w,.34,22,color,{bold:true});txt(s,body,x,y+.53,w,1.02,20,C.muted,{valign:'top',breakLine:false});}
function tag(s,t,x,y,w,color=C.teal){rect(s,x,y,w,.42,color);txt(s,t,x+.12,y+.04,w-.24,.32,12,C.white,{bold:true});}
function footer(s,n,source,dark=false){txt(s,source,.6,7.03,11.35,.19,9.5,dark?'A6B5BE':C.muted);txt(s,String(n).padStart(2,'0'),12.12,6.98,.6,.28,12,dark?'A6B5BE':C.muted,{align:'right'});}
function slide(title,section,seconds,speaker,source,dark=false){const s=pptx.addSlide();s.background={color:dark?C.dark:C.white};label(s,section,.6,.25,11,dark?C.yellow:C.teal);txt(s,title,.6,.78,12.1,.7,35,dark?C.white:C.ink,{bold:true});footer(s,pptx._slides.length,source,dark);slidesMeta.push({title,seconds,speaker});return s;}
function notes(s,text,refs,qa=''){const m=slidesMeta[slidesMeta.length-1];s.addNotes(`SPEAKER: ${m.speaker}\nTIME: ${m.seconds} seconds\n\n${text}\n\nSOURCE: Road-Damage-Research-Proposal-v8.pdf, 29 October 2026. ${refs}\n\n${qa?'Q&A PREPARATION: '+qa:''}`);}
function comparison(s,left,right,y=2.05){label(s,'PROPOSED METHOD',.7,y,5.4,C.teal);label(s,'PRINCIPAL COMPARATOR',7.12,y,5.4);txt(s,left,.7,y+.45,5.35,1.07,27,C.ink,{bold:true,valign:'top'});txt(s,right,7.12,y+.45,5.4,1.07,27,C.ink,{bold:true,valign:'top'});circle(s,6.17,y+.49,.55,C.pale);txt(s,'vs',6.17,y+.61,.55,.22,13,C.muted,{align:'center',bold:true});}

// 01 / The title carries the full research question in its notes.
{
const s=slide('Small road-damage detection','IS 4990 | RESEARCH PROPOSAL',10,'Member A','University of Moratuwa | Faculty of IT | IT & Management | Proposal v8, 29 Oct 2026',true);
txt(s,'Across unseen countries',.6,1.62,11.7,.7,38,C.yellow,{bold:true});
txt(s,'Three controlled studies in assignment, consistency\nand missed-damage prediction',.64,2.65,10.9,1.1,25,C.white,{breakLine:false});
const xs=[.65,4.85,9.05],names=['A  |  ASSIGN','B  |  STABILISE','C  |  FLAG MISSES'];
xs.forEach((x,i)=>{circle(s,x,4.58,.65,[C.yellow,C.teal,C.rust][i]);txt(s,String.fromCharCode(65+i),x,4.74,.65,.25,20,i===0?C.dark:C.white,{align:'center',bold:true});txt(s,names[i].split('  |  ')[1],x+.88,4.76,3.0,.3,19,C.white,{bold:true});});
txt(s,'Three-member final-year research project',.65,6.21,11.8,.36,17,'A6B5BE');
notes(s,'Our proposal asks whether three targeted changes can improve detection, or predict missed small and thin damage, on countries excluded from training. Each member owns a separate controlled study.','Summary and main research question, pp. 1, 6-7.');
}
// 02 / Motivation: hypothesis is explicitly distinct from established shift.
{
const s=slide('The problem: country shift and silent misses','BACKGROUND | 00:10-00:50',40,'Member A','Sources: proposal v8, pp. 2-3; Arya et al. (2020); RDD2022 / CRDDC\'2022');
label(s,'TRAINING CONTEXT',.7,1.85,4.1);txt(s,'Source-country roads',.7,2.3,4.1,.55,27,C.ink,{bold:true});
label(s,'UNSEEN CONTEXT',7.65,1.85,4.8);txt(s,'Different roads + cameras',7.65,2.3,4.95,.55,27,C.ink,{bold:true});
line(s,5.1,2.6,7.1,2.6,C.teal,3,true);
para(s,'Appearance changes','Surface, lighting, markings and viewpoint shift.',.7,3.55,3.6);
para(s,'Small / thin damage','Its recall under shift must be measured.',4.85,3.55,3.6);
para(s,'Misses stay invisible','A missing box gives an operator no warning.',9.0,3.55,3.6);
rect(s,.7,5.73,11.93,.67,C.tealPale);txt(s,'Research aim: measure transfer and flag likely misses without target-country data.',.92,5.9,11.45,.3,20,C.teal,{bold:true});
notes(s,'A detector trained on one set of roads encounters different surfaces, camera positions and lighting in a new country. Prior road-damage work establishes transfer problems. The proposal targets small or thin boxes, but whether they fail first in our folds is a question we will measure. A missed crack creates no output box. This motivates both detector improvements and a separate warning model for likely misses. Road agencies and inspection teams are the intended stakeholders; deployment benefits are outside the claim.','Problem and motivation, pp. 2-3; Arya et al. (2020), cited in proposal.');
}
// 03 / Literature: compact, bounded comparisons.
{
const s=slide('The gap is in the controlled comparisons','LITERATURE & GAP | 00:50-02:00',70,'Member A','Sources: Chen et al. (2026), MAMDG; Wang et al. (2021), NWD; Danish et al. (2024); Rahman et al. (2019)');
rect(s,.7,1.7,11.93,.62,C.tealPale);txt(s,'Source-only road-damage transfer already exists: MAMDG (Chen et al., 2026).',.92,1.88,11.5,.25,19,C.teal,{bold:true});
label(s,'EXISTING IDEA',1.3,2.64,4.45);label(s,'OUR QUESTION ON AN UNSEEN COUNTRY',6.65,2.64,5.7);
const rows=[['A','Size-aware matching / NWD','Does short-side scaling beat equally tuned plain NWD?'],['B','Consistency across views','Does choosing small / thin boxes beat generic consistency?'],['C','Prediction of detector misses','Do features add value beyond learned weak detections?']];
rows.forEach((r,i)=>{const y=3.13+i*.89;circle(s,.73,y,.41,[C.yellow,C.teal,C.rust][i]);txt(s,r[0],.73,y+.085,.41,.2,13,i===0?C.ink:C.white,{align:'center',bold:true});txt(s,r[1],1.3,y+.02,4.75,.56,21,C.ink,{bold:true});txt(s,r[2],6.65,y+.02,5.7,.7,19.5,C.ink);if(i<2)line(s,1.3,y+.76,12.48,y+.76,C.line,.8);});
txt(s,'Bounded to papers examined. Full MAMDG experiments and MSDA-RDD reading remain a week 1-3 gate.',.73,6.25,11.8,.38,16,C.rust,{bold:true});
notes(s,'The cross-country source-only setting is not our novelty. MAMDG already studies domain generalisation for road damage using feature alignment. NWD and related assignment papers already address small objects. Cross-view consistency and predicting detector misses also have established precedents. Our bounded contribution is three specific comparisons under the same country-transfer protocol. A tests short-side scaling against equally tuned plain NWD. B tests which objects receive consistency. C tests whether detector features add information beyond a learned model of weak outputs. The proposal has only partial access to MAMDG and unverified details for MSDA-RDD. Reading those in full is an early gate before the final novelty claim.','Literature and bounded gap, pp. 3-6; references pp. 26-27. Literature summaries retain the proposal\'s access limitations.','Do not claim to be first at domain generalisation or miss prediction. NWD/SimD, Danish, and Rahman are close method neighbours.');
}
// 04 / Four-country matrix and freeze sequence.
{
const s=slide('Four folds, with development kept source-only','SHARED DESIGN | 02:00-02:40',40,'Member A','Source: proposal v8, pp. 9-11 | Baseline: YOLO11s, 640 px, COCO weights; Ultralytics 8.4.192');
const cx=[3.0,5.3,7.6,9.9],country=['Japan','India','United States','Czech Republic'];
country.forEach((t,j)=>txt(s,t,cx[j],1.88,2.1,.43,17,C.ink,{align:'center',bold:true}));
for(let i=0;i<4;i++){txt(s,`Fold ${i+1}`,.73,2.6+i*.56,1.6,.3,17,C.muted);for(let j=0;j<4;j++){rect(s,cx[j],2.48+i*.56,2.1,.43,i===j?C.dark:C.tealPale);txt(s,i===j?'HELD OUT':'SOURCE',cx[j],2.59+i*.56,2.1,.2,12,i===j?C.yellow:C.teal,{align:'center',bold:true});}}
const stages=[['Develop','2 countries + inner validation'],['Freeze','Rules and code fixed'],['Retrain','All 3 source countries'],['Evaluate','Open the held-out country once']];
stages.forEach((r,i)=>{const x=.73+i*3.12;circle(s,x,5.33,.41,i===3?C.dark:C.teal);txt(s,String(i+1),x,5.425,.41,.17,12,C.white,{align:'center',bold:true});txt(s,r[0],x+.57,5.32,2.4,.36,21,C.ink,{bold:true});txt(s,r[1],x+.57,5.9,2.31,.56,16,C.muted);if(i<3)line(s,x+2.65,5.53,x+2.99,5.53,C.line,1.2,true);});
notes(s,'Each country is the held-out target once. During development, one of the remaining three countries is the inner validation country and two supply training data. Only source data choose settings and thresholds. After configuration freeze, retrain on all three sources. Final detector training, checkpoint selection, C fitting and C selection use separate source slices, approximately 70, 10, 10 and 10 percent. Global freeze is week 22; held-out results are opened once afterward.','Dataset roles and decision table, pp. 9-11.','Fixed inner countries: Japan out -> US; India out -> Czech Republic; US out -> Japan; Czech Republic out -> India. Global design changes are logged and applied uniformly, not tuned from target results.');
}
// 05 / Dataset evidence and geometry definitions.
{
const s=slide('RDD2022: 25,846 labelled images','DATA & DEFINITIONS | 02:40-03:05',25,'Member A','Source: Arya et al. (2024), RDD2022, Geoscience Data Journal; proposal v8, pp. 8-9 | CC BY-SA 4.0');
const countries=['Japan','India','United States','Czech Republic'],counts=[10506,7706,4805,2829];
s.addChart(pptx.ChartType.bar,[{name:'Labelled images',labels:countries.slice().reverse(),values:counts.slice().reverse()}],{x:.6,y:1.68,w:8.4,h:3.58,barDir:'bar',barGrouping:'clustered',catAxisLabelFontFace:'Arial',catAxisLabelFontSize:18,catAxisLabelColor:C.ink,catAxisLineShow:false,catAxisMajorTickMark:'none',catAxisMinorTickMark:'none',valAxisHidden:true,valAxisMinVal:0,valAxisMaxVal:13000,showValue:true,dataLabelPosition:'outEnd',dataLabelFormatCode:'#,##0',dataLabelColor:C.ink,dataLabelBkgrdColor:C.white,dataLabelFontFace:'Arial',dataLabelFontSize:17,chartColors:[C.teal],showLegend:false,showTitle:false,showBorder:false,showCatName:false,catGridLine:{style:'none'},valGridLine:{style:'none'},chartArea:{fill:{color:C.white},border:{color:C.white,pt:0}},plotArea:{fill:{color:C.white},border:{color:C.white,pt:0}},showShadow:false,gapSize:95});
label(s,'BOX GEOMETRY AT 640 PX',9.43,1.91,3.1);
rect(s,9.48,2.52,.78,.78,C.white,C.teal);txt(s,'Small',10.5,2.49,1.95,.33,21,C.ink,{bold:true});txt(s,'Area < 32 × 32 px',10.5,2.98,2.1,.62,16,C.muted);
rect(s,9.48,4.02,.21,1.12,C.white,C.rust);txt(s,'Thin',10.5,4.01,1.95,.33,21,C.ink,{bold:true});txt(s,'Short side < 16 px',10.5,4.5,2.1,.55,16,C.muted);
txt(s,'D00 longitudinal   /   D10 transverse   /   D20 alligator   /   D40 pothole',.73,5.61,11.9,.38,19,C.ink,{bold:true});
txt(s,'Keep duplicate groups together. Keep labelled negatives. Flag rare classes. Box size is not crack severity.',.73,6.23,11.9,.42,16,C.muted);
notes(s,'The four labelled training-country subsets contain 25,846 images and four official damage classes. We retain genuine labelled negatives and split duplicate groups together. Small means area below 32 squared pixels; thin means short side below 16 pixels, both at a fixed 640-pixel reference. Their union counts each box once. These definitions describe boxes, not physical crack severity.','RDD2022 counts, class mapping, data preparation, pp. 8-9.','Official test images lack public labels and are excluded from confirmatory scoring. India D10 and US D40 have low support; missing annotation files are never treated as clean road.');
}
// 06 / Member A mechanism: calculated example, no empirical result.
{
const s=slide('A: scale assignment similarity by the short side','MEMBER A | METHOD | 03:05-03:50',45,'Member A','Sources: proposal v8, pp. 12-13; Wang et al. (2021), NWD | Values below are a mathematical illustration');
label(s,'PLAIN NWD',.73,1.9,4.7);txt(s,'S = exp(−W₂ / C)',.73,2.35,5.2,.6,31,C.ink,{bold:true});
label(s,'SHORT-SIDE-RELATIVE NWD',7.0,1.9,5.5,C.teal);txt(s,'S = exp(−W₂ / (κ × s))',7.0,2.35,5.6,.6,31,C.teal,{bold:true});
txt(s,'C is constant for all boxes',.73,3.08,5.3,.36,20,C.muted);txt(s,'s = min(width, height) of the labelled box',7.0,3.08,5.6,.54,19,C.muted);
label(s,'SAME 2 PX DISTANCE, κ = 1',.73,4.11,5.6);
rect(s,.76,4.68,.16,.82,C.white,C.rust);txt(s,'2 px short side → S ≈ 0.37',1.24,4.85,5.28,.4,23,C.rust,{bold:true});
rect(s,7.02,4.68,.82,.82,C.white,C.teal);txt(s,'20 px → S ≈ 0.90',8.14,4.85,4.3,.4,23,C.teal,{bold:true});
txt(s,'Stricter on thin boxes; affects assignment and target-score weights.',.73,6.11,11.8,.53,21,C.ink,{bold:true});
notes(s,'A replaces the overlap similarity inside YOLO11\'s task-aligned assigner. Plain NWD divides box distance by one constant. A divides by the labelled box\'s short side times a tuned tolerance. This is stricter on thin boxes, not more forgiving. At a two-pixel distance and tolerance one, the equation gives similarity about 0.37 for a two-pixel short side and 0.90 for twenty pixels. These are calculated examples, not results. The score affects both positive selection and supervision weights, so we measure both.','Member A equations and mechanism, pp. 12-13; NWD reference p. 26.','W₂ is the Euclidean length of the vector of centre offsets and half-width/half-height differences. Same candidate eligibility for both methods, including built-in 16 px widening in the proposal\'s pinned Ultralytics release.');
}
// 07 / Member A comparison.
{
const s=slide('A: test normalisation against a fair rival','MEMBER A | EXPERIMENT | 03:50-04:30',40,'Member A','Source: proposal v8, pp. 6, 12-13, 16-17 | Original training labels in the core study');
comparison(s,'Short-side-relative\nNWD','Plain NWD\nwith equally tuned C');
para(s,'Keep fixed','Candidate eligibility, data, training schedule and tuning budget.',.73,4.02,3.55);
para(s,'Primary outcome','Held-out mAP50:95, averaged equally across countries.',4.88,4.02,3.55);
para(s,'Explain the mechanism','Positives per box, zero-positive boxes and target-weight mass.',9.03,4.02,3.55);
rect(s,.73,6.02,11.85,.55,C.pale);txt(s,'H1: higher held-out mAP50:95. Small / thin breakdowns are secondary; noisy boxes are extension-only.',.91,6.17,11.5,.25,16,C.ink,{bold:true});
notes(s,'The principal comparison changes normalisation alone: A versus plain NWD, with identical candidate eligibility and equally tuned constants. The original YOLO assigner remains a baseline control. The primary outcome is held-out mAP50:95, reported per country and as a country-macro average. Geometry-specific performance and assignment logs explain any difference. Noisy training boxes are an extension requiring extra GPU capacity; the core study uses original labels.','Member A principal contrast and evaluation, pp. 6, 12-13, 16-17.','Do not describe A as a new family of size-aware assignment. Its claim is the controlled short-side-relative transfer test. Optional noise extension uses unchanged target labels and a -1.0 mAP-point clean-performance margin.');
}
// 08 / Member B editable computational graph.
{
const s=slide('B: anchor consistency on small and thin boxes','MEMBER B | METHOD | 04:30-05:20',50,'Member B','Sources: proposal v8, pp. 13-14; Danish et al. (2024), CVPR | Proposed training graph');
rect(s,.76,2.01,3.05,.85,C.tealPale);txt(s,'Student · 640 px',.96,2.24,2.65,.37,24,C.teal,{bold:true});
rect(s,.76,4.17,3.05,.85,C.pale);txt(s,'Student · 320 px',.96,4.4,2.65,.37,24,C.ink,{bold:true});
rect(s,9.05,2.01,3.48,.85,C.pale);txt(s,'EMA teacher · 640 px',9.23,2.24,3.15,.37,20,C.ink,{bold:true});
txt(s,'Normal detection loss',.84,3.03,3.0,.41,19,C.muted);txt(s,'No teacher gradients',9.18,3.03,3.15,.41,19,C.muted);
line(s,4.08,2.43,8.68,2.43,C.line,1.5,true);txt(s,'EMA update',5.66,2.03,2.0,.25,13,C.muted,{align:'center'});
rect(s,5.0,4.03,4.62,1.13,C.tealPale);txt(s,'Agreement on matched\nsmall / thin boxes',5.22,4.22,4.18,.68,23,C.teal,{bold:true,align:'center'});
line(s,3.81,4.6,4.76,4.6,C.teal,2,true);line(s,10.78,3.53,10.78,4.59,C.ink,1.5);line(s,10.78,4.59,9.86,4.59,C.ink,1.5,true);
txt(s,'Bernoulli KL on class scores + L1 on normalised boxes',.76,5.78,11.75,.42,23,C.ink,{bold:true});
txt(s,'Test only the 640 px student. Exclude boxes with short side < 8 px at full size; report their share.',.76,6.35,11.75,.32,16,C.muted);
notes(s,'B keeps the ordinary detection loss on the full-size student. A half-size student view is used only for consistency, with a slow-moving EMA teacher seeing the full image. For each eligible labelled box, top-three predictions in each view are combined. Agreement uses per-class Bernoulli KL for scores and L1 for normalised boxes. The inference model remains the 640-pixel student. Boxes below eight pixels on the short side at full resolution are excluded from consistency because the half-size view is too small. Their prevalence and baseline recall are reported.','Member B training policy, matching, loss and visibility mask, pp. 13-14.','YOLO class probabilities use independent sigmoids, hence Bernoulli KL, not categorical KL. Loss averages over included boxes; zero-candidate cases are skipped and counted.');
}
// 09 / B comparison: threshold and false-positive condition are explicit.
{
const s=slide('B: separate object choice from extra training','MEMBER B | EXPERIMENT | 05:20-06:00',40,'Member B','Source: proposal v8, pp. 7, 13-14, 17 | Thresholds are chosen on source data for each final detector');
comparison(s,'Consistency on\nsmall / thin boxes','Consistency on\nall eligible boxes');
para(s,'Matched training','Identical views, supervision, loss and training budget.',.73,4.02,3.55);
para(s,'Primary outcome','Small-or-thin recall at a source-chosen threshold.',4.88,4.02,3.55);
para(s,'Secondary control','Random boxes: same count as the anchored set; one seed.',9.03,4.02,3.55);
rect(s,.73,6.0,11.85,.6,C.tealPale);txt(s,'H2 requires higher recall AND false positives per image ≤ 1.10 × generic consistency.',.92,6.18,11.48,.27,19,C.teal,{bold:true});
notes(s,'The principal comparator is generic consistency on every eligible box, with identical views, loss, supervision and training budget. A count-matched random subset is a secondary one-seed control: it tests geometry selection rather than merely fewer boxes. Each detector\'s threshold maximises recall on source selection data subject to precision at least 0.7, with a best-F1 fallback if unreachable. H2 needs higher held-out small-or-thin recall while false positives per image remain within ten percent of generic consistency. Otherwise we report the trade-off.','Member B hypothesis, controls and threshold rule, pp. 7, 13-14, 17.');
}
// 10 / Member C labels and model inputs, native dense grid.
{
const s=slide('C: predict where the detector missed damage','MEMBER C | METHOD | 06:00-06:55',55,'Member C','Sources: proposal v8, pp. 14-15; Rahman et al. (2019), IROS; Zimmermann et al. (2026), KGFP');
label(s,'INPUTS FROM A FROZEN DETECTOR',.73,1.87,6.1);
rect(s,.73,2.34,3.38,.7,C.pale);txt(s,'P3 + P4 features',.94,2.54,2.96,.3,23,C.ink,{bold:true});
rect(s,.73,3.42,3.38,.7,C.pale);txt(s,'Weak-detection map',.94,3.62,2.96,.3,18.5,C.ink,{bold:true});
txt(s,'Scores from 0.05 to the\nsource-chosen threshold',.76,4.39,3.5,.67,18,C.muted);
line(s,4.22,2.69,4.76,2.69,C.line,1.5);line(s,4.22,3.77,4.76,3.77,C.line,1.5);line(s,4.76,2.69,4.76,3.77,C.line,1.5);line(s,4.76,3.23,5.31,3.23,C.teal,2,true);
circle(s,5.57,2.55,1.35,C.teal);txt(s,'CNN\nhead',5.67,2.88,1.15,.62,18,C.white,{align:'center',bold:true});
line(s,7.18,3.23,8.05,3.23,C.teal,2,true);
label(s,'40 × 40 MISS-LOCATION GRID',8.47,1.87,4.0);
const gx=8.75,gy=2.4,cell=.3,hot=new Set(['2,2','3,2','6,4','6,5','1,6']);
for(let i=0;i<8;i++)for(let j=0;j<8;j++)rect(s,gx+j*cell,gy+i*cell,cell,cell,hot.has(`${j},${i}`)?C.rust:C.pale,C.white);
txt(s,'Schematic grid detail',8.54,5.01,3.4,.28,13,C.muted,{italic:true});
txt(s,'Positive cell = centre of an unmatched small / thin labelled box',.73,5.66,11.82,.49,23,C.ink,{bold:true});
txt(s,'Same-class, one-to-one matching at IoU ≥ 0.5. Flags likely locations; does not recover missing cracks.',.73,6.31,11.82,.38,16,C.muted);
notes(s,'C trains a small convolutional head on a frozen detector. Its inputs are pooled P3 and P4 features and a map of weak post-NMS detections between confidence 0.05 and the frozen operating threshold. Labels come from source images the detector never trained on. A cell on a 40-by-40 grid is positive if it contains the centre of an unmatched small or thin labelled box, using same-class one-to-one matching at IoU 0.5. The displayed grid is only a schematic detail. The model predicts likely missed-damage locations; it does not locate crack extent or recover the missing detections.','Member C target, architecture, weak map and source splits, pp. 14-15.','P3 is pooled from 80x80 to 40x40 and concatenated with P4; 1x1 to 32 channels, two 3x3 layers, final 1x1 logit. Weighted BCE and AdamW; select by AUPRC on C\'s separate source selection slice.');
}
// 11 / C comparison and gate.
{
const s=slide('C: ask whether internal features add information','MEMBER C | EXPERIMENT | 06:55-07:40',45,'Member C','Source: proposal v8, pp. 7, 14-15, 17 | C is evaluated first on the shared baseline detector');
comparison(s,'Head on features\n+ weak map','Matched learned head\non weak map only');
para(s,'Primary outcome','Cell-level AUPRC, with the positive-cell share stated.',.73,4.03,3.55);
para(s,'Additional baselines','Raw weak map and a features-only head.',4.88,4.03,3.55);
para(s,'No detector leakage','Separate source slices fit and select the head.',9.03,4.03,3.55);
rect(s,.73,6.0,11.85,.63,C.rustPale);txt(s,'Week 8 gate: if the grid target is unusable, switch to an image-level miss predictor.',.92,6.18,11.48,.29,19,C.rust,{bold:true});
notes(s,'H3 tests whether detector features increase held-out cell-level AUPRC beyond a matched learned head using the weak map alone. Both receive the same labels, grid and training and selection rules. Raw weak maps and features-only heads add context. Positive-cell share accompanies AUPRC because rare positives affect interpretation. The baseline detector across four folds and three seeds is primary; heads on A and B are secondary. A week-eight source-only gate checks target prevalence. If grid labels are unusable, switch to image-level miss prediction; calibration is a last-resort fallback.','Member C principal contrast, baselines and gate, pp. 7, 14-15, 17.');
}
// 12 / Summary evaluation matrix and uncertainty procedure.
{
const s=slide('Evaluate each claim on the same held-out countries','EVALUATION | 07:40-08:15',35,'Member B','Source: proposal v8, pp. 16-18 | Three seeds for principal contrasts; one-seed controls are exploratory');
const cols=[.76,2.65,8.9],ww=[1.6,5.9,3.6];label(s,'STUDY',cols[0],1.91,ww[0]);label(s,'PRINCIPAL CONTRAST',cols[1],1.91,ww[1]);label(s,'PRIMARY OUTCOME',cols[2],1.91,ww[2]);
const rows=[['A','Short-side NWD vs plain NWD','mAP50:95'],['B','Anchored vs generic consistency','Small / thin recall'],['C','Features + weak map vs weak map only','Cell-level AUPRC']];
rows.forEach((r,i)=>{const y=2.51+i*.78;rect(s,.73,y-.08,11.86,.65,i%2===0?C.pale:C.white);txt(s,r[0],.88,y+.05,1.1,.3,23,[C.ink,C.teal,C.rust][i],{bold:true});txt(s,r[1],2.65,y+.03,5.95,.36,19,C.ink);txt(s,r[2],8.9,y+.03,3.45,.36,21,C.ink,{bold:true});});
para(s,'Report variation','Each country, country-macro mean and worst country.',.76,5.11,3.65);
para(s,'Paired uncertainty','Resample images / duplicate groups; average seed-wise differences.',4.9,5.11,3.65);
para(s,'Bound the claim','Four countries do not establish worldwide generalisation.',9.04,5.11,3.55);
notes(s,'Each member has one predeclared principal contrast and outcome. Report every held-out country, an equal-country average and the worst country. Paired bootstrap intervals resample whole images with duplicate groups kept together. Compute differences separately per seed, then average; never pool predictions into an unintended ensemble. C\'s grid cells are not independent resampling units. Three seeds only roughly estimate training variation, and four countries cannot support a broad cross-country significance claim.','Evaluation and uncertainty, pp. 16-18.','With four countries even a clean sweep gives a two-sided sign-test p of 0.125. Match predictions against all ground truth before geometry-specific scoring; ignore outside-bin matches rather than counting them as errors.');
}
// 13 / Editable timeline with module ownership and actual stage gates.
{
const s=slide('Three individual studies, one 34-week plan','OWNERSHIP & MILESTONES | 08:15-08:50',35,'Member B','Source: proposal v8, pp. 21-23, step-by-step method pp. 34-39 | Weeks are relative to project approval');
const names=['Protocol + data','Baseline + pilot','Member studies','Final evaluation','Web demo','Dissertation'];
const ranges=[[1,3],[4,6],[7,22],[23,27],[28,30],[31,34]],cy=2.32,cx=3.63,cw=8.72;
[1,6,12,18,24,30,34].forEach(v=>txt(s,String(v),cx+(v-1)/34*cw-.12,1.86,.4,.24,12,C.muted,{align:'center'}));
names.forEach((t,i)=>{const y=cy+i*.5;txt(s,t,.74,y,2.65,.28,17,C.ink);rect(s,cx,y+.02,cw,.25,C.pale);const [a,b]=ranges[i];rect(s,cx+(a-1)/34*cw,y+.02,(b-a+1)/34*cw,.25,i===2?C.teal:C.ink);});
txt(s,'Gates: W3 literature / protocol   ·   W6 GPU timing   ·   W8 C target viability   ·   W22 global freeze',.74,5.66,11.9,.4,17,C.teal,{bold:true});
txt(s,'A: assignment + logs     B: consistency + recall     C: miss prediction     Shared: data, evaluation and demo',.74,6.29,11.9,.36,16,C.ink);
notes(s,'The project runs for 34 weeks from approval. The first three weeks lock the protocol and closest-literature review; week six decides compute scope; week eight checks C\'s target. Members develop separately on the shared baseline through week 22. Final training rolls forward whenever a configuration freezes, rather than waiting until week 23. Held-out evaluation follows the global freeze, then demo and writing. Each member owns their research method and analysis; shared evaluation code is infrastructure.','Timeline, resources and gates, pp. 21-23; step-by-step method, pp. 34-39.');
}
// 14 / Feasibility: one practical arithmetic example from the proposal.
{
const s=slide('Feasibility depends on the week-6 GPU pilot','RESOURCES & FALLBACKS | 08:50-09:25',35,'Member C','Source: proposal v8, pp. 18-23 | GPU times and feature-cache size are planning estimates, not measurements');
txt(s,'72',.76,1.92,3.4,1.0,65,C.teal,{bold:true});txt(s,'final detector trainings',.78,3.05,3.45,.38,21,C.ink,{bold:true});txt(s,'AB and noise study excluded.\nPlus 20-30 development runs.',.78,3.69,3.55,.84,18,C.muted);
txt(s,'500 GPU-hours',5.03,2.0,7.4,.65,33,C.ink,{bold:true});txt(s,'If committed, with 100 reserved for development:',5.03,2.97,7.4,.36,20,C.muted);
txt(s,'ordinary run must be ≈ 3.5 h or less',5.03,3.62,7.5,.5,27,C.ink,{bold:true});
txt(s,'86 run equivalents × 1.3 allowance × measured run time',5.03,4.39,7.4,.37,17,C.muted);
rect(s,.76,5.23,11.78,1.2,C.pale);txt(s,'Cut exploratory work first; benchmark YOLO11n if needed.',.98,5.43,11.3,.35,22,C.ink,{bold:true});txt(s,'Retain all four countries, three principal-contrast seeds, plain NWD and generic consistency.',.98,5.97,11.3,.27,16,C.muted);
notes(s,'The realistic core has 72 final detector trainings without AB or noise studies, plus 20 to 30 development runs. Two-view costs make this about 86 ordinary-run equivalents. With 500 committed GPU-hours and 100 reserved for development, an ordinary run needs to take about three and a half hours after a thirty-percent allowance. This is conditional, not confirmed feasibility. The week-six pilot measures runtimes. Cut optional work first, defer C\'s secondary heads, then benchmark YOLO11n if necessary. C\'s pooled-feature cache is estimated at about 60 GB and must be budgeted separately.','Compute grid, assumptions, cut ladder and risks, pp. 18-23.','The proposal\'s 10-25 GB storage table excludes the later ~60 GB cache estimate; budget at least that cache separately. Do not present free GPU quotas or runtimes as guaranteed. Noise extension adds 48 trainings and requires documented extra capacity.');
}
// 15 / Deliverables, boundaries, demonstration and Q&A close.
{
const s=slide('Expected contribution: three testable answers','CONTRIBUTION & LIMITS | 09:25-10:00',35,'Member C','Source: proposal v8, pp. 15-18, 24 | Proposed outcomes; no experimental results are claimed',true);
const ys=[1.97,3.05,4.13],heads=['A  |  Short-side-relative assignment','B  |  Small / thin consistency','C  |  Miss-location prediction'],bodies=['Does the normalisation improve held-out detection?','Does object selection improve recall at controlled false positives?','Do internal features add information beyond weak outputs?'];
heads.forEach((t,i)=>{circle(s,.77,ys[i],.44,[C.yellow,C.teal,C.rust][i]);txt(s,String.fromCharCode(65+i),.77,ys[i]+.1,.44,.19,13,i===0?C.ink:C.white,{align:'center',bold:true});txt(s,t.slice(5),1.47,ys[i]-.01,10.9,.34,24,C.white,{bold:true});txt(s,bodies[i],1.47,ys[i]+.49,10.9,.35,19,'B9C5CC');});
txt(s,'Deliver: evaluated studies + reproducible benchmark + a small web demonstration.',.77,5.61,11.8,.45,21,C.yellow,{bold:true});
txt(s,'Four-country evidence; likely-miss warnings, not recovered cracks or demonstrated safety benefits.',.77,6.25,11.8,.39,16,'B9C5CC');
notes(s,'We aim to deliver three controlled answers: whether short-side assignment helps, whether geometry-anchored consistency improves recall under a false-positive constraint, and whether features predict misses better than weak outputs alone. Deliverables are evaluated studies, a reproducible benchmark and a small web demo showing boxes, calibrated scores and miss warnings on public images. The demo is not the research contribution. Conclusions remain limited to four countries and box labels. We do not claim crack recovery, safety benefits or deployment readiness. Thank you.','Integration, deliverables, prototype and responsible-use limits, pp. 15-18, 24.','Demo stack: ONNX / FastAPI / React or Next.js, CPU inference, no new photo collection. CC BY-SA attribution and share-alike apply to released derived data. Literature and compute gates remain conditional.');
}
const seconds=slidesMeta.reduce((s,r)=>s+r.seconds,0);
if(seconds!==600 || slidesMeta.length!==15)throw new Error('Slide count or timing incorrect');
fs.writeFileSync(path.join(root,'tmp','slides-road-damage','deck-plan.json'),JSON.stringify(slidesMeta,null,2));
pptx.writeFile({fileName:path.join(out,'Road-Damage-Proposal.pptx')}).then(()=>console.log(`Wrote 15 slides; ${seconds} seconds; ${out}`));

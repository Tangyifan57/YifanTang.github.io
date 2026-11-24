from pathlib import Path
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,KeepTogether
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import yaml,html
r=Path(__file__).resolve().parents[1];out=r/'assets/files/Yifan_Tang_CV.pdf';out.parent.mkdir(parents=True,exist_ok=True)
for name,file in [('DejaVu','DejaVuSans.ttf'),('DejaVu-Bold','DejaVuSans-Bold.ttf')]:
 pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+file))
pdfmetrics.registerFontFamily('DejaVu',normal='DejaVu',bold='DejaVu-Bold',italic='DejaVu',boldItalic='DejaVu-Bold')
s=getSampleStyleSheet();s.add(ParagraphStyle(name='NameY',fontName='DejaVu-Bold',fontSize=23,leading=28,textColor=colors.HexColor('#07563f'),spaceAfter=8));s.add(ParagraphStyle(name='HeaderY',fontName='DejaVu-Bold',fontSize=12,leading=17,textColor=colors.HexColor('#07563f'),spaceBefore=14,spaceAfter=8,keepWithNext=True));s.add(ParagraphStyle(name='TextY',fontName='DejaVu',fontSize=9,leading=14,spaceAfter=7));s.add(ParagraphStyle(name='SmallY',fontName='DejaVu',fontSize=8,leading=12,spaceAfter=4))
flow=[]
def p(text,style='TextY'):
 paragraph=Paragraph(text,s[style])
 flow.append(paragraph if style=='HeaderY' else KeepTogether([paragraph]))
def h(text):p(text,'HeaderY')
p('Yifan Tang','NameY');p('Ph.D. Student · Energy and Power Engineering<br/>School of Advanced Energy, Sun Yat-sen University · Shenzhen, China')
p('<link href="mailto:tangyf57@mail2.sysu.edu.cn">tangyf57@mail2.sysu.edu.cn</link> · <link href="https://scholar.google.com/citations?user=ytSlTN0AAAAJ">Google Scholar</link>')
h('EDUCATION')
for e in yaml.safe_load((r/'_data/education.yml').read_text()):
 p(f'<b>{e["institution"]}</b> · {e["dates"]}<br/>{e["degree"]}<br/>{e["school"]} · Advisor(s): {e["advisors"]}')
h('WORK EXPERIENCE')
for e in yaml.safe_load((r/'_data/experience.yml').read_text()):
 p(f'<b>{html.escape(e["company"])}</b> · {html.escape(e["dates"])}<br/>{html.escape(e["role"])}<br/>{html.escape(e["responsibilities"])}')
h('RESEARCH EXPERIENCE')
p('<b>Prelithiation / Presodiation for High-Energy Batteries</b><br/>Sun Yat-sen University · Sep. 2025 – Present<br/>Developing cathode-side and anode-side lithium/sodium compensation strategies; regulating additive decomposition, ion transport, interphase formation, and electrode structural stability; integrating material chemistry with full-cell and pouch-cell validation.')
p('<b>MOF-Derived Sodium-Ion Anodes and Interfacial Chemistry</b><br/>Ningbo University · Sep. 2022 – Jun. 2025<br/>Designed MOF-derived composites, single-atom-regulated electrodes, and metal/2D-semiconductor heterostructures. Investigated sodium-storage mechanisms, phase evolution, interfacial charge transfer, and SEI chemistry using in-situ characterization and theoretical analysis.')
p('<b>Laser Additive Manufacturing of TiC-Reinforced CoCrNi Alloys</b><br/>University of South China · Sep. 2020 – Jun. 2022<br/>Investigated TiC effects on solidification microstructure, grain structure, precipitates, and forming defects in medium-entropy alloys.')
h('PEER-REVIEWED PUBLICATIONS')
for a in yaml.safe_load((r/'_data/publications.yml').read_text()):
 if a['status']!='published':continue
 authors=html.escape(a['authors']).replace('Y. Tang','<b>Y. Tang</b>')
 p(f'{authors}. {html.escape(a["title"])}. <b>{a["journal"]}</b> {a["volume"]}, {a["article"]} ({a["year"]}).<br/><link href="https://doi.org/{a["doi"]}">doi:{a["doi"]}</link> · {a["role"]}')
p('# Equal contribution. * Corresponding author.','SmallY')
h('MANUSCRIPT UNDER REVIEW')
for a in yaml.safe_load((r/'_data/publications.yml').read_text()):
 if a['status']=='under-review':p(f'{html.escape(a["authors"])}. {html.escape(a["title"])}. {a["journal"]} ({a["year"]}). <b>Under review.</b>')
h('CONFERENCES AND PRESENTATIONS')
p('<b>Oct. 2026 · Guangzhou:</b> Poster, 24th National Electrochemical Conference of the Chinese Chemical Society. Chalcogenide-anion presodiation additives for sodium compensation and cathode stabilization.')
p('<b>May 2025 · Nanjing:</b> Oral presentation, 9th National Conference on Structural Chemistry of the Chinese Chemical Society. MOF-derived sodium-ion anodes and storage mechanisms.')
p('<b>Apr. 2024 · Hangzhou:</b> Poster, 4th National Conference on Energy and Environmental Materials &amp; Summit Forum on New Materials and Carbon Neutrality. MOF-derived carbon composites for sodium storage.')
h('TECHNICAL SKILLS AND ADDITIONAL INFORMATION')
p('Origin; COMSOL; in-situ XRD and Raman; XAS; XPS; SEM; TEM; FTIR; in-situ DEMS; electrochemical testing (CV, EIS, DRT, GCD, GITT, PITT, LSV, CC–CV); MS Office; AI-assisted research and coding tools.')
p('Four invention patents (one granted, three pending). Languages: Chinese (native); English (conversational).')
p('Public web edition · Based on the CV supplied on 24 November 2026.','SmallY')
def footer(c,d):
 c.setFont('DejaVu',8);c.setFillColor(colors.HexColor('#68766f'));c.drawString(42,27,'Yifan Tang | Curriculum Vitae');c.drawRightString(A4[0]-42,27,str(d.page))
SimpleDocTemplate(str(out),pagesize=A4,rightMargin=42,leftMargin=42,topMargin=38,bottomMargin=42,title='Yifan Tang — Curriculum Vitae',author='Yifan Tang').build(flow,onFirstPage=footer,onLaterPages=footer)
print(out)

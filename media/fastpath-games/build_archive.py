"""Rebuild the PDF and Markdown: python build_archive.py (reportlab, Pillow)."""
from pathlib import Path
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.utils import ImageReader

ROOT = Path(__file__).resolve().parent
GAMES = [
('The Tornado', 'Collect-and-grow play across city streets, a beach, ice, and a rainbow road.', 'Existing local visual QA renders; these frames omit the native HUD. Rainbow Road is level 4 in the inspected 1.3.0 menu, not a separate fifth level.', [
('tornado/new-york-start.png','01 / New York','The city field contains blocks, cones, small objects, and the tornado.'),
('tornado/seaside-start.png','02 / The Seaside','A sandy field introduces beach objects and a warm palette.'),
('tornado/fire-ice-start.png','03 / Fire & Ice','The opening icy field shows flags and scattered collectible objects.'),
('tornado/rainbow-road-start.png','04 / Rainbow Road','Colored lanes and star shapes give the fourth adventure its visual identity.'),
('tornado/rainbow-road-finale.png','Rainbow Road / Finale','The existing finale render reads: A whole rainbow, tucked away. This is not evidence of a newly completed run.')]),
('The Courier: Wrong Door','Route packages through a small network to their matching destinations.','Existing local visual QA captures. File names identify scenarios; the images do not establish a newly completed session.',[
('courier/01-first-ten-seconds.png','Opening route','The network, package, destinations, and score are visible.'),
('courier/02-two-package-overlap.png','Package traffic','The QA scenario is named two-package-overlap; this frame records its network state.'),
('courier/03-stage-3-overdrive.png','Stage 3 / Overdrive','An escalation capture from the local QA collection, with route and score feedback.'),
('courier/04-successful-rescue.png','Rescue scenario','The QA capture is named successful-rescue. Its score and destination feedback are preserved.'),
('courier/05-shift-complete.png','Shift clear','The existing completion capture shows SHIFT CLEAR, a score, and AGAIN.')]),
('PUT THE MOON BACK','An orbital puzzle about moving the Moon while watching the consequences of each intervention.','Existing public visual portfolio, pages 2, 3, 4, 6, and 9. Portfolio framing is retained. A local mission was separately opened during the earlier review.',[
('put-the-moon-back/01-title.png','It Was Fine Where It Was','The title screen introduces the Moon and the game navigation.'),
('put-the-moon-back/02-gameplay.png','Orbital gameplay','Earth, the Moon, orbit guides, and control panels share the playfield. No mission number is inferred from this image.'),
('put-the-moon-back/03-mission-select.png','Mission selection','The campaign selection screen presents a collection of lunar problems.'),
('put-the-moon-back/04-seeded-challenges.png','Seeded challenges','The portfolio records the challenge selection interface.'),
('put-the-moon-back/05-history.png','Your Moon','The portfolio presents a persistent Moon profile: It remembers what you did to it. This is not a replay-verification result.')]),
('Grounded DI City - The Morning Line','A city-and-tram puzzle with route controls, junction progress, and a cargo ledger.','One existing public gameplay capture is available in this edition. The requested 3-5 images are not yet met for this game; no completed live run is claimed.',[
('grounded-di-city/01-the-morning-line-gameplay.png','Audit Blue / City route','The city view shows the tram, route choices, cargo ledger, and junction progress together.')]),
('Page Two','A storybook mystery set on Bellweather Island in summer 1985: find the glasses and follow the clues.','Four pages from the existing public v1.0 screenshot PDF. Added during publication audit; no runnable build was opened for this game.',[
('page-two/01-title.png','A Little Mystery Comes Into Focus','The title screen offers New Story, Settings, and Credits.'),
('page-two/02-settings.png','Comfort & Sound','Settings expose sound, reduced motion, reduced blur, high contrast, and text speed.'),
('page-two/03-credits.png','Credits / Version 1.0.0','The credits identify Grounded DI and describe the original family adventure.'),
('page-two/04-mailboat-cabin.png','Chapter One / Mailboat Cabin','Out of Focus introduces Listen, Touch, a notebook, and a gentle nudge.')])]

W,H=792,612
BG,FG,MUTED,ACCENT=map(HexColor,['#071326','#F5E8C5','#ABC1D5','#7DE3D1'])
def text(c,s,x,y,size=11,width=704,color=FG,font='Helvetica'):
    c.setFont(font,size); c.setFillColor(color)
    for para in s.split('\n'):
        line=''
        for word in para.split():
            candidate=(line+' '+word).strip()
            if stringWidth(candidate,font,size)>width and line:
                c.drawString(x,y,line); y-=size*1.4; line=word
            else: line=candidate
        c.drawString(x,y,line); y-=size*1.4
    return y
def page(c,n,section):
    c.setFillColor(BG); c.rect(0,0,W,H,fill=1,stroke=0)
    text(c,section.upper(),44,568,9,color=ACCENT)
    text(c,'GROUNDED DI LLC / VISUAL ARCHIVE / 2026-10-01',44,25,8,color=MUTED)
    text(c,str(n).zfill(2),728,25,8,color=MUTED)
def photo(c,path):
    with Image.open(path) as im: w,h=im.size
    scale=min(704/w,375/h); dw,dh=w*scale,h*scale
    c.drawImage(ImageReader(str(path)),44+(704-dw)/2,131+(375-dh)/2,dw,dh,mask='auto')
def build():
    c=canvas.Canvas(str(ROOT/'fastpath-games-visual-archive.pdf'),pagesize=(W,H),invariant=1)
    c.setTitle('FastPath Games - A Visual Archive'); c.setAuthor('Grounded DI LLC')
    page(c,1,'Grounded DI LLC / Game collection')
    text(c,'FastPath Games',44,464,40,font='Helvetica-Bold')
    text(c,'A Visual Archive',44,417,29,color=ACCENT)
    text(c,'Storms, packages, orbital repairs, a city route, and an island mystery.',44,338,17,width=620)
    text(c,'5 games / 20 distinct images / audited publication edition',44,227,13)
    text(c,'A collection of existing game renders, QA captures, and public portfolio pages. Published as visual history with image provenance and coverage limits.',44,177,12,width=630,color=MUTED)
    c.showPage(); page(c,2,'Introduction / Contents')
    text(c,'A record of the games',44,529,28,font='Helvetica-Bold')
    y=text(c,'This book archives five games represented in local project material and the Grounded DI Desktop Builds repository. Images are preserved as found; no game artwork was generated for this edition.',44,476,12)
    start=3
    for title,desc,provenance,shots in GAMES:
        y-=25; text(c,f'{start:02d}  {title}',44,y,13,color=ACCENT,font='Helvetica-Bold')
        y=text(c,desc,65,y-20,10.5,width=660,color=MUTED); start+=len(shots)
    text(c,'Each image appears once. Source types and incomplete coverage are identified on the image pages and in the accompanying README.',44,77,10,color=MUTED)
    c.showPage(); n=3
    md=['# FastPath Games - A Visual Archive','','Grounded DI LLC | Audited publication edition | 2026-10-01','','Five games, twenty distinct images. Existing QA renders and portfolio captures; these are not newly saved screenshots from live play.','']
    for title,desc,provenance,shots in GAMES:
        md.extend(['## '+title,'',desc,'','**Source and coverage:** '+provenance,''])
        for file,label,caption in shots:
            page(c,n,title); text(c,label,44,531,24,font='Helvetica-Bold')
            photo(c,ROOT/'screenshots'/file)
            y=text(c,caption,44,110,10.5)
            text(c,provenance,44,min(76,y-8),8.5,color=MUTED)
            md.extend(['### '+label,'',caption,'',f'![{label}](screenshots/{file})',''])
            c.showPage(); n+=1
    page(c,n,'Closing inventory / Coverage')
    text(c,'Five games, with room to grow',44,528,28,font='Helvetica-Bold'); y=469
    for title,desc,provenance,shots in GAMES:
        y=text(c,f'{title} / {len(shots)} images',44,y,14,color=ACCENT,font='Helvetica-Bold')-12
    text(c,'Tornado coverage includes four levels and a Rainbow Road finale. The Morning Line has one image, so this edition does not meet the original 3-5-image target for every game.',44,250,12)
    text(c,'Galaxy Chess Explorer: Strategy Quest remains a discovery lead: a local safety document was found, but no runnable build was located. It is not counted among the five illustrated games.',44,178,11,color=MUTED)
    text(c,'The archive is a bounded collection of identified material, not a claim that every game or level has been found or completed. See README.md for sources and audit notes.',44,107,11,color=MUTED)
    c.save()
    md.extend(['## Coverage limits','','The Morning Line has one image. Galaxy Chess Explorer: Strategy Quest was named in a local safety document, but no runnable build was located. This is a bounded archive, not an exhaustive inventory or a claim of completed live play.',''])
    (ROOT/'fastpath-games-visual-archive.md').write_text('\n'.join(md),encoding='utf-8')
    print(f'Built {n} pages')
if __name__=='__main__': build()

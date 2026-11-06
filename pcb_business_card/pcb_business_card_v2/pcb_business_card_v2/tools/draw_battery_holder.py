#!/usr/bin/env python3
"""Dimensioned SVG derived from the same reference outline as the footprint."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
edges=json.loads(Path(__file__).with_name('bigfoot_outline.json').read_text())['edges']
remaining=edges.copy(); ordered=[remaining.pop(0)]
while remaining:
    end=ordered[-1]['end']
    for i,e in enumerate(remaining):
        if e['start']==end or e['end']==end:
            e=remaining.pop(i).copy()
            if e['end']==end:e['start'],e['end']=e['end'],e['start']
            ordered.append(e);break
    else:raise ValueError('Open reference contour')
assert ordered[-1]['end']==ordered[0]['start']
path=f'M {ordered[0]["start"][0]+3.5} {ordered[0]["start"][1]}'
for e in ordered:
    x,y=e['end'];x+=3.5
    if e['type']=='line':path+=f' L{x} {y}'
    else:
        a,m,b=e['start'],e['mid'],e['end']
        cross=(m[0]-a[0])*(b[1]-m[1])-(m[1]-a[1])*(b[0]-m[0])
        path+=f' A1 1 0 0 {int(cross>0)} {x} {y}'
path+=' Z'
out=['''<svg xmlns="http://www.w3.org/2000/svg" width="1500" height="980" viewBox="0 0 1500 980">
<defs><marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="#334155"/></marker></defs>
<rect width="1500" height="980" fill="#f8fafc"/>
<g font-family="DejaVu Sans, sans-serif" fill="#172b3a">
<text x="55" y="55" font-size="32" font-weight="bold">CR2032 PCB spring holder</text>
<text x="55" y="90" font-size="18">0.8 mm FR-4 · right entry · positive face toward the component side</text>
<text x="55" y="122" font-size="17" fill="#a34c12">PROTOTYPE A — frequent-removal durability requires physical testing</text>
<text x="55" y="166" font-size="21" font-weight="bold">Card placement · front view</text>
<text x="855" y="166" font-size="21" font-weight="bold">Holder detail · both copper faces overlaid</text>
''']
def line(x1,y1,x2,y2,style=''):
    out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#334155" stroke-width="1.4" {style}/>')
def label(x,y,s,size=17,anchor='middle'):
    out.append(f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}">{s}</text>')
def holder(s,ox,oy,small=False):
    out.append(f'<g transform="translate({ox} {oy}) scale({s})">')
    out.append(f'<path d="{path}" fill="#f8fafc" stroke="#162f28" stroke-width="0.08"/>')
    out.append('<path d="M-15 0 H-4" fill="none" stroke="#4c88be" stroke-width="0.4" opacity="0.65"/>')
    out.append('<path d="M0 -6.5 H11.025 V6.5 H0 M0 -6.5 H-11.025 M0 6.5 H-11.025" fill="none" stroke="#ae7951" stroke-width="1" opacity="0.7"/>')
    out.append('<path d="M-8.5 -1.45 H1.835 L2.95 -0.706 V0.706 L1.835 1.45 H-8.5 Z" fill="#72b7ed"/>')
    out.append('<path d="M0 -5.05 L-7.335 -5.05 L-8.45 -5.794 V-7.206 L-7.335 -7.95 H0 Z" fill="#f3c667"/>')
    out.append('<path d="M0 5.05 L-7.335 5.05 L-8.45 5.794 V7.206 L-7.335 7.95 H0 Z" fill="#f3c667"/>')
    out.append('<circle cx="0" cy="0" r="10" fill="none" stroke="#cfdeed" stroke-width="0.12" stroke-dasharray="0.55 0.4"/>')
    out.append('<path d="M-0.5 0 H0.5 M0 -0.5 V0.5" stroke="#ffffff" stroke-width="0.1"/>')
    if not small:
        out.append('<g font-size="0.9" fill="#172b3a" text-anchor="middle"><text x="-4" y="0.3">1 · + · B.Cu</text><text x="0" y="-5.3">2 · −</text><text x="0" y="5.9">2 · −</text></g>')
    out.append('</g>')
# Card.
sx=8;bx=55;by=210
out.append(f'<rect x="{bx}" y="{by}" width="{85.6*sx}" height="{53.98*sx}" rx="24" fill="#17684e" stroke="#124632" stroke-width="2"/>')
holder(sx,bx+71.35*sx,by+14.25*sx,True)
line(bx,by+53.98*sx+26,bx+85.6*sx,by+53.98*sx+26,'marker-start="url(#arrow)" marker-end="url(#arrow)"')
label(bx+42.8*sx,by+53.98*sx+52,'85.60 mm')
label(bx+42.8*sx,by+53.98*sx+80,'53.98 mm high · R3 corners · 0.80 mm thick')
label(bx+42.8*sx,by+53.98*sx+108,'Cell centre: 71.35 mm right, 14.25 mm down from top-left',16)
# Enlarged portion including the exact right support bridge.
ds=18;dx=1130;dy=420
out.append(f'<rect x="{dx-17*ds}" y="{dy-12*ds}" width="{31.25*ds}" height="{25*ds}" fill="#17684e" stroke="#124632" stroke-width="1"/>')
holder(ds,dx,dy)
for x in [-14,10]:line(dx+x*ds,dy-10.5*ds,dx+x*ds,dy-13.1*ds)
line(dx-14*ds,dy-12.8*ds,dx+10*ds,dy-12.8*ds,'marker-start="url(#arrow)" marker-end="url(#arrow)"')
label(dx-2*ds,dy-13.1*ds,'24.00 mm',16)
line(dx-15.7*ds,dy-10.5*ds,dx-15.7*ds,dy+10.5*ds,'marker-start="url(#arrow)" marker-end="url(#arrow)"')
out.append(f'<text transform="translate({dx-16.1*ds} {dy}) rotate(-90)" font-size="16" text-anchor="middle" fill="#fff">21.00 mm</text>')
line(dx+10*ds,dy+14.4*ds,dx+14.25*ds,dy+14.4*ds,'marker-start="url(#arrow)" marker-end="url(#arrow)"')
label(dx+12.125*ds,dy+15.7*ds,'4.25 mm',16)
label(dx+12.125*ds,dy+16.9*ds,'support bridge',15)
line(1460,420,1398,420,'marker-end="url(#arrow)"')
label(1438,388,'Insert',16)
label(1438,405,'from right',14)
label(1090,682,'Dashed circle: nominal Ø20 mm cell',16)
out.append('''<rect x="55" y="790" width="1390" height="145" rx="12" fill="#e6edf3"/>
<text x="75" y="824" font-size="19" font-weight="bold">Contact arrangement</text>
<text x="75" y="855" font-size="17">Blue: pad 1, underside of centre arm, contacting the cell’s positive face.</text>
<text x="75" y="883" font-size="17">Gold: pad 2, upper surfaces of the two lower arms, contacting the negative face.</text>
<text x="75" y="911" font-size="16">Coloured thin paths are masked copper. White areas are routed out. No solder paste on contacts.</text>
<text x="55" y="960" font-size="14">Mechanical outline: Dennis Kaandorp / Bigfoot Creations. Contact adaptation: project prototype. Dimensions in mm; drawing not to print scale.</text>
</g></svg>''')
target=ROOT/'docs'/'battery-holder-dimensions.svg'
target.write_text('\n'.join(out))
print(target)

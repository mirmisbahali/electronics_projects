#!/usr/bin/env python3
"""Generate the project CR2032 footprint. Does not change the schematic or PCB.

Mechanical outline: Dennis Kaandorp / Bigfoot Creations, see bigfoot_outline.json.
Units: mm. Origin: nominal cell centre. Front is the component/+ face.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME = 'CR2032_PCB_Spring_Bigfoot_0.8mm_RightEntry'
LIB = 'BusinessCard'

def generate():
    outline = json.loads((Path(__file__).with_name('bigfoot_outline.json')).read_text())
    out = [f'''(footprint "{NAME}"
  (version 20260206)
  (generator "battery_holder_generator")
  (layer "F.Cu")
  (descr "Prototype CR2032 PCB spring holder; Bigfoot outline; 0.8mm FR4; + face front; right entry over retained bridge. No paste. Frequent removal requires physical validation.")
  (tags "CR2032 battery spring PCB cutout 0.8mm Bigfoot")
  (attr smd exclude_from_pos_files exclude_from_bom)
  (fp_text reference "REF**" (at -6 -12.2) (layer "F.SilkS")
    (effects (font (size 1 1) (thickness 0.15))))
  (fp_text value "{NAME}" (at -2 13.2) (layer "F.Fab") hide
    (effects (font (size 0.8 0.8) (thickness 0.12))))
  (fp_text user "CR2032 + UP" (at -5 0) (layer "F.SilkS")
    (effects (font (size 0.9 0.9) (thickness 0.14))))
  (fp_text user "0.8mm PCB" (at -5 12.1) (layer "F.SilkS")
    (effects (font (size 0.8 0.8) (thickness 0.12))))
  (fp_circle (center 0 0) (end 10 0) (stroke (width 0.1) (type dash))
    (fill none) (layer "F.Fab"))
  (fp_text user "CELL CENTRE / PROTOTYPE" (at 0 -14) (layer "Dwgs.User")
    (effects (font (size 0.8 0.8) (thickness 0.12))))
  (fp_text user "RIGHT ENTRY" (at 5 12.1) (layer "F.Fab")
    (effects (font (size 0.8 0.8) (thickness 0.12))))
''']
    for e in outline['edges']:
        pts = ' '.join(f'({key} {e[key][0]+3.5:.6f} {e[key][1]:.6f})'
                       for key in ('start','mid','end') if key in e)
        out.append(f'  (fp_{e["type"]} {pts} (stroke (width 0.05) (type default)) (layer "Edge.Cuts"))\n')
    # Courtyard reserves the springs, cell and masked routing tails on BOTH faces.
    for layer in ('F.CrtYd','B.CrtYd'):
        out.append(f'  (fp_rect (start -16 -11.25) (end 12.25 11.25) (stroke (width 0.05) (type default)) (fill none) (layer "{layer}"))\n')
    # Contact edges follow the Edge.Cuts bevels, offset 0.55 mm into FR-4.
    # This leaves at least 0.5 mm after KiCad accounts for the 0.05 mm cut stroke.
    # The + contact is on the underside of the centre arm. The two - contacts
    # are same-net custom pads on the upper surfaces of the outer arms.
    out.append('''  (pad "1" smd custom (at -4 0) (size 1 1)
    (layers "B.Cu" "B.Mask") (solder_mask_margin 0)
    (options (clearance outline) (anchor rect))
    (primitives (gr_poly (pts (xy -4.5 -1.45) (xy 5.835 -1.45)
      (xy 6.95 -0.7063) (xy 6.95 0.7063) (xy 5.835 1.45)
      (xy -4.5 1.45))
      (width 0) (fill yes))))
  (pad "1" smd custom (at -15 0) (size 0.4 0.4) (layers "B.Cu")
    (options (clearance outline) (anchor rect))
    (primitives (gr_line (start 0 0) (end 11 0) (width 1))))
  (pad "2" smd custom (at -4.225 -6.5) (size 1 1)
    (layers "F.Cu" "F.Mask") (solder_mask_margin 0)
    (options (clearance outline) (anchor rect))
    (primitives (gr_poly (pts (xy 4.225 1.45) (xy -3.11 1.45)
      (xy -4.225 0.706) (xy -4.225 -0.706) (xy -3.11 -1.45)
      (xy 4.225 -1.45)) (width 0) (fill yes))))
  (pad "2" smd custom (at -4.225 6.5) (size 1 1)
    (layers "F.Cu" "F.Mask") (solder_mask_margin 0)
    (options (clearance outline) (anchor rect))
    (primitives (gr_poly (pts (xy 4.225 -1.45) (xy -3.11 -1.45)
      (xy -4.225 -0.706) (xy -4.225 0.706) (xy -3.11 1.45)
      (xy 4.225 1.45)) (width 0) (fill yes))))
  (pad "2" smd custom (at 11.025 0) (size 1 1) (layers "F.Cu")
    (options (clearance outline) (anchor rect))
    (primitives
      (gr_line (start 0 -6.5) (end 0 6.5) (width 1))
      (gr_line (start 0 -6.5) (end -11.025 -6.5) (width 1))
      (gr_line (start 0 6.5) (end -11.025 6.5) (width 1))))
  (zone (net 0) (net_name "") (layers "F.Cu" "B.Cu")
    (name "CR2032_SPRINGS_NO_FILL_OR_VIAS")
    (hatch edge 0.5) (connect_pads (clearance 0)) (min_thickness 0.25)
    (keepout (tracks allowed) (vias not_allowed) (pads allowed)
      (copperpour not_allowed) (footprints not_allowed))
    (fill (thermal_gap 0.3) (thermal_bridge_width 0.3))
    (polygon (pts (xy -16 -11.25) (xy 12.25 -11.25)
      (xy 12.25 11.25) (xy -16 11.25))))
)\n''')
    lib = ROOT / f'{LIB}.pretty'
    lib.mkdir(exist_ok=True)
    target = lib / f'{NAME}.kicad_mod'
    target.write_text(''.join(out))
    print(target)


if __name__ == '__main__':
    generate()

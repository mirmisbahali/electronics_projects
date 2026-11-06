# CR2032 spring holder — prototype revision A

This is a PCB-integrated holder for the CR2032, with the battery's positive face
toward the front/component side. Insert from the right, over the retained support
bridge and underneath the centre arm. The two outer arms pass underneath the cell.
The user selected 0.8 mm PCB thickness, JLCPCB, upper-right placement, and frequent
removal. The original Bigfoot mechanical outline is preserved, with new contact
geometry, masked connections, markings, and keepouts.

**Status: electrically/layout checked; physical retention, insertion shorts, and
repeated-insertion durability are not yet validated.** There is no established
insertion-cycle rating for this footprint. Frequent removal must be qualified on
fabricated samples; it is not established merely by passing KiCad DRC.

## Open and use

- Footprint: `BusinessCard:CR2032_PCB_Spring_Bigfoot_0.8mm_RightEntry`.
- Library: `../BusinessCard.pretty`, registered in the project `fp-lib-table`
  through `${KIPRJMOD}`. No global library installation is required.
- BT1 in the main schematic is assigned to this footprint.
- The main PCB now contains the card outline and BT1. Other schematic components
  still need to be imported and laid out with **Update PCB from Schematic (F8)**.
- The original schematic, empty PCB, and project settings were backed up under
  `../backups/before_battery_holder/` before editing.
- If the project was already open during these edits, close the affected editors
  **without saving their old in-memory copies**, then reopen the project.

The `.kicad_pro` file remains the project entry point. Footprint geometry resides
in the `.kicad_mod`, its assignment in the schematic, and physical placement and
board thickness in the `.kicad_pcb`.

## Dimensions and placement

| Item | Value |
|---|---|
| Card outline | 85.60 × 53.98 mm, corner radius 3.00 mm |
| PCB thickness | 0.80 mm; two copper layers |
| Nominal cell envelope | Ø20.0 × 3.2 mm; untabbed CR2032 |
| Footprint origin | Nominal seated cell centre |
| Initial centre from card upper-left | X = 71.35 mm; Y = 14.25 mm |
| Cutout bounding box relative to origin | X −14.00…+10.00; Y −10.50…+10.50 mm |
| Cutout overall extent | 24.00 × 21.00 mm |
| Cutout top margin to card top | 3.75 mm |
| Right support bridge beyond cutout | 4.25 mm |
| Narrowest straight routed channel | 2.00 mm |
| Root/end circular fillets in reference | Radius 1.00 mm |
| Nominal straight arm width | 4.00 mm |
| Copper-to-cutout design minimum | 0.50 mm |
| Courtyard / keepout rectangle | X −16…+12.25; Y −11.25…+11.25 mm |

The top and right margins are retained from the original board, adapting its
outline to the requested credit-card dimensions. R3 corners also match that
source board. The position is editable, but preserve the right support bridge and
clearance to the top edge. Do not merge the internal cutout with the card outline.

The article describes 19 × 4 mm tabs. The downloaded geometry is the more precise
reference: the two outer tips span 19 mm to the rightmost root boundary; the centre
tip spans 17.5 mm from the leftmost cutout boundary. Root fillets affect effective
flex length. No attempt was made to replace these shapes with three identical
19 mm cantilevers. All 30 source outline primitives are preserved with an X-only
translation of +3.5 mm to the new origin.

The nominal cell position is a placement guide, not a latch or hard stop. A cell
can shift in a friction holder. Check the actual purchased cell's terminal drawing,
diameter, height, and gasket geometry before releasing the design.

## Electrical contacts and layout

| Pad | Net | Contact location | Connection point |
|---|---|---|---|
| 1 | `+BATT` | Centre arm, **B.Cu/B.Mask**, chamfered custom pad | Masked B.Cu tail at (−15, 0) |
| 2 | `GND` | Two **numbered custom pads**, **F.Cu/F.Mask**, chamfered to echo the Edge.Cuts | Masked F.Cu spine at (+11.025, 0) |

The layer choice is intentional: the centre arm is above the installed cell, so
its underside contacts the upward-facing positive terminal. The outer arms are
below the cell, so their upper surfaces contact the negative terminal.
The positive opening reaches to 0.55 mm behind the centre-arm tip to avoid leaving
a long masked tip ahead of the contact; physical contact pressure still needs testing.

The two negative contacts are already joined by 1.0 mm masked copper around the
right support bridge. The positive contact has a 1.0 mm masked tail into the
left support. Route from these connection points; no vias through flexing arms
are needed. Connection tails are pads without mask openings, not solder points.

The contact pads follow the nearby Edge.Cuts bevel angles but sit 0.55 mm into
the FR-4 from the cutout outline. The board's 0.5 mm copper-edge rule is the
controlling minimum; keep this offset when editing the pad contours. This avoids
the copper approaching the CNC cutout or being clipped by routing tolerances.
This clearance is not proof of safe contact throughout insertion, removal,
misalignment, or use with every CR2032 brand. In particular, the positive can/rim
must never be bridged to the negative terminal.

All contacts omit F.Paste/B.Paste. Do not stencil or tin them. The keepout on both
copper faces excludes copper pours, vias, and other footprints. Tracks and pads
remain allowed so the battery can be routed: manually keep unrelated tracks and
exposed copper out of the reserved area. Do not put components or silkscreen on
the rubbing contact surfaces. The positive label is on the non-contact face of
the centre arm.

The footprint is excluded from placement files and PCB BOM because the retaining
structure is fabricated with the board. The schematic's CR2032 cell remains a BOM
item. Tell the assembler not to populate a separate holder at BT1.

## JLCPCB fabrication

- Order **0.8 mm FR-4**, not the default 1.6 mm. The source board file itself says
  1.6 mm, whereas its author's build description explicitly says 0.8 mm. This
  project follows the user's confirmed 0.8 mm and the author's fabricated build.
- Recommended prototype finish: **ENIG** for flat pressure contacts. The footprint
  does not itself select a fabrication-order finish. JLCPCB's ENIG is not
  electroplated hard gold and does not establish long-term rubbing durability.
- The closed internal `Edge.Cuts` loop is an **unplated routed cutout**, not a
  V-score, plated slot, edge-plating request, or castellated-hole feature.
- JLCPCB currently lists 1.0 mm minimum non-plated slot width, ±0.2 mm non-plated
  slot tolerance, and ≥0.2 mm routed-edge copper clearance. This design uses a
  2.0 mm minimum straight channel and ≥0.5 mm copper clearance.
- For boards below 1.0 mm, JLCPCB lists ±0.1 mm thickness tolerance. The resulting
  0.7–0.9 mm range matters to spring force and must be sampled in physical testing.
- Keep tooling tabs, panel rails, and breakaway features away from the spring
  arms and insertion path. Ask CAM to preserve the closed cutout and support
  bridges rather than simplifying them.

## Prototype checks before frequent use

1. Inspect milled edges and pads for burrs, copper exposure at edges, delamination,
   solder deposits, and scratches. Measure PCB thickness and cutout dimensions.
2. With no cell installed, verify pad 1 is isolated from pad 2; both negative
   openings must have continuity to each other and to the GND connection point.
3. Check the insertion/removal contact sequence with a mechanically representative
   test cell/fixture and a current-limited supply before using a real lithium cell.
   Confirm there is no positive-can-to-negative short at any point in the motion.
   Do not treat an MCU reset or supply limiter trip as acceptable contact behaviour.
4. Verify seating, retention, polarity, and voltage drop at the intended maximum
   load. Test movement and light bending while monitoring for contact interruptions.
5. Define the required lifetime in insertion/removal cycles. Cycle several samples
   from the actual PCB finish/thickness and cell supplier; record contact voltage
   drop, retention, spring set, copper/finish wear, and root cracking. Check early
   cycles and regular intervals rather than inspecting only the final state.
6. If repeated removal produces wear, shorts, intermittent power, or loosening,
   revise the mechanism or use a spring-metal holder with an appropriate rating.
   ENIG and FR-4 spring arms alone provide no defensible cycle-life guarantee.

## Validation performed

- Loaded and rendered with **KiCad 10.0.7**.
- Native PCB DRC: **0 violations; 0 unconnected items** with this project's existing
  0.5 mm minimum copper-edge clearance. Report: `battery-holder-drc.json`.
- Checked BT1 pad mapping against the schematic netlist: 1 = +BATT, 2 = GND.
- Schematic edit is limited to BT1's footprint field.
- This DRC result applies to the outline and holder only. The rest of the circuit
  is not on the PCB yet; full schematic parity/routing and physical durability
  are outside the checks completed here.
- `battery-holder-board-top.png` and `battery-holder-board-bottom.png`: native
  KiCad renders of the unloaded board, showing the two contact faces.
- `battery-holder-dimensions.svg`: dimensioned drawing, viewed from the front;
  opposite-face contacts are overlaid for explanation.
- `battery-holder-kicad.svg`: native KiCad layer export.

Regenerate only the library footprint with:

```sh
python3 tools/generate_battery_holder.py
```

After regeneration, use **Update Footprints from Library** in PCB Editor to update
the placed instance. The generator does not overwrite the board or schematic.

## Sources and provenance

- Dennis Kaandorp / Bigfoot Creations, [PCB business card](https://bigfootcreations.wordpress.com/2022/12/31/pcb-business-card/),
  published December 31, 2022. Mechanical outline adapted from the author's
  [downloaded PCB](https://drive.google.com/file/d/1-0pnOduwlwVwwKG0UaxshtP1D-_LR8Du/view),
  footprint `custom_parts:CR2032_PCBcutout`. Source hash and original outline
  coordinates are retained in `../tools/bigfoot_outline.json`.
- [JLCPCB rigid PCB capabilities](https://jlcpcb.com/capabilities/pcb-capabilities/),
  accessed November 6, 2026.
- [JLCPCB discussion of hard gold and ENIG availability](https://jlcpcb.com/blog/hard-gold-pcb-finish),
  accessed November 6, 2026.
- [Panasonic CR2032 mechanical reference](https://energy.panasonic.com/dam/master/pdf/en/datasheet/lithium/CR2032_Datasheet_EN_240701.pdf).
  Used as a dimensional reference, not a user-selected battery supplier.
- Jeremy S. Cook's [experience adapting PCB spring holders](https://embeddedcomputing.com/technology/analog-and-power/pcbs-components/pcb-coin-cell-battery-holder-and-switch)
  documents intermittent contact after changing the arm geometry.

The reference's published prototype experience is not a mechanical qualification
of this adaptation. Attribution is preserved; no new licence is asserted over
the original geometry.

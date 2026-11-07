# SWD programming contacts

J1 is a bare PCB contact array for a 2 × 6 pogo probe, with an assumed 1.27 mm pitch in both directions. Viewed onto the PCB contact face with pin 1 at the upper left:

| Pin | Signal | Pin | Signal |
| --- | --- | --- | --- |
| 1 | +3V0 / target voltage | 2 | SWCLK (PA14) |
| 3 | GND | 4 | SWDIO (PA13) |
| 5 | NRST | 6 | GND |
| 7 | Unconnected | 8 | Unconnected |
| 9 | Unconnected | 10 | Unconnected |
| 11 | Unconnected | 12 | Unconnected |

This is a custom pinout: pin 6 is ground, not SWO. Wire the probe by signal name; do not assume another 6-pin adapter has the same pinout. The +3V0 contact is the MCU supply rail and the voltage reference for an ST-LINK with a target-voltage input. Power the target separately, with the board switched on; do not connect a programmer power output to an installed coin cell.

For an original ST-LINK/V2 20-pin connector, connect VAPP (pin 1 or 2) to J1 pin 1, SWCLK (9) to J1 pin 2, ground to J1 pin 3 or 6, SWDIO (7) to J1 pin 4, and NRST (15) to J1 pin 5. Check the markings and documentation for other ST-LINK/V2 versions or clones. NRST supports connect-under-reset.

The footprint uses six 1.0 mm diameter exposed copper pads, no paste, and a pin-1 silk mark. Confirm the actual probe's row spacing, pitch, pin tip size, numbering, alignment and clearance against its mechanical drawing before PCB layout or fabrication. The footprint does not provide mechanical alignment or retention. Choose a suitable finish and place it where the pogo fixture can make reliable contact.

This addition exists in the schematic and footprint library only. Update the PCB from the schematic, place and route J1, and run the board's design rules before fabrication.

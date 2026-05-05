import pcbnew
import re

board = pcbnew.GetBoard()

# ── Configuration ──────────────────────────────────────────────────
GRID_COLS   = 12     # columns in the main display grid
GRID_ROWS   = 8      # rows    in the main display grid  (12×8 = 96 LEDs)
PITCH_X     = 3.8    # mm  horizontal center-to-center pitch
PITCH_Y     = 3.0    # mm  vertical   center-to-center pitch
ORIGIN_X    = 50.0   # mm  X of the top-left LED in the main grid
ORIGIN_Y    = 30.0   # mm  Y of the top-left LED in the main grid
# Remaining 14 LEDs go in a single row 3 row-pitches below the main grid
LEFTOVER_X  = ORIGIN_X
LEFTOVER_Y  = ORIGIN_Y + (GRID_ROWS + 3) * PITCH_Y
# ───────────────────────────────────────────────────────────────────

LED_RE = re.compile(r'^D(\d+),(\d+)$')

leds = []
for fp in board.GetFootprints():
    m = LED_RE.match(fp.GetReference())
    if m:
        leds.append((int(m.group(1)), int(m.group(2)), fp))

leds.sort()   # sort by (schematic_row, schematic_col)
print(f"Found {len(leds)} LEDs total")

grid_total = GRID_ROWS * GRID_COLS   # 96

# Place main 12×8 grid (sequential, row-major)
for idx, (_, __, fp) in enumerate(leds[:grid_total]):
    col = idx % GRID_COLS
    row = idx // GRID_COLS
    fp.SetPosition(pcbnew.VECTOR2I(
        pcbnew.FromMM(ORIGIN_X + col * PITCH_X),
        pcbnew.FromMM(ORIGIN_Y + row * PITCH_Y),
    ))

# Place remaining LEDs in a single row below
for idx, (_, __, fp) in enumerate(leds[grid_total:]):
    fp.SetPosition(pcbnew.VECTOR2I(
        pcbnew.FromMM(LEFTOVER_X + idx * PITCH_X),
        pcbnew.FromMM(LEFTOVER_Y),
    ))

pcbnew.Refresh()
print(f"  Main grid : {min(grid_total, len(leds))} LEDs in {GRID_ROWS}×{GRID_COLS} layout")
print(f"  Leftover  : {max(0, len(leds) - grid_total)} LEDs in a row below")
print("Done — undo with Ctrl+Z if you need to tweak parameters.")

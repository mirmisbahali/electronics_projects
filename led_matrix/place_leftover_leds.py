import pcbnew
import re

board = pcbnew.GetBoard()

# ── Configuration — match these to your main grid script ───────────
PITCH_X       = 3.8    # mm  same horizontal pitch as main grid
PITCH_Y       = 3.0    # mm  same vertical pitch as main grid
LEFTOVER_COLS = 1      # single column
ORIGIN_X      = 50.0   # mm  X of the first leftover LED — adjust to taste
ORIGIN_Y      = 62.0   # mm  Y of the first leftover LED — adjust to taste
# ───────────────────────────────────────────────────────────────────

LED_RE = re.compile(r'^D(\d+),(\d+)$')

# Collect only the leftover LEDs: row 10 col>=7 and all of row 11 col<=10
leds = []
for fp in board.GetFootprints():
    m = LED_RE.match(fp.GetReference())
    if not m:
        continue
    r, c = int(m.group(1)), int(m.group(2))
    if (r == 10 and c >= 7) or (r == 11 and c <= 10):
        leds.append((r, c, fp))

leds.sort()
print(f"Found {len(leds)} leftover LEDs")

# Place in a 2D grid with same pitch as main grid
for idx, (r, c, fp) in enumerate(leds):
    grid_col = idx % LEFTOVER_COLS
    grid_row = idx // LEFTOVER_COLS
    fp.SetPosition(pcbnew.VECTOR2I(
        pcbnew.FromMM(ORIGIN_X + grid_col * PITCH_X),
        pcbnew.FromMM(ORIGIN_Y + grid_row * PITCH_Y),
    ))
    print(f"  D{r},{c} → col={grid_col} row={grid_row}")

pcbnew.Refresh()
print("Done — Ctrl+Z to undo.")

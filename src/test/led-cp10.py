import board
import displayio
from adafruit_display_text import label
import terminalio

# grab the built-in display
display = board.DISPLAY

# make a group that’s offset (x=10,y=20) and scaled 2×
group = displayio.Group(scale=2, x=10, y=20)
display.root_group = group

# create your label (only font, text, color here)
heybub = label.Label(
    terminalio.FONT,
    text="bubby 2",
    color=0xFF00FF
)
# append it into your pre-scaled group
group.append(heybub)

while True:
    pass

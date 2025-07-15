import board, busio, displayio
from fourwire import FourWire
from adafruit_st7735r import ST7735R
from adafruit_display_text import label
import terminalio

# Take over the built-in SPI display
displayio.release_displays()
spi     = busio.SPI(board.LCD_CLK, board.LCD_DIN)
bus     = FourWire(spi, command=board.LCD_DC, chip_select=board.LCD_CS, reset=board.LCD_RST)
display = ST7735R(
    bus,
    width=160, height=80,
    rowstart=1, colstart=26,
    rotation=270,
    invert=True
)

# Create root group and assign
splash = displayio.Group()
display.root_group = splash

# Create a 4× scaled label and add it
text_group = displayio.Group(scale=2, x=10, y=20)
text_area  = label.Label(terminalio.FONT, text="bubby 2", color=0xFF00FF)
text_group.append(text_area)
splash.append(text_group)

while True:
    pass

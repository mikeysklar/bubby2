# code.py

import time
import board
import digitalio

# Map SW0 → GP15, SW1 → GP10, SW2 → GP9, SW3 → GP4, SW4 → GP14
PINS = [
    board.GP15,  # SW0
    board.GP10,  # SW1
    board.GP9,   # SW2
    board.GP4,   # SW3
    board.GP14,  # SW4
]

# Set up each pin as a pulled-up input
buttons = []
for i, pin in enumerate(PINS):
    b = digitalio.DigitalInOut(pin)
    b.direction = digitalio.Direction.INPUT
    b.pull = digitalio.Pull.UP
    buttons.append((f"SW{i}", b))

print("Button tester running. Press and hold any switch…")
while True:
    for name, b in buttons:
        if not b.value:               # reads LOW when pressed
            print(f"{name} pressed")
            time.sleep(0.2)           # debounce hold
    time.sleep(0.01)

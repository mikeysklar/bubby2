# code.py

import time
import board
import digitalio

# Only test SW0 → GP15, SW3 → GP4, SW4 → GP14
TEST_PINS = [
    ("SW0", board.GP15),
    ("SW3", board.GP4),
    ("SW4", board.GP14),
]

buttons = []
for name, pin in TEST_PINS:
    b = digitalio.DigitalInOut(pin)
    b.direction = digitalio.Direction.INPUT
    b.pull = digitalio.Pull.UP
    buttons.append((name, b))

print("Partial tester (SW0, SW3, SW4). Press & hold any of these switches…")
while True:
    for name, b in buttons:
        if not b.value:             # LOW when pressed
            print(f"{name} pressed")
            time.sleep(0.2)         # debounce
    time.sleep(0.01)

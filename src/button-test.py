import time
import board
import digitalio

SW_PINS = [
    ("SW0", board.GP15),
    ("SW1", board.GP13),
    ("SW2", board.GP7),
    ("SW3", board.GP2),
    ("SW4", board.GP14),
]

buttons = []
for name, pin in SW_PINS:
    b = digitalio.DigitalInOut(pin)
    b.direction = digitalio.Direction.INPUT
    b.pull = digitalio.Pull.UP
    buttons.append((name, b))

print("Button tester running. Press and hold any switch…")
while True:
    for name, b in buttons:
        if not b.value:               # LOW when pressed
            print(f"{name} pressed")
            time.sleep(0.2)           # simple debounce
    time.sleep(0.01)

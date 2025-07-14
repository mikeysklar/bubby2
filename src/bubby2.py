import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.mouse import Mouse
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
import chords_config

# ─── Hardware setup ────────────────────────────────────────────────────
SW_PINS = (
    board.GP15,  # SW0
    board.GP13,  # SW1
    board.GP7,   # SW2
    board.GP2,   # SW3
    board.GP14,  # SW4
)
pins = []
for gp in SW_PINS:
    p = digitalio.DigitalInOut(gp)
    p.direction = digitalio.Direction.INPUT
    p.pull = digitalio.Pull.UP
    pins.append(p)

# ─── USB HID setup ─────────────────────────────────────────────────────
keyboard = Keyboard(usb_hid.devices)
mouse    = Mouse(usb_hid.devices)
cc       = ConsumerControl(usb_hid.devices)

# ─── Timing constants, state vars, etc. ────────────────────────────────
STABLE_MS_ALPHA = 0.03
STABLE_MS_OTHER = 0.02
DEBOUNCE_UP     = 0.05
TAP_WINDOW      = 0.5
MIN_TAP_INT     = 0.1
L5_REPEAT_MS    = 0.1
NAV_REPEAT_MS   = 0.2
LAYER_LOCK_COOLDOWN = 0.1
SCROLL_REPEAT_MS    = 0.15
THUMB_HOLD_TO_LOCK  = 0.12

layer = 1
thumb_taps = 0
tap_in_prog = False
last_tap_time = 0.0
last_combo = ()
pending_combo = None
sent_release = False
skip_scag = False
scag_skip_combo = None
modifier_armed = False
held_modifier = None
last_time = time.monotonic()
held_combo = ()
last_repeat = 0.0
accel_active = False
held_nav_combo = ()
last_nav = 0.0
last_pending_combo = None
last_layer_change = 0.0
held_scroll_combo = ()
last_scroll = 0.0
thumb_locked = False

MOVE_DELTA = 5
ACCEL_MULTIPLIER = 2
ACCEL_CHORD = (1, 2, 3)

def check_chords():
    # ... your full function, unchanged, using `pins` ...
    pressed = tuple(not p.value for p in pins)
    # rest of logic from your MCP23008 version

# ─── Main loop ────────────────────────────────────────────────────────
while True:
    check_chords()
    time.sleep(0.01)

import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import board
import digitalio


def build_btn(pin):
    btn = digitalio.DigitalInOut(pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.DOWN
    return btn


GP_PINS = [board.GP9, board.GP8, board.GP7, board.GP19, board.GP20, board.GP21]
BTN_TRIGGER = [
    (Keycode.COMMAND, Keycode.L),
    (Keycode.COMMAND, Keycode.C),
    (Keycode.COMMAND, Keycode.V),
    (Keycode.COMMAND, Keycode.Z),
    (Keycode.COMMAND, Keycode.T),
    (Keycode.COMMAND, Keycode.N)
]

btns = [build_btn(pin) for pin in GP_PINS]


keyboard = Keyboard(usb_hid.devices)

while True:
    for (i, btn) in enumerate(btns):
        if btn.value:
            keyboard.send(*BTN_TRIGGER[i])
            time.sleep(0.1)
    time.sleep(0.1)

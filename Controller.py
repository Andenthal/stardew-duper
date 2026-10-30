import time
import vgamepad as vg

CONTROLLER_PATH = '/dev/input/event13'
SHORT_DELAY = 0.100
MEDIUM_DELAY = 0.24


class Controller:

    def __init__(self):
        self.gamepad = vg.VX360Gamepad()
        #self.gamepad = vg.VDS4Gamepad()
        time.sleep(0.5) # give time for game engine to recognize new device

    def tap_down(self, count=1):
        #idea for refactor repeat(cmd(count)) ???
        # move looping single method somehow ???
        for i in range(0, count):
            self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
            self.gamepad.update()
            time.sleep(MEDIUM_DELAY)
            self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
            self.gamepad.update()
            time.sleep(0.25)
            count += 1

    def tap_left(self, count=1):
        for i in range(0, count):
            self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
            self.gamepad.update()
            time.sleep(MEDIUM_DELAY)
            self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
            self.gamepad.update()
            time.sleep(0.25)
            count += 1

    def tap_left_trigger(self, count=1):
        for i in range(0, count):
            self.gamepad.left_trigger_float(value_float=1)
            #self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            self.gamepad.update()
            time.sleep(MEDIUM_DELAY)
            self.gamepad.left_trigger_float(value_float=0.0)
            #self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
            self.gamepad.update()
            time.sleep(0.25)
            count += 1

    def tap_right(self, count=1):
        for i in range(0, count):
            #print("Tap right")
            self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
            self.gamepad.update()
            time.sleep(MEDIUM_DELAY)
            self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
            self.gamepad.update()
            time.sleep(0.25)
            count += 1

    def tap_start(self, count=1):
        for i in range(0, count):
            self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
            #self.gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_OPTIONS)
            self.gamepad.update()
            time.sleep(MEDIUM_DELAY)
            self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
            #self.gamepad.update()
            time.sleep(0.25)
            count += 1

    def tap_up(self, count=1):
        for i in range(0, count):
            #print("Tap up")
            self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
            self.gamepad.update()
            time.sleep(MEDIUM_DELAY)
            self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
            self.gamepad.update()
            time.sleep(0.25)
            count += 1

    def tap_circle(self, count=1):
        for i in range(0, count):
            #print("Tap Circle")
            self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            #self.gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
            self.gamepad.update()
            time.sleep(MEDIUM_DELAY)
            self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            #self.gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
            self.gamepad.update()
            time.sleep(0.25)
            count += 1

    def tap_cross(self, count=1):
        for i in range(0, count):
            #print("Tap Cross")
            self.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            #self.gamepad.press_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
            self.gamepad.update()
            #time.sleep(MEDIUM_DELAY)
            time.sleep(SHORT_DELAY)
            self.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            #self.gamepad.release_button(button=vg.DS4_BUTTONS.DS4_BUTTON_CROSS)
            self.gamepad.update()
            #time.sleep(0.25)
            count += 1



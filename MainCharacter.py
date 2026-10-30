import time

from pynput.mouse import Button, Controller as Mouse

class MainCharacter:

    def __init__(self):
        self.mouse = Mouse()

    # fer debugging
    def _monitor_mouse(self):
        while True:
            #print(mouse.get_position())
            print(self.mouse.position)

    def click(self):
        self.mouse.press(Button.left)
        time.sleep(0.25)
        self.mouse.release(Button.left)

    def double_click(self):
        # Double click; this is different from pressing and releasing twice on macOS
        self.mouse.click(Button.left, 2)

    def grab(self):
        print("Main grabbing")
        self.right_click()

    def go_home(self):
        self.mouse.position = (2758, 984)
        time.sleep(0.25)

    def left_click(self):
        self.click()

    def move(self):
        #mouse.move(50, 50, absolute=False, duration=0.2)
        pass

    def mouse_over_table(self):
        self.mouse.position = (2370, 533)
        time.sleep(0.25)

    def right_click(self):
        self.mouse.press(Button.right)
        time.sleep(0.25)
        self.mouse.release(Button.right)

    def spam_read_book(self, count = 1):
        for i in range(1, count):
            self.right_click()
            time.sleep(1.3)


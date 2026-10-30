import time

from Controller import Controller


class Duper:

    def __init__(self):
        self.controller = Controller()

    def drop(self):
        self.controller.tap_cross()

    def grab(self):
        self.controller.tap_cross()

    def logout(self):
        self.controller.tap_start()
        self.controller.tap_up()
        self.controller.tap_right(9)
        self.controller.tap_cross()
        self.controller.tap_down()
        self.controller.tap_cross()

    def move_from_dupe_door_outside(self):
        self.move_down(2)
        self.move_right(7)
        self.move_up(3)
        self.tap_cross()
        # outside -> inside transition
        time.sleep(1.5)
        self.move_up(2)
        self.move_left(4)
        self.move_up(2)
        self.move_right()
        # should be facing table

    def move_from_spawn_to_table(self):
        self.move_left(5)
        #delay of .25 for movement seems to be good
        # maybe refactor to define here
        # move_left passes pause down
        self.move_down(3)
        #outside now, wait for transition
        time.sleep(1.5)
        self.move_from_dupe_door_outside()


    def move_down(self, count=1):
        self.controller.tap_down(count)

    def move_left(self, count=1):
        self.controller.tap_left(count)
        #time.sleep(.100)

    def move_right(self, count=1):
        self.controller.tap_right(count)

    def move_up(self, count=1):
        self.controller.tap_up(count)

    def set_active_item(self):
        self.grab()
        self.select_and_place_item()

    def select_and_place_item(self):
        self.controller.tap_left_trigger()
        self.controller.tap_cross()

    def spawn_dupe(self):
        self.controller.tap_start()
        self.controller.tap_cross()
        # wait for loading screen
        time.sleep(5)

    def tap_cross(self, count=1):
        self.controller.tap_cross(count)

    def tap_circle(self, count=1):
        self.controller.tap_circle(count)
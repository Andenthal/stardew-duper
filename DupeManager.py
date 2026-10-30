import time

from Duper import Duper
from MainCharacter import MainCharacter
from threading import Thread


class DupeManager:
    def __init__(self,
                 spawn=True,
                 start_from_bed=True,
                 start_from_dupe_door=False,
                 logout_dupe=True,
                 main_only=False,
                 ):

        self.spawn = spawn
        self.start_from_bed = start_from_bed
        self.start_from_dupe_door = start_from_dupe_door
        self.logout_dupe = logout_dupe
        self.main_only = main_only

        if not main_only:
            self.duper = Duper()

        self.main_character = MainCharacter()
        time.sleep(0.5)

        #debug
        #self._unfuck()
        #return

        self._set_the_stage()

    def _unfuck(self):
        #self.duper.move_left(4)
        #self.duper.move_down()
        #self.duper.move_right()
        #self.duper.tap_cross()
        self.duper.tap_circle()
        #self.duper.logout()
        pass

    def _set_the_stage(self):
        #print(f"self.spawn: {self.spawn}")
        if self.spawn:
            print("spawning")
            self.duper.spawn_dupe()

        if self.start_from_bed:
            self.duper.move_from_spawn_to_table()
            self._set_active_item()
        elif self.start_from_dupe_door:
            self.duper.move_from_dupe_door_outside()
            self._set_active_item()

        self._setup_main_character()
        time.sleep(0.25)

    def _setup_main_character(self):
        # main character is manually placed next to table
        self.main_character.mouse_over_table()

    def all_grab(self):
        self.main_character.mouse_over_table()
        character_grab = Thread(target=self.main_character.grab)
        duper_grab = Thread(target=self.duper.grab)

        duper_grab.start()
        character_grab.start()

        character_grab.join()
        duper_grab.join()

    def dupe_items(self, count = 1):
        for i in range(1, count):
            #rhythm is both grab, dupe drops, repeat
            self.all_grab()
            self.duper.drop()

        if self.logout_dupe:
            self.duper.logout()

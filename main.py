import time

from DupeManager import DupeManager
from MainCharacter import MainCharacter

if __name__ == '__main__':
    # need time to move mouse to window
    time.sleep(1)

    # working controller
    #dev = Controller()
    #time.sleep(0.5)
    #dev.tap_start()
    #dev.tap_x()
    #dev.tap_left()
    #time.sleep(1)

    #mouse = Mouse()
    #mouse.move_to_table()
    #mouse.right_click()
    #time.sleep(1)

    # Fine tune getting to table in Duper and ControllerMEDIUM_DELAY
    #dupe = DupeManager()
    dupe = DupeManager(
        spawn=True,
        start_from_bed=False,
        start_from_dupe_door=False,
        logout_dupe=False
        #fall through to spawn @ table
        #on 2nd login in same session - player 2 has their current item remembered
        # try to set to default before logging out???
    )
    dupe.dupe_items(count = 5)


    #mainCharacter = MainCharacter()
    #time.sleep(1)
    #mainCharacter.spam_read_book(10)



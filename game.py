import traceback
from src.dot.dotscreen import DotScreen
from src.interact.keyboardinteract import *
from src.interact.mouseinteract import *
import i18n

from src.define import GameDefine
from src.world.logosplashworld import LogoSplashWorld


import os
os.environ['SDL_VIDEO_CENTERED'] = '1'


def main():
    screen = DotScreen(dotget(GameDefine.WINDOW_WIDTH), dotget(GameDefine.WINDOW_HEIGHT), GameDefine.FPS, 0)
    screen.addEventInteract(KeyboardInteract())
    screen.addEventInteract(MouseInteract())
    screen.addEventInteract(MouseInteract())

    # face_interact = CascadeFollowerInteract(1, 2, "assets/cascade/hand.xml")
    # face_interact = CascadeFollowerInteract(1, 0, "assets/cascade/haarcascade_frontalface_alt.xml")
    # face_interact.set_boundaries(face_interact.leftBoundary, face_interact.rightBoundary, 100)
    # face_interact.set_boundaries(face_interact.leftBoundary, face_interact.rightBoundary - 10, 49)

    # face_interact.start()
    # screen.addInteract(face_interact)

    screen.setWorld(LogoSplashWorld())

    try:
        while screen.on:
            screen.step()

        pygame.quit()
    except:
        traceback.print_exc()
        pygame.quit()


    #face_interact.stop()

if __name__ == '__main__':
    main()

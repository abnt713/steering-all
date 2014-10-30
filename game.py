import pygame
import traceback
from src.draw.dotscreen import DotScreen
from src.interact.keyboardinteract import *
from src.interact.mouseinteract import *

from src.define import GameDefine
from src.world.dot.logosplashworld import LogoSplashWorld


import os
os.environ['SDL_VIDEO_CENTERED'] = '1'


def main():
    screen = DotScreen(dotget(GameDefine.WINDOW_WIDTH), dotget(GameDefine.WINDOW_HEIGHT), GameDefine.FPS, pygame.FULLSCREEN)
    screen.addEventInteract(KeyboardInteract())
    screen.addEventInteract(MouseInteract())
    screen.setWorld(LogoSplashWorld())

    try:
        while screen.on:
            screen.step()

        pygame.quit()
    except:
        traceback.print_exc()
        pygame.quit()

if __name__ == '__main__':
    main()

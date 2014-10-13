import pygame
import traceback
from src.draw.dotscreen import DotScreen
from src.interact.keyboardinteract import *

from src.define import GameDefine
from src.world.dot.logosplashworld import LogoSplashWorld


import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

def main():
  screen = DotScreen(dotget(GameDefine.WINDOW_WIDTH), dotget(GameDefine.WINDOW_HEIGHT), 30)
  screen.addInteract(KeyboardInteract())
  screen.setWorld(LogoSplashWorld())

  try:
    while screen.on:
      screen.step()

    pygame.quit()
  except:
    traceback.print_exc()
    pygame.quit()

if __name__=='__main__':
  main()

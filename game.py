import pygame
import traceback
from src.draw.dotscreen import DotScreen

from src.define import GameDefine
from src.world.dot.logosplashworld import LogoSplashWorld


import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

def main():
  screen = DotScreen(GameDefine.WINDOW_WIDTH, GameDefine.WINDOW_HEIGHT)
  screen.setWorld(LogoSplashWorld())

  try:
    while screen.on:
      screen.step()

    pygame.quit()
  except:
    #traceback.print_exc()
    pygame.quit()

if __name__=='__main__':
  main()

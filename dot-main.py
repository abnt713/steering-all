import pygame
from src.define import *
from src.dot.entities.dotcar import DotCar
from src.dot.entities.dotpolice import DotPoliceStation
from src.dot.entities.dotradar import DotRadar
from src.dot.entities.dotlog import DotLog
from src.dot.entities.dotgoblet import DotGoblet
from src.dot.entities.dotflag import DotFlag
from src.dot.entities.dotkog import DotKog
from src.dot.entities.dotheart import DotHeart

import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

def main():
  pygame.init()

  kog = DotHeart()
  goblet = DotGoblet()
  flag = DotFlag()

  totalWidth = GameDefine.WINDOW_WIDTH
  totalHeight = GameDefine.WINDOW_HEIGHT
  windowDim = (int(totalWidth), int(totalHeight))
  displaysurf = pygame.display.set_mode(windowDim)

  goblet.createSurface()

  flag.setDotAlpha(127)
  flag.createSurface()

  kog.setDotAlpha(127)
  kog.createSurface()

  goblet.centerX(totalWidth)
  goblet.centerY(totalHeight)

  flag.marginRight(dotget(1))
  flag.leftOf(goblet)
  flag.centerY(totalHeight)

  kog.marginLeft(dotget(1))
  kog.rightOf(goblet)
  kog.centerY(totalHeight)

  while True:
    displaysurf.fill((208, 208, 208));
    flag.draw(displaysurf)
    kog.draw(displaysurf)
    goblet.draw(displaysurf)

    pygame.display.update()

if __name__=='__main__':
  main()

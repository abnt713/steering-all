import pygame
from src.dot.entities.dotcar import DotCar
from src.dot.entities.dotpolice import DotPoliceStation
from src.dot.entities.dotradar import DotRadar
from src.dot.entities.dotlog import DotLog
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

def main():
  pygame.init()

  ent = DotCar()
  totalWidth = ent.surfaceWidth
  totalHeight = ent.surfaceHeight
  windowDim = (int(totalWidth), int(totalHeight))
  displaysurf = pygame.display.set_mode(windowDim, pygame.NOFRAME)
  ent.createSurface()


  while True:
    displaysurf.fill((208, 208, 208));
    displaysurf.blit(ent.surface, (0, 0))
    pygame.display.update()


if __name__=='__main__':
  main()

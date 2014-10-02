from src.builder.carworldbuilder import *
from src.entities.carhero import *

import pygame
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

def main():
  global worldManager
  pygame.init()

  worldManager = CarWorldBuilder(CarHero(96, 128), 3)

  displaysurf = pygame.display.set_mode(worldManager.getAdjustedDisplaySize(), pygame.FULLSCREEN)
  clock = pygame.time.Clock()

  worldManager.setDisplaysurf(displaysurf)

  pygame.display.set_caption('Steering Head')

  while worldManager.world.gameOn:
    clock.tick(worldManager.fps)
    worldManager.step()
    pygame.display.update()

  worldManager.dispose()

if __name__=='__main__':
  main()

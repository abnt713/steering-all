from src.builder.carworldbuilder import *
from src.entities.carhero import *
from src.spawner.spawnercollector import *
from src.spawner.enemyspawner import *

import pygame
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

def main():
  global worldManager
  pygame.init()

  worldManager = CarWorldBuilder(CarHero(96, 128), 3)
  worldManager.setSpawnerCollector(SpawnerCollector())

  worldManager.addSpawner(EnemySpawner(2, 0))

  displaysurf = pygame.display.set_mode(worldManager.getAdjustedDisplaySize(), pygame.NOFRAME)
  worldManager.fps = pygame.time.Clock()

  worldManager.setDisplaysurf(displaysurf)

  pygame.display.set_caption('Steering Head')

  while worldManager.world.gameOn:
    worldManager.step()
    pygame.display.update()


if __name__=='__main__':
  main()

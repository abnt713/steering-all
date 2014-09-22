import worldbuilder
from src.spawner.spawnercollector import *
from src.spawner.enemyspawner import *
from src.interact.faceInteract import *
from src.entities.carentity import *
from src.world.carworld import *
from src.world.drawing.carworldrender import *
from src.interact.keyboardInteract import *
from src.interact.mouseInteract import *

class CarWorldBuilder (worldbuilder.WorldBuilder):

  def __init__(self, hero, trails, trailPadding = 4):
    worldWidth = (hero.width * trails) + (hero.width / trailPadding) * trails * 2
    self.spawner = SpawnerCollector()
    self.addSpawner(EnemySpawner(2, 0))
    self.world = CarWorld(self, trails, worldWidth , hero.height * 5, (hero.height * 2) / 100)
    self.world = CarWorld(self, trails, worldWidth , hero.height * 5, 4)
    self.world.hero = hero

    self.fthread = FaceInteract(1, 0)
    self.fthread.start()
    self.world.addInteract(self.fthread)

    self.world.addInteract(KeyboardInteract())
    self.world.addInteract(MouseInteract())

    self.worldRenderer = CarWorldRenderer(hero, trailPadding)

  def dispose(self):
    self.fthread.stop()

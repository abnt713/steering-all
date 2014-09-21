import worldbuilder
from src.spawner.spawnercollector import *
from src.entities.carentity import *
from src.world.carworld import *
from src.world.drawing.carworldrender import *
from src.interact.keyboardInteract import *

class CarWorldBuilder (worldbuilder.WorldBuilder):

  def __init__(self, hero, trails, trailPadding = 4):
    worldWidth = (hero.width * trails) + (hero.width / trailPadding) * trails * 2
    self.spawner = SpawnerCollector()
    self.world = CarWorld(self, trails, worldWidth , hero.height * 5, (hero.height * 2) / 100)
    self.world.hero = hero
    self.world.addInteract(KeyboardInteract())

    self.worldRenderer = CarWorldRenderer(hero, trailPadding)

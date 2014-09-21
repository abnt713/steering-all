import spawner
from src.entities.carentity import *
from src.utils.dice import *

class EnemySpawner (spawner.Spawner):

  def __init__(self, spawnFrequency, padding):
    self.latestTrail = 0
    self.latestSpawnTime = 0
    self.spawnFrequency = spawnFrequency
    self.padding = padding

  def spawn(self, world):
    spawnLimit = int((world.height / self.spawnFrequency) + (world.hero.height * self.padding))

    # Check if should spawn
    if self.latestSpawnTime > spawnLimit:
      maxTrail = world.trailsCount

      dice = Dice(0, maxTrail - 1)
      electedTrail = dice.roll()

      chance = (world.trailsCount - 2) * 10
      doubleDice = PercentChance(chance)
      shouldDouble = doubleDice.roll()

      # Check if there is a 'double' enemy
      if shouldDouble:
        if electedTrail == (maxTrail - 1):
          electedTrail -= 1

        self.addEnemyToWorld(world, electedTrail)
        self.addEnemyToWorld(world, electedTrail + 1)
      else:
        self.addEnemyToWorld(world, electedTrail)

      self.latestSpawnTime = 0

    self.latestSpawnTime += world.actualDropspeed

    #if self.latestSpawnTime > (world.height * 2):
    #  self.latestSpawnTime = self.latestSpawnTime - (world.height * 2)

  def addEnemyToWorld(self, world, trail):
    enemy = CarEntity(world.hero.width, world.hero.height)
    enemy.y -= enemy.height
    enemy.activeTrail = trail
    world.addEnemy(enemy)

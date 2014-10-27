import spawner
from src.dot.entities.dotcar import *
from src.utils.dice import *

class DotCarSpawner (spawner.Spawner):

  def __init__(self, spawnFrequency, padding):
    self.latestTrail = 0
    self.latestSpawnTime = 0
    self.spawnFrequency = spawnFrequency
    self.padding = padding

  def spawn(self, parent):
    # Spawning based on world height and Car height
    spawnLimit = int((parent.height / self.spawnFrequency) + (parent.hero.height * self.padding))

    # Check if should spawn
    if self.latestSpawnTime > spawnLimit:
      maxTrail = 3

      dice = Dice(0, maxTrail - 1)
      electedTrail = dice.roll()

      chance = (maxTrail - 2) * 10
      doubleDice = PercentChance(chance)
      shouldDouble = doubleDice.roll()

      # Check if there is a 'double' enemy
      if shouldDouble:
        if electedTrail == (maxTrail - 1):
          electedTrail -= 1

        self.addEnemyToWorld(parent, electedTrail)
        self.addEnemyToWorld(parent, electedTrail + 1)
      else:
        self.addEnemyToWorld(parent, electedTrail)

      self.latestSpawnTime = 0

    self.latestSpawnTime += parent.actualFallSpeed

  def addEnemyToWorld(self, parent, trail):
    enemy = DotCar()

    enemy.setDotRes([
      "assets/img/red-brick.png"
    ]);


    enemy.y -= enemy.height
    enemy.trail = trail

    parent.addChild(enemy)

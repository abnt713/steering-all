import spawner
from src.dot.entities.dotcar import *
from src.dot.entities.dotradar import *
from src.utils.dice import *


class DotCarSpawner (spawner.Spawner):

    def __init__(self, spawnFrequency, padding):
        self.latestSpawnTime = 0
        self.spawnFrequency = spawnFrequency
        self.padding = padding
        self.canSpawn = True
        self.lastWasRadar = False
        self.lastWasDouble = False
        self.lastWasMiddle = False


    def spawn(self, parent):
        if self.canSpawn:
            # Spawning based on world height and Car height
            spawnLimit = int((parent.height / self.spawnFrequency) + (parent.hero.height * self.padding))

            # Check if should spawn
            if self.latestSpawnTime > spawnLimit:

                dice = PercentChance(10)
                print("Radar chance: ")
                spawnradar = dice.roll()
                if spawnradar and not self.lastWasRadar:
                    self.canSpawn = False
                    self.spawnRadar(parent)
                else:
                    print("Speed chance: ")
                    cardice = PercentChance(25)
                    shouldDoubleSpeed = cardice.roll()
                    if shouldDoubleSpeed and not self.lastWasRadar and not self.lastWasDouble and not self.lastWasMiddle:
                        self.spawnCar(parent, 2)
                    else:
                        print("Spawning normal car")
                        self.spawnCar(parent, 1)

            if parent.shouldFall:
                self.latestSpawnTime += parent.dropHeight


    def spawnCar(self, parent, speed):

        maxTrail = 3

        dice = Dice(0, maxTrail - 1)
        electedTrail = dice.roll()

        if electedTrail == 1:
            self.lastWasMiddle = True
        else:
            self.lastWasMiddle = False

        chance = (maxTrail - 2) * 20
        doubleDice = PercentChance(chance)
        shouldDouble = doubleDice.roll()

        # Check if there is a 'double' enemy
        if shouldDouble and speed == 1:
            if electedTrail == (maxTrail - 1):
                subtrail = 0
            else:
                subtrail = electedTrail + 1

            self.addEnemyToWorld(parent, electedTrail, speed)
            self.addEnemyToWorld(parent, subtrail, speed)
            self.lastWasDouble = True
            self.lastWasRadar = False
        else:
            self.lastWasRadar = False
            self.lastWasDouble = False
            self.addEnemyToWorld(parent, electedTrail, speed)

        self.latestSpawnTime = 0

    def spawnRadar(self, parent):
        radar = DotRadar(9, 10, self)
        radar.y -= radar.height

        parent.addChild(radar)
        self.lastWasRadar = True
        self.lastWasDouble = False
        self.lastWasMiddle = False

    def addEnemyToWorld(self, parent, trail, speed):
        enemy = DotCar()

        if speed == 1:
            enemy.setDotRes([
                "assets/img/red-brick.png"
            ]);
        else:
            enemy.setDotRes([
                "assets/img/yellow-brick.png"
            ]);


        enemy.y -= enemy.height
        enemy.speed = speed
        enemy.trail = trail

        parent.addChild(enemy)

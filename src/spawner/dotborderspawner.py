import spawner
from src.dot.entities.dotborder import *
from src.utils.dice import *


class DotBorderSpawner (spawner.Spawner):

    def __init__(self, padding):
        self.latestSpawnTime = 0
        self.padding = padding

    def spawn(self, parent):
        modelborder = DotBorder()
        spawnLimit = int(modelborder.height * self.padding)

        if self.latestSpawnTime > spawnLimit:
            self.latestSpawnTime = 0
            self.spawnchild(parent)

        if parent.shouldFall:
            self.latestSpawnTime += parent.dropHeight

    def spawnchild(self, parent):
        leftBorder = DotBorder()
        rightBorder = DotBorder()

        leftBorder.y = 0 - leftBorder.height
        rightBorder.y = 0 - rightBorder.height

        leftBorder.x = 0
        rightBorder.x = parent.width - rightBorder.width

        parent.addChild(leftBorder)
        parent.addChild(rightBorder)


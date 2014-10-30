import src.dot.dotchild
from src.define import *


class DotRadar(src.dot.dotchild.DotChild):

    def __init__(self, width, height, spawner):
        res = [
            "assets/img/red-brick.png"
        ]

        self.spawner = spawner

        self.canMove = True
        grid = []

        for row in range(0, height):
            element = []
            for column in range(0, width):
                element.append(1)
            grid.append(element)

        src.dot.dotchild.DotChild.__init__(self, grid, res)
        self.setDotAlpha(55)

    def onAttachToCollection(self):
        print(self.parent.getBorderWidth())
        print(self.x)
        self.x = self.parent.getBorderWidth() + self.parent.x

    def step(self):
        if self.parent.shouldFall:
            self.y += self.parent.dropHeight

        if self.y > self.height:
            self.spawner.canSpawn = True

    def handleEvent(self, inputResult):
        if not self.canMove:
            if inputResult == GameDefine.COMMAND_LEFT or inputResult == GameDefine.COMMAND_RIGHT:
                self.parent.resetGame()

    def notifyCollide(self, collider):

        if collider is None:
            self.canMove = True
            return

        if collider.type == "hero":
            self.canMove = False

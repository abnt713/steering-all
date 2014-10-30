import dotcar
from src.define import GameDefine

class DotHero(dotcar.DotCar):

    def __init__(self):
        dotcar.DotCar.__init__(self)
        self.setDotRes(["assets/img/blue-brick.png"])
        self.type = "hero"

    def step(self):
        self.x = self.parent.getBorderWidth() + (self.width * self.trail) + self.parent.x

    def handleEvent(self, inputResult):
        if inputResult == GameDefine.COMMAND_LEFT and self.trail > 0:
            self.trail -= 1

        if inputResult == GameDefine.COMMAND_RIGHT and self.trail < 2:
            self.trail += 1

    def notifyCollide(self, collider):
        pass

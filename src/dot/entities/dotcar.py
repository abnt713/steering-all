import src.dot.dotchild
from src.define import GameDefine

class DotCar(src.dot.dotchild.DotChild):

  def __init__(self):
    res = [
      "assets/img/black-brick.png"
    ]

    grid = [
      [0, 1, 0],
      [1, 1, 1],
      [0, 1, 0],
      [1, 0, 1]
    ]

    src.dot.dotchild.DotChild.__init__(self, grid, res)
    self.type = "enemy"
    self.trail = 0

  def step(self):
    if self.parent.shouldFall:
      self.y += self.parent.dropHeight

    self.x = self.parent.getBorderWidth() + (self.width * self.trail) + self.parent.x

  def setTrail(self, trail):
    self.trail = trail

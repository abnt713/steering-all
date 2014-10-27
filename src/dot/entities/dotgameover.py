__author__ = 'alisonbento'

import src.dot.dotentity

class DotGameOver(src.dot.dotentity.DotEntity):

  def __init__(self):
    res = [
        "assets/img/black-brick.png",
        "assets/img/gray-brick.png",
        "assets/img/brown-brick.png"
    ]

    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    src.dot.dotentity.DotEntity.__init__(self, grid, res)

  def setSmall(self):
    self.setDotScale(0.5)

  def setMedium(self):
    self.setDotScale(0.75)

  def setLarge(self):
    self.setDotScale(1)


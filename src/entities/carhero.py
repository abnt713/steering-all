from carentity import *

class CarHero(CarEntity):

  def __init__(self, width, height):
    CarEntity.__init__(self, width, height)
    self.score = 0
    self.isBoosting = False
    self.boostTime = 0

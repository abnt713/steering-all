import src.dot.dotchild
from src.define import *

class SimpleDot(src.dot.dotchild.DotChild):

  def __init__(self):
    res = [
      "assets/img/black-brick.png"
    ]

    grid = [
      [1],
      [1]
    ]

    src.dot.dotchild.DotChild.__init__(self, grid, res)
    

  def drop(self, dist):
    self.y += dist

  def step(self):
    if self.y > self.parent.height + (self.height * 2):
      self.parent.removeChild(self)
      del self

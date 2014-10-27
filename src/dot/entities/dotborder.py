import simpledot
from src.define import *

class DotBorder(simpledot.SimpleDot):

  def step(self):
    if self.parent.shouldFall:
      self.y += dotget(1)

    if self.y > self.parent.height + (self.height * 2):
      self.parent.removeChild(self)
      del self

import spawner
from src.dot.entities.dotborder import *
from src.utils.dice import *

class DotBorderSpawner (spawner.Spawner):

  def spawn(self, parent):
    if parent.shouldSpawn:
      leftBorder = DotBorder()
      rightBorder = DotBorder()

      leftBorder.y = 0 - leftBorder.height
      rightBorder.y = 0 - rightBorder.height

      leftBorder.x = 0
      rightBorder.x = parent.width - rightBorder.width

      parent.addChild(leftBorder)
      parent.addChild(rightBorder)

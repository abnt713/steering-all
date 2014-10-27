import dotentity
import src.interact.listener

class DotCollection(dotentity.DotEntity, src.interact.listener.InteractListener):

  def __init__(self, grid, dotRes, dotScale = 1):
    dotentity.DotEntity.__init__(self, grid, dotRes, dotScale)
    self.children = []

  def addChild(self, child):
    child.x = child.x + self.x
    child.y = child.y + self.y
    child.attachToCollection(self)
    self.children.append(child)

  def draw(self, displaysurf):
    dotentity.DotEntity.draw(self, displaysurf)
    for child in self.children:
      child.step()
      child.createSurface()

      child.draw(displaysurf)

  def listen(self, inputResult):
    for child in self.children:
      child.handleEvent(inputResult)

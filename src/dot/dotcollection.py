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

  def draw(self, displaysurf, order=1):
    dotentity.DotEntity.draw(self, displaysurf)

    if order == 1:
        list = self.children
    else:
        list = reversed(self.children)

    for child in list:
      child.step()
      child.createSurface()

      child.draw(displaysurf)

  def listen(self, inputResult):
    for child in self.children:
      child.handleEvent(inputResult)

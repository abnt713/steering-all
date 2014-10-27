from dotgrid import DotGrid

class DotEntity(DotGrid):

  def __init__(self, grid, dotRes, dotScale = 1):
    DotGrid.__init__(self, grid, dotRes, dotScale)

  def setSmall(self):
    pass

  def setMedium(self):
    pass

  def setLarge(self):
    pass

  def step(self):
    pass

  def handleEvent(self, inputResult):
    pass

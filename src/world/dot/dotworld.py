

class DotWorld:

  def __init__(self):
    self.screen = None

  def setScreen(self, screen):
    self.screen = screen
    self.onAttachScreen()

  def onAttachScreen(self):
    pass

  def step(self):
    pass

import src.interact.listener

class DotWorld(src.interact.listener.InteractListener):

  def __init__(self):
    self.screen = None
    self.active = True

  def pause(self):
    self.active = False

  def resume(self):
    self.active = True

  def listen(self, inputResult):
    pass

  def setScreen(self, screen):
    self.screen = screen
    self.onAttachScreen()

  def onAttachScreen(self):
    pass

  def step(self):
    pass

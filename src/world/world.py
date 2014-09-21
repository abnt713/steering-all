import src.interact.listener

class World (src.interact.listener.InteractListener):

  def __init__(self, width, height, builder):
    self.builder = builder
    self.width = width
    self.height = height
    self.interacts = []

  def notifyInteracts(self):
    for interact in self.interacts:
      interact.checkInteraction()

  def addInteract(self, interact):
    interact.setListener(self)
    self.interacts.append(interact)

  def listen(self, inputResult):
    pass

  def update(self):
    self.notifyInteracts()
    self.step()

  def step(self):
    pass

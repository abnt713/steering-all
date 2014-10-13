import interact

class EvtInteract(interact.Interact):

  def __init__(self):
    self.events = []

  def checkEventInteraction(self, events):
    self.events = events
    self.checkInteraction()

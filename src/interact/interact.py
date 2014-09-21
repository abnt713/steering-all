class Interact:

  def setListener(self, listener):
    self.listener = listener

  def checkInteraction(self):
    pass

  def notifyListener(self, inputResult):
    self.listener.listen(inputResult)

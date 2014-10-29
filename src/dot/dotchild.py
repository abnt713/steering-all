import dotentity

class DotChild(dotentity.DotEntity):

    def __init__(self, grid, dotRes, dotScale = 1):
        dotentity.DotEntity.__init__(self, grid, dotRes, dotScale)
        self.type = None
        self.parent = None

    def attachToCollection(self, parent):
        self.parent = parent

    def onDispose(self):
        pass

    def notifyCollide(self, collider):
        pass

class Entity:

  def __init__(self, width, height):
    self.x = 0
    self.y = 0
    self.width = width
    self.height = height

  def getCoordinates(self):
    return (self.x, self.y)

  def getDimensions(self):
    return (self.width, self.height)

  def getRect(self):
    return ((self.x, self.y), (self.width, self.height))

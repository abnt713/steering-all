
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

  def centerX(self, totalWidth):
    self.x = (totalWidth / 2) - (self.width / 2)

  def centerY(self, totalHeight):
    self.y = (totalHeight / 2) - (self.height / 2)

  def draw(self, displaysurf):
    displaysurf.blit(self.surface, (self.x, self.y))

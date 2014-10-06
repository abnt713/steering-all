from entity import Entity

class RelativeEntity(Entity):

  def __init__(self, width, height):
    Entity.__init__(self, width, height)
    self.margin = [0, 0, 0, 0]

  def below(self, entity):
    self.y = entity.y + entity.height + self.margin[1]

  def above(self, entity):
    self.y = entity.y - self.height - self.margin[3]

  def leftOf(self, entity):
    self.x = entity.x - self.width - self.margin[2]

  def rightOf(self, entity):
    self.x = entity.x + entity.width + self.margin[0]


  def margin(self, margin):
    self.margin = margin;

  def marginLeft(self, margin):
    self.margin[0] = margin

  def marginRight(self, margin):
    self.margin[2] = margin

  def marginTop(self, margin):
    self.margin[1] = margin

  def marginBottom(self, margin):
    self.margin[3] = margin


  def centerRelativeX(self, entity):
    self.x = entity.x + (entity.width / 2) - (self.width / 2)

  def centerRelativeY(self, entity):
    self.y = entity.y + (entity.height / 2) - (self.height / 2)

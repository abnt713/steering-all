import entity

class CarEntity (entity.Entity):

  def __init__(self, width, height):
    entity.Entity.__init__(self, width, height)
    self.activeTrail = 0

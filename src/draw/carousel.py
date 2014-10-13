
class Carousel:

  def __init__(self):
    self.items = []
    self.selected = -1

  def addItem(self, item, selected = False):
    self.items.append(item)
    if selected:
      self.selected = (len(self.items) - 1)

  def draw(self, displaysurf):
    

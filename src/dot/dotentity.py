import dotgrid

class DotEntity(dotgrid.DotGrid):

  x = 0
  y = 0

  def __init__(self, grid, dotRes = ["assets/img/black-brick.png"], dotScale = 1.0):
    dotgrid.DotGrid.__init__(self, grid, dotRes, dotScale)

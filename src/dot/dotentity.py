from dotgrid import DotGrid

class DotEntity(DotGrid):

  def __init__(self, grid, dotRes, dotScale = 1):
    DotGrid.__init__(self, grid, dotRes, dotScale)

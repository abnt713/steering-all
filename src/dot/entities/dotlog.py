import src.dot.dotentity

class DotLog(src.dot.dotentity.DotEntity):

  def __init__(self):
    res = [
      "assets/img/brown-brick.png"
    ]

    grid = [
      [1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1]
    ]

    src.dot.dotentity.DotEntity.__init__(self, grid, res, 1)

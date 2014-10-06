import src.dot.dotentity

class DotUFRN(src.dot.dotentity.DotEntity):

  def __init__(self):
    res = [
      "assets/img/blue-brick.png",
      "assets/img/dark-blue-brick.png"
    ]

    grid = [
      [0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [1, 0, 0, 1, 0, 0, 0, 2, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1],
      [1, 0, 0, 1, 0, 2, 2, 2, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1],
      [1, 0, 0, 1, 0, 0, 0, 2, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1],
      [1, 0, 0, 1, 0, 2, 2, 2, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
      [1, 1, 1, 1, 0, 2, 2, 2, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
      [0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    src.dot.dotentity.DotEntity.__init__(self, grid, res, 1)

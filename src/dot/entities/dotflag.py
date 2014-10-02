import src.dot.dotentity

class DotFlag(src.dot.dotentity.DotEntity):

  def __init__(self):
    res = [
      "assets/img/black-brick.png",
      "assets/img/gray-brick.png",
      "assets/img/brown-brick.png"
    ]

    grid = [
      [3, 1, 1, 1, 2, 2, 2],
      [3, 1, 1, 1, 2, 2, 2],
      [3, 1, 1, 1, 2, 2, 2],
      [3, 2, 2, 2, 1, 1, 1],
      [3, 2, 2, 2, 1, 1, 1],
      [3, 2, 2, 2, 1, 1, 1],
      [3, 0, 0, 0, 0, 0, 0],
      [3, 0, 0, 0, 0, 0, 0],
      [3, 0, 0, 0, 0, 0, 0]
    ]

    src.dot.dotentity.DotEntity.__init__(self, grid, res, 0.5)

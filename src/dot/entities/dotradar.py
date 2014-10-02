import src.dot.dotentity

class DotRadar(src.dot.dotentity.DotEntity):

  def __init__(self):
    res = [
      "assets/img/black-brick.png",
      "assets/img/blue-brick.png",
      "assets/img/red-brick.png",
    ]

    grid = [
      [2, 2, 1, 3],
      [1, 1, 1, 1],
      [0, 0, 1, 1]
    ]

    src.dot.dotentity.DotEntity.__init__(self, grid, res, 0.5)

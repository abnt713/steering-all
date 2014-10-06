import src.dot.dotentity

class DotLogo(src.dot.dotentity.DotEntity):

  def __init__(self):
    res = [
      "assets/img/black-brick.png",
      "assets/img/blue-brick.png",
      "assets/img/gray-brick.png"
    ]

    grid = [
      [1, 1, 1, 1, 1, 1, 1],
      [1, 0, 0, 0, 1, 0, 1],
      [1, 0, 1, 0, 1, 0, 1],
      [1, 0, 1, 0, 1, 0, 1],
      [1, 0, 1, 0, 1, 0, 1],
      [1, 0, 1, 0, 0, 0, 1],
      [1, 1, 1, 1, 1, 1, 1],
    ]

    src.dot.dotentity.DotEntity.__init__(self, grid, res)

import src.dot.dotentity

class DotHeart(src.dot.dotentity.DotEntity):

  def __init__(self):
    res = [
      "assets/img/red-brick.png",
      "assets/img/black-brick.png"
    ]

    grid = [
      [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
      [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
      [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
      [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
      [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
      [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    ]

    src.dot.dotentity.DotEntity.__init__(self, grid, res, 0.5)

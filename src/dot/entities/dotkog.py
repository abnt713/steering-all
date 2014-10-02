import src.dot.dotentity

class DotKog(src.dot.dotentity.DotEntity):

  def __init__(self):
    res = [
      "assets/img/black-brick.png",
      "assets/img/gray-brick.png",
      "assets/img/brown-brick.png"
    ]

    grid = [
      [0, 0, 0, 1, 1, 1, 0, 0, 0],
      [0, 0, 0, 1, 1, 1, 0, 0, 0],
      [0, 0, 0, 1, 1, 1, 0, 0, 0],
      [1, 1, 1, 1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1, 1, 1, 1, 1],
      [0, 0, 0, 1, 1, 1, 0, 0, 0],
      [0, 0, 0, 1, 1, 1, 0, 0, 0],
      [0, 0, 0, 1, 1, 1, 0, 0, 0],
      [1, 1, 1, 0, 0, 0, 1, 1, 1],
      [1, 1, 1, 0, 0, 0, 1, 1, 1],
      [1, 1, 1, 0, 0, 0, 1, 1, 1]

    ]

    src.dot.dotentity.DotEntity.__init__(self, grid, res, 0.5)

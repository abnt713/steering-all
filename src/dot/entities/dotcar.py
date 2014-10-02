import src.dot.dotentity

class DotCar(src.dot.dotentity.DotEntity):

  def __init__(self):
    res = [
      "assets/img/red-brick.png",
      "assets/img/black-brick.png"
    ]

    grid = [
      [0, 1, 0],
      [1, 1, 1],
      [0, 1, 0],
      [1, 0, 1]
    ]

    src.dot.dotentity.DotEntity.__init__(self, grid, res)

import dotworld

from menuworld import MenuWorld
from src.define import *
from src.dot.entities.dotufrn import DotUFRN
from src.dot.dottext import DotText

class UfrnSplashWorld(dotworld.DotWorld):

  def __init__(self):
    dotworld.DotWorld.__init__(self)
    self.counter = 0
    self.limit = 400
    self.alpha = 0
    self.animState = 1

    self.logo = DotUFRN()
    self.label = DotText("Universidade Federal do Rio Grande do Norte", 16, (0, 0, 0), (255, 255, 255))

  def onAttachScreen(self):
    self.logo.centerX(self.screen.width)
    self.logo.centerY(self.screen.height)
    self.logo.createSurface()

    self.label.centerX(self.screen.width)
    self.label.marginTop(dotget(1))
    self.label.below(self.logo)

  def changeAlpha(self):
    self.logo.setDotAlpha(self.alpha)
    self.logo.createSurface()

    self.label.surface.set_alpha(self.alpha)

  def listen(self, inputResult):
    if inputResult == GameDefine.COMMAND_BOOST:
      self.pause()

  def step(self):
    if self.active:
      self.changeAlpha()

      self.logo.draw(self.screen.displaysurf)
      self.label.draw(self.screen.displaysurf)

      self.counter += 1

      if self.animState == 1:
        self.alpha += 2

        if self.alpha > 255:
          self.animState = 2
          self.counter = 0

      if self.animState == 2:
        self.counter += 1
        if self.counter > self.screen.fps * 3:
          self.animState = 3

      if self.animState == 3:
        self.alpha -= 2
        if self.alpha <= 0:
          self.pause()
    else:
      self.screen.setWorld(MenuWorld())
      del self

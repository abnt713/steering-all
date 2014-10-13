import dotworld
from src.define import *
from src.dot.entities.dotgoblet import DotGoblet
from src.dot.entities.dotflag import DotFlag
from src.dot.entities.dotheart import DotHeart
from dotgame import *

class MenuWorld(dotworld.DotWorld):

  SELECTION_RACE = 0
  SELECTION_CREDITS = 1
  SELECTION_OPTIONS = 2

  UNSELECTED_ALPHA = 125

  def __init__(self):
    dotworld.DotWorld.__init__(self)
    self.isPressing = False
    self.initEntities()
    self.selected = self.SELECTION_CREDITS

  def onAttachScreen(self):
    self.drawMenu()

  def initEntities(self):
    self.goblet = DotGoblet()
    self.flag = DotFlag()
    self.heart = DotHeart()

  def drawMenu(self):
    self.initEntities()

    selectedItem = self.getSelectedItem()
    selectedItem.setMedium()
    selectedItem.createSurface()
    selectedItem.centerX(self.screen.width)
    selectedItem.centerY(self.screen.height)

    previousItem = self.getPreviousItem()
    previousItem.setDotAlpha(self.UNSELECTED_ALPHA)
    previousItem.setSmall()
    previousItem.createSurface()
    previousItem.marginLeft(dotget(1))
    previousItem.alignLeft()

    previousItem.centerY(self.screen.height)

    nextItem = self.getNextItem()
    nextItem.setDotAlpha(self.UNSELECTED_ALPHA)
    nextItem.setSmall()
    nextItem.createSurface()
    nextItem.marginRight(dotget(1))
    nextItem.alignRight(self.screen.width)

    nextItem.centerY(self.screen.height)


  def getSelectedItem(self):
    if self.selected == self.SELECTION_RACE:
      return self.goblet

    if self.selected == self.SELECTION_CREDITS:
      return self.heart

    if self.selected == self.SELECTION_OPTIONS:
      return self.flag

  def getPreviousItem(self):
    if self.selected == self.SELECTION_RACE:
      return self.flag

    if self.selected == self.SELECTION_CREDITS:
      return self.goblet

    if self.selected == self.SELECTION_OPTIONS:
      return self.heart

  def getNextItem(self):
    if self.selected == self.SELECTION_RACE:
      return self.heart

    if self.selected == self.SELECTION_CREDITS:
      return self.flag

    if self.selected == self.SELECTION_OPTIONS:
      return self.goblet

  def listen(self, inputResult):
    if(inputResult == GameDefine.COMMAND_EXIT):
      self.screen.turnOff()

    if inputResult == GameDefine.COMMAND_RIGHT:
      self.selected = (self.selected + 1) % 3
      self.drawMenu()

    if inputResult == GameDefine.COMMAND_LEFT:
      nextSelect = (self.selected - 1)
      if(nextSelect < 0):
        nextSelect = 2
      self.selected = nextSelect
      self.drawMenu()

    if inputResult == GameDefine.COMMAND_BOOST:
      self.isPressing = True

    if (inputResult == GameDefine.COMMAND_UNBOOST) and self.isPressing == True:
      self.screen.setWorld(DotGame())
      del self

  def step(self):
    self.goblet.draw(self.screen.displaysurf)
    self.flag.draw(self.screen.displaysurf)
    self.heart.draw(self.screen.displaysurf)

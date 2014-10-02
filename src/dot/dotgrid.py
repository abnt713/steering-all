import pygame
from src.define import GameDefine
from src.entities.relativeentity import RelativeEntity

class DotGrid(RelativeEntity):

  def __init__(self, grid, dotRes, dotScale):
    self.dotDim = GameDefine.DOT_DIMENSION * dotScale
    self.dotWidth = len(grid[0])
    self.dotHeight = len(grid)
    self.grid = grid
    self.dotScale = dotScale
    self.dotAlpha = 255
    self.surface = None
    self.dotRes = dotRes
    self.dotImage = None

    RelativeEntity.__init__(self, self.dotDim * self.dotWidth, self.dotDim * self.dotHeight)

    self.setDotScale(dotScale)

  def setDotScale(self, dotScale = 1.0):
    self.dotDim = GameDefine.DOT_DIMENSION * dotScale
    self.width = self.dotDim * self.dotWidth
    self.height = self.dotDim * self.dotHeight

  def setDotAlpha(self, dotAlpha = 255):
    self.dotAlpha = dotAlpha

  def createSurface(self):
    self.initSurface()

    for lineIndex, line in enumerate(self.grid):
      for columnIndex, column in enumerate(line):
        if column == 0:
          pass
        else:
          res = pygame.image.load(self.dotRes[column - 1])
          image = pygame.transform.scale(res, (int(self.dotDim), int(self.dotDim))).convert()
          image.set_alpha(self.dotAlpha)

          posX = columnIndex * self.dotDim
          posY = lineIndex * self.dotDim

          self.drawRectToSurface(image, posX, posY)

  def drawRectToSurface(self, res, surfaceX, surfaceY):
    position = (surfaceX, surfaceY)
    self.surface.blit(res, position)

  def initSurface(self):
    image = pygame.Surface((self.width, self.height), pygame.SRCALPHA, 32)
    self.surface = image.convert_alpha()
    #self.surface.fill((208, 208, 208))

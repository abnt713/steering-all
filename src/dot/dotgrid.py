import pygame
from src.define import GameDefine

class DotGrid:

  def __init__(self, grid, dotRes, dotScale):
    self.dotWidth = len(grid[0])
    self.dotHeight = len(grid)
    self.grid = grid
    self.dotScale = dotScale
    self.surface = None
    self.dotRes = dotRes
    self.dotImage = None
    self.setDotScale(dotScale)

    self.surfaceWidth = self.dotDim * self.dotWidth
    self.surfaceHeight = self.dotDim * self.dotHeight

  def setDotScale(self, dotScale = 1.0):
    self.dotDim = GameDefine.DOT_DIMENSION * dotScale

  def createSurface(self):
    if self.surface == None:
      self.initSurface()

    for lineIndex, line in enumerate(self.grid):
      for columnIndex, column in enumerate(line):
        if column == 0:
          pass
        else:
          dotDim = int(GameDefine.DOT_DIMENSION * self.dotScale)
          res = pygame.image.load(self.dotRes[column - 1])
          image = pygame.transform.scale(res, (dotDim, dotDim))

          posX = columnIndex * self.dotDim
          posY = lineIndex * self.dotDim

          self.drawRectToSurface(image, posX, posY)


  def drawRectToSurface(self, res, surfaceX, surfaceY):
    position = (surfaceX, surfaceY)
    self.surface.blit(res, position)

  def initSurface(self):

    image = pygame.Surface((self.surfaceWidth, self.surfaceHeight), pygame.SRCALPHA, 32)
    self.surface = image.convert_alpha()
    #self.surface.fill((208, 208, 208))

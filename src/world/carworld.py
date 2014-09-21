import world
import pygame
from src.define import *

class CarWorld(world.World):

  def __init__(self, builder, trailsCount, worldWidth, worldHeight, dropspeed):
    world.World.__init__(self, worldWidth, worldHeight, builder)
    self.builder = builder
    self.trailsCount = trailsCount
    self.hero = None
    self.defaultDropspeed = dropspeed
    self.actualDropspeed = dropspeed
    self.enemies = []
    self.gameOn = True

  def getTrailsCount(self):
    return self.trailsCount

  def setHero(self, hero):
    self.hero = hero

  def addEnemy(self, enemy):
    self.enemies.append(enemy);

  def removeEnemy(self, index):
    self.enemies.remove(index)

  def listen(self, inputResult):
    if inputResult == GameDefine.COMMAND_RIGHT:
      if self.hero.activeTrail < (self.trailsCount - 1):
        self.hero.activeTrail += 1
    elif inputResult == GameDefine.COMMAND_LEFT:
      if self.hero.activeTrail > 0:
        self.hero.activeTrail -= 1
    elif inputResult == GameDefine.COMMAND_BOOST:
      self.hero.isBoosting = True
    elif inputResult == GameDefine.COMMAND_UNBOOST:
      self.hero.isBoosting = False
    elif inputResult == GameDefine.COMMAND_EXIT:
      self.gameOn = False

  def step(self):
    self.updateDropspeed()
    self.updateEnemies()
    self.checkCollide()

  def checkCollide(self):
    heroRect = pygame.Rect(self.hero.getCoordinates(), self.hero.getDimensions())
    for enemy in self.enemies:
      enemyRect = pygame.Rect(enemy.getCoordinates(), enemy.getDimensions())
      if heroRect.colliderect(enemyRect):
          self.resetGame()

  def resetGame(self):
    #for enemy in self.enemies:
      #self.enemies.remove(enemy)

    self.hero.score = 0

  def updateEnemies(self):
    for enemy in self.enemies:
      enemy.y += self.actualDropspeed

      if enemy.y > (self.height + enemy.height):
        self.enemies.remove(enemy)

  def updateDropspeed(self):
    self.hero.score += self.actualDropspeed

    if self.hero.boostTime <= 0:
      boostFactor = 1

    if self.hero.isBoosting == True:

      if(self.hero.boostTime == 0):
        self.hero.boostTime = 100


      if self.hero.boostTime < 400:
        self.hero.boostTime += 1

    elif self.hero.isBoosting == False:

      if self.hero.boostTime > 0:
        self.hero.boostTime -= 2

      if self.hero.boostTime < 100:
        self.hero.boostTime = 0

    boostFactor = 1 + (self.hero.boostTime / 100)

    self.actualDropspeed = int(self.defaultDropspeed * boostFactor)

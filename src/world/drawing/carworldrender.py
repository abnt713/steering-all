from worldrender import *
from src.define import GameDefine

import pygame

class CarWorldRenderer(WorldRender):

  def __init__(self, hero, carPadding = 4):
    self.carPadding = carPadding
    self.extraWidth = hero.width * 4
    self.extraHeight = 0
    self.counter = 0
    self.blinkRate = 400
    self.lineWeight = 1

  def render(self, world, displaysurf):
    displaysurf.fill(GameDefine.COLOR_TRAIL);
    self.counter = self.counter + 1
    self.renderTrails(world, displaysurf)
    self.renderInterface(world, displaysurf)
    self.renderHero(world, displaysurf)
    self.renderEnemies(world, displaysurf)

    if self.counter > self.blinkRate:
      self.counter = 0

  def renderEnemies(self, world, displaysurf):
    for enemy in world.enemies:
      coordinates = self.getCarCoordinates(enemy, world, displaysurf)
      enemy.x = coordinates[0]


      img = pygame.image.load("assets/img/carrinho.png")
      displaysurf.blit(img, enemy.getCoordinates())
      #pygame.draw.rect(displaysurf, (0, 0, 0), enemy.getRect())

  def renderTrails(self, world, displaysurf):
    trailWidth = world.width / world.trailsCount
    for x in range(0, world.trailsCount - 1):
      xIndex = x * trailWidth
      xLineBoundary = xIndex + trailWidth
      pygame.draw.rect(displaysurf, GameDefine.COLOR_DIVIDER, ((xLineBoundary - self.lineWeight, 0), (self.lineWeight, world.height)))

  def renderHero(self, world, displaysurf):
    coordinates = self.getCarCoordinates(world.hero, world, False)

    world.hero.x = coordinates[0]
    world.hero.y = coordinates[1]

    img = pygame.image.load("assets/img/carrinho.png")
    displaysurf.blit(img, world.hero.getCoordinates())

    #pygame.draw.rect(displaysurf, (0, 0, 0), ((xIndex, yIndex), (world.hero.width, world.hero.height)))

  def renderInterface(self, world, displaysurf):
    interfaceRect = ((world.width, 0), (self.extraWidth, world.height))
    pygame.draw.rect(displaysurf, GameDefine.COLOR_CONSOLE, interfaceRect)
    separatorRect = ((world.width, 0), (2, world.height))
    pygame.draw.rect(displaysurf, GameDefine.COLOR_DIVIDER, separatorRect)

    canvas = self.renderTitle(world, displaysurf)
    self.renderScore(world, displaysurf, canvas)
    self.renderSpeed(world, displaysurf, canvas)

  def renderTitle(self, world, displaysurf):
    fontSize = int(world.hero.width / 2.5)
    font = pygame.font.Font("assets/fonts/VCR_OSD_MONO.ttf", fontSize)
    text = font.render(GameDefine.GAME_TITLE, True, GameDefine.COLOR_FONT_TITLE)
    textpos = text.get_rect()
    textpos.x = world.width + (self.getExtraWidth() / 2) - (textpos.width / 2)
    textpos.y = world.hero.height / self.carPadding

    xPadding = world.hero.width / self.carPadding
    yPadding = world.hero.height / self.carPadding

    canvasPos = ((textpos.x - xPadding / 2, textpos.y - yPadding / 2), (textpos.width + xPadding, textpos.height + yPadding))
    pygame.draw.rect(displaysurf, GameDefine.COLOR_DIVIDER, canvasPos)

    if self.counter >= 0 and self.counter <= (self.blinkRate / 4) * 3:
      displaysurf.blit(text, textpos)

    return canvasPos

  def renderScore(self, world, displaysurf, canvas):
    pointsX = canvas[0][0]
    pointsY = canvas[0][1] + canvas[1][1] + (world.hero.height / self.carPadding)

    fontSize = int(world.hero.width / 4)
    font = pygame.font.Font(None, fontSize)
    score = int(world.hero.score / 10)
    text = font.render("Score: " + str(score), True, GameDefine.COLOR_FONT_CONSOLE)
    textpos = text.get_rect()

    textpos.x = pointsX
    textpos.y = pointsY

    displaysurf.blit(text, textpos)

  def getCarCoordinates(self, car, world, fromTop = True):
    trailWidth = world.width / world.trailsCount
    xIndex = (trailWidth * car.activeTrail) + (car.width / self.carPadding)
    if not fromTop:
      yIndex = (world.height - car.height) - car.height / (self.carPadding * 2)
    else:
      yIndex = -car.height

    return (xIndex, yIndex)

  def renderSpeed(self, world, displaysurf, canvas):
    pointsX = canvas[0][0]
    pointsY = canvas[0][1] + (canvas[1][1] * 2) + (world.hero.height / self.carPadding)

    fontSize = int(world.hero.width / 4)
    font = pygame.font.Font("assets/fonts/VCR_OSD_MONO.ttf", fontSize)
    text = font.render("Speed", True, GameDefine.COLOR_FONT_CONSOLE)
    textpos = text.get_rect()
    textpos.x = world.width + (self.getExtraWidth() / 2) - (textpos.width / 2)
    textpos.y = pointsY

    displaysurf.blit(text, textpos)

    xPadding = world.hero.width / self.carPadding
    yPadding = world.hero.height / self.carPadding

    speedWidth = canvas[1][0] / 5
    speedHeight = canvas[1][1]
    speedCount = world.actualDropspeed / world.defaultDropspeed

    latestX = pointsX
    speedY = pointsY + textpos.height + yPadding / 2
    for x in xrange(0, speedCount):
      pygame.draw.rect(displaysurf, GameDefine.SPEED_COLORS[x], ((latestX, speedY), (speedWidth, speedHeight)))
      latestX += speedWidth

    bottomRect = ((pointsX, speedY + speedHeight + yPadding / 4), (canvas[1][0], yPadding / 2))
    pygame.draw.rect(displaysurf, GameDefine.COLOR_DIVIDER, bottomRect)

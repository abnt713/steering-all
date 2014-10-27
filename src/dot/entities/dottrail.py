import src.dot.dotcollection
import pygame

from src.dot.entities.dothero import *
from src.dot.entities.dotcar import *
from src.dot.entities.simpledot import *

from src.define import *

class DotTrail(src.dot.dotcollection.DotCollection):

    def __init__(self, screen, score):
        res = [
            "assets/img/gray-brick.png"
        ]

        self.score = score

        self.isActive = True
        self.shouldFall = False
        self.shouldSpawn = False

        self.isBoosting = False
        self.boostTime = 0

        self.screen = screen
        self.defaultFallSpeed = 20
        self.actualFallSpeed = self.defaultFallSpeed

        self.spawnMoment = 0
        self.dropHeight = dotget(1)

        grid = []

        for row in range(0, 20):
            element = []
            for column in range(0, 13):
                element.append(1)
            grid.append(element)

        src.dot.dotcollection.DotCollection.__init__(self, grid, res)
        self.setDotAlpha(55)

        self.hero = DotHero()
        self.hero.y = self.height - self.hero.height
        self.borders = []
        self.addChild(self.hero)

    def listen(self, inputResult):

        if inputResult == GameDefine.COMMAND_BOOST:
            #self.actualFallSpeed = self.defaultFallSpeed * 2
            self.isBoosting = True

        if inputResult == GameDefine.COMMAND_UNBOOST:
            #self.actualFallSpeed = self.defaultFallSpeed
            self.isBoosting = False

        src.dot.dotcollection.DotCollection.listen(self, inputResult)


    def changeScreen(self, screen):
        self.screen = screen

    def getFallMoment(self):
        return self.hero.height * 3

    def getBorderWidth(self):
        return dotget(2)

    def cleanChildren(self):
        for child in self.children:
            if child.y > self.height + (child.height * 2):
                self.removeChild(child)
                del child

    def removeChild(self, child):
        self.children.remove(child)

    def checkCollide(self):
        heroRect = pygame.Rect(self.hero.getCoordinates(), self.hero.getDimensions())
        for child in self.children:
            if child.type == "enemy":
                enemyRect = pygame.Rect(child.getCoordinates(), child.getDimensions())
                if heroRect.colliderect(enemyRect):
                    self.resetGame()

    def resetGame(self):
        self.isActive = False

    def updateFallSpeed(self):
        if self.boostTime <= 0:
            boostFactor = 1

        if self.isBoosting:

            if(self.boostTime == 0):
                self.boostTime = 100

            if self.boostTime < 400:
                self.boostTime += 1

        elif not self.isBoosting:

            if self.boostTime > 0:
                self.boostTime -= 2

            if self.boostTime < 100:
                self.boostTime = 0

        boostFactor = 1 + (self.boostTime / 100)
        self.actualFallSpeed = int(self.defaultFallSpeed * boostFactor)

    def draw(self, displaysurf):
        if self.spawnMoment > self.getFallMoment():
            self.shouldFall = True
            self.spawnMoment = 0

        self.spawnMoment += self.actualFallSpeed
        self.score += self.actualFallSpeed
        self.checkCollide()
        src.dot.dotcollection.DotCollection.draw(self, displaysurf)

        self.updateFallSpeed()
        self.shouldFall = False
        self.cleanChildren()
        print(len(self.children))

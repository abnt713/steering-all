import src.dot.dotcollection
import pygame

from src.dot.dotchild import DotChild
from src.dot.entities.dothero import *
from src.dot.entities.dotcar import *
from src.dot.entities.simpledot import *

from src.define import *


class DotTrail(src.dot.dotcollection.DotCollection):

    def __init__(self, screen, score, level):
        res = [
            "assets/img/gray-brick.png"
        ]

        self.score = score
        self.level = level
        self.levelbase = 1000 * GameDefine.SCORE_DECIMAL
        self.levellimit = self.levelbase * level

        self.isActive = True
        self.shouldFall = False
        self.shouldSpawn = False

        self.isBoosting = False
        self.boostTime = 0

        self.screen = screen
        self.basespeed = 16
        self.defaultFallSpeed = self.basespeed + (self.level * 10)
        self.actualFallSpeed = self.defaultFallSpeed

        self.spawnMoment = 0
        self.dropHeight = dotget(1)

        grid = []

        for row in range(0, 20):
            element = []
            for column in range(0, 11):
                element.append(1)
            grid.append(element)

        src.dot.dotcollection.DotCollection.__init__(self, grid, res)
        self.setDotAlpha(55)

        self.hero = DotHero()
        self.hero.trail = 1
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
        return dotget(1)

    def cleanChildren(self):
        for child in self.children:
            if child.y > self.height + (self.hero.height * 2):
                self.removeChild(child)
                child.onDispose()
                del child

    def removeChild(self, child):
        self.children.remove(child)

    def checkCollide(self):
        heroRect = pygame.Rect(self.hero.getCoordinates(), self.hero.getDimensions())
        for child in self.children:
            childRect = pygame.Rect(child.getCoordinates(), child.getDimensions())
            if heroRect.colliderect(childRect):
                child.notifyCollide(self.hero)
            else:
                child.notifyCollide(None)

    def resetGame(self):
        self.isActive = False

    def updateLevel(self):
        if self.score > self.levellimit and self.level < 15:
            play_sound('assets/music/effects/levelup.wav')
            self.level += 1
            self.levellimit = self.levelbase * self.level
            self.defaultFallSpeed = self.basespeed + (self.level * 10)


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
        self.shouldFall = False
        if self.spawnMoment > self.getFallMoment():
            self.shouldFall = True
            self.spawnMoment = 0

        self.spawnMoment += self.actualFallSpeed

        self.score += self.actualFallSpeed
        self.checkCollide()



        src.dot.dotcollection.DotCollection.draw(self, displaysurf, 2)

        self.updateLevel()
        self.updateFallSpeed()
        self.cleanChildren()

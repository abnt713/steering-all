import dotworld
import menuworld
from src.define import *
from src.draw.dottext import DotText

class GameOver(dotworld.DotWorld):

    def __init__(self, score):
        dotworld.DotWorld.__init__(self)
        self.counter = 0
        self.limit = 400
        self.alpha = 0
        self.animState = 1

        self.label = DotText("Game Over", 32, (0, 0, 0), (255, 255, 255))
        self.scorelabel = DotText("Score: " + str(int(score / GameDefine.SCORE_DECIMAL)), 24, (0, 0, 0), (255, 255, 255))

    def onAttachScreen(self):

        self.label.centerX(self.screen.width)
        self.label.centerY(self.screen.height)

        self.scorelabel.centerX(self.screen.width)
        self.scorelabel.marginTop(dotget(1))
        self.scorelabel.below(self.label)

    def changeAlpha(self):

        self.label.surface.set_alpha(self.alpha)
        self.scorelabel.surface.set_alpha(self.alpha)

    def listen(self, inputResult):
        if inputResult == GameDefine.COMMAND_BOOST:
            self.pause()

    def step(self):
        if self.active:
            self.changeAlpha()

            self.label.draw(self.screen.displaysurf)
            self.scorelabel.draw(self.screen.displaysurf)

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
            self.screen.setWorld(menuworld.MenuWorld())
            del self

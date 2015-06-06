import dotworld
import ufrnsplashworld
from src.define import *
from src.dot.entities.dotpairg import DotPairg
from src.dot.dottext import DotText

import i18n
_ = i18n.language.ugettext


class LogoSplashWorld(dotworld.DotWorld):

    def __init__(self):
        dotworld.DotWorld.__init__(self)
        self.counter = 0
        self.limit = 400
        self.alpha = 0
        self.animState = 1

        self.logo = DotPairg()
        self.label = DotText("PAIRG - Physical Artifacts of Interaction Research Group", 16, (0, 0, 0), (255, 255, 255))
        self.sublabel = DotText(_("Developed by") + " Alison Bento", 16, (0, 0, 0), (255, 255, 255))

    def onAttachScreen(self):
        self.logo.setMedium()
        self.logo.centerX(self.screen.width)
        self.logo.centerY(self.screen.height)
        self.logo.createSurface()

        self.label.centerX(self.screen.width)
        self.label.marginTop(dotget(1))
        self.label.below(self.logo)

        self.sublabel.centerX(self.screen.width)
        self.sublabel.marginTop(dotget(1))
        self.sublabel.below(self.label)

    def changeAlpha(self):
        self.logo.setDotAlpha(self.alpha)
        # self.logo.createSurface()

        self.label.surface.set_alpha(self.alpha)
        self.sublabel.surface.set_alpha(self.alpha)

    def listen(self, inputResult):
        if inputResult == GameDefine.COMMAND_EXIT:
            self.screen.turnOff()

        if inputResult == GameDefine.COMMAND_BOOST:
            self.pause()

    def step(self):
        if self.active:
            self.changeAlpha()

            self.logo.draw(self.screen.displaysurf)
            self.label.draw(self.screen.displaysurf)
            self.sublabel.draw(self.screen.displaysurf)

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
            self.screen.setWorld(ufrnsplashworld.UfrnSplashWorld())
            del self

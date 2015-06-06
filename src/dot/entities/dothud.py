import src.dot.dotcollection
import pygame

from src.dot.entities.dotcar import *
from src.dot.entities.simpledot import *
from src.dot.dottext import *
from src.define import dotget

import i18n
_ = i18n.language.ugettext


class DotHUD(src.dot.dotcollection.DotCollection):
    def __init__(self, lives):
        res = []
        grid = []

        for row in range(0, 20):
            element = []
            for column in range(0, 8):
                element.append(0)
            grid.append(element)

        src.dot.dotcollection.DotCollection.__init__(self, grid, res)

        # Adding the score label
        self.scorelabel = self.scorelabel = DotText(_("Score") + ": 0", 32, (0, 0, 0), (255, 255, 255))
        self.set_score(0)
        self.addChild(self.scorelabel)

        # Speed
        self.speedlabel = DotText(_("Speed") + ": 0", 32, (0, 0, 0), (255, 255, 255))
        self.set_speed(0)
        self.addChild(self.speedlabel)

        # Level
        self.levellabel = DotText(_("Level") + ": 0", 32, (0, 0, 0), (255, 255, 255))
        self.set_level(1)
        self.addChild(self.levellabel)

        # Lives
        self.liveslabel = DotText(_("Lives") + ": " + str(lives), 32, (0, 0, 0), (255, 255, 255))
        self.liveslabel.marginTop(dotget(2))
        self.liveslabel.below(self.levellabel)
        self.liveslabel.centerRelativeX(self)

        self.addChild(self.liveslabel)

        # Signal
        self.signallabel = DotText("Text", 32, (0, 0, 0), (255, 255, 255))
        self.signallabel.marginTop(dotget(3))
        self.signallabel.below(self.liveslabel)
        self.signallabel.centerRelativeX(self)

        self.addChild(self.signallabel)

    def set_score(self, score):
        self.scorelabel.setText(_("Score") + ": " + str(score))
        self.scorelabel.marginTop(dotget(2))
        self.scorelabel.alignTop()
        self.scorelabel.centerRelativeX(self)

    def set_level(self, level):
        self.levellabel.setText(_("Level") + ": " + str(level))
        self.levellabel.marginTop(dotget(1))
        self.levellabel.below(self.speedlabel)
        self.levellabel.centerRelativeX(self)

    def set_speed(self, speed):
        self.speedlabel.setText(_("Speed") + ": " + str(speed))
        self.speedlabel.marginTop(dotget(1))
        self.speedlabel.below(self.scorelabel)
        self.speedlabel.centerRelativeX(self)

    def set_lost(self, lost):
        if lost:
            self.signallabel.setText(_("Signal Lost"))
            self.signallabel.marginBottom(dotget(1))
            self.signallabel.alignBottom(self.height)
            self.signallabel.centerRelativeX(self)
        else:
            self.signallabel.setText("")
            self.signallabel.marginBottom(dotget(1))
            self.signallabel.alignBottom(self.height)
            self.signallabel.centerRelativeX(self)



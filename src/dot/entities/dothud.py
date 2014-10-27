import src.dot.dotcollection
import pygame

from src.dot.entities.dotcar import *
from src.dot.entities.simpledot import *
from src.draw.dottext import *
from src.define import dotget


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
        self.scorelabel = self.scorelabel = DotText("Score: 0", 32, (0, 0, 0), (255, 255, 255))
        self.set_score(0)
        self.addChild(self.scorelabel)

        self.speedlabel = DotText("Speed: 0", 32, (0, 0, 0), (255, 255, 255))
        self.set_speed(0)
        self.addChild(self.speedlabel)

        self.liveslabel = DotText("Lives: " + str(lives), 32, (0, 0, 0), (255, 255, 255))
        self.liveslabel.marginTop(dotget(2))
        self.liveslabel.below(self.speedlabel)
        self.liveslabel.centerRelativeX(self)

        self.addChild(self.liveslabel)


    def set_score(self, score):
        self.scorelabel.setText("Score: " + str(score))
        self.scorelabel.marginTop(dotget(2))
        self.scorelabel.alignTop()
        self.scorelabel.centerRelativeX(self)

    def set_speed(self, speed):
        self.speedlabel.setText("Speed: " + str(speed))
        self.speedlabel.marginTop(dotget(1))
        self.speedlabel.below(self.scorelabel)
        self.speedlabel.centerRelativeX(self)


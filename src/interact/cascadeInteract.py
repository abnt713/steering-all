import baseCascadeInteract

from src.define import *


class CascadeInteract(baseCascadeInteract.BaseCascadeInteract):

    def __init__(self, threadID, cameraIndex, cascade):
        baseCascadeInteract.BaseCascadeInteract.__init__(self, threadID, cameraIndex, cascade)
        self.goingRight = False
        self.goingLeft = False
        self.isBoosting = False

    def checkInteraction(self):
        baseCascadeInteract.BaseCascadeInteract.checkInteraction(self)

        if(self.f_x < self.rightBoundary and not self.goingRight):
            self.listener.listen(GameDefine.COMMAND_RIGHT)
            self.goingLeft = False
            self.goingRight = True

        elif (self.f_x > self.leftBoundary and not self.goingLeft):
            self.listener.listen(GameDefine.COMMAND_LEFT)
            self.goingLeft = True
            self.goingRight = False

        elif (self.f_x <= self.leftBoundary and self.f_x >= self.rightBoundary):
            self.goingLeft = False
            self.goingRight = False

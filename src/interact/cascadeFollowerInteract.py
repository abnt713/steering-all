__author__ = 'alisonbento'

import baseCascadeInteract
from src.define import GameDefine


class CascadeFollowerInteract(baseCascadeInteract.BaseCascadeInteract):

    def __init__(self, threadID, cameraIndex, cascade):
        baseCascadeInteract.BaseCascadeInteract.__init__(self, threadID, cameraIndex, cascade)
        self.active_trail = 0

    def checkInteraction(self):
        baseCascadeInteract.BaseCascadeInteract.checkInteraction(self)

        if self.f_x < self.rightBoundary and self.active_trail != 1:
            self.listener.listen(GameDefine.COMMAND_TRAIL_RIGHT)
            self.active_trail = 1

        elif self.f_x > self.leftBoundary and self.active_trail != -1:
            self.listener.listen(GameDefine.COMMAND_TRAIL_LEFT)
            self.active_trail = -1

        elif self.f_x < self.leftBoundary and self.f_x > self.rightBoundary and self.active_trail != 0:
            self.listener.listen(GameDefine.COMMAND_TRAIL_CENTER)
            self.active_trail = 0

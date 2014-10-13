import evtInteract
import pygame
import sys

from src.define import *
from pygame.locals import *

class MouseInteract(evtInteract.EvtInteract):

  def checkInteraction(self):
    for event in self.events:

      if event.type == QUIT:
        pygame.quit()
        sys.exit()

      if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 3:
          self.listener.listen(GameDefine.COMMAND_RIGHT)

        if event.button == 1:
          self.listener.listen(GameDefine.COMMAND_LEFT)

        if event.button == 4:
          self.listener.listen(GameDefine.COMMAND_BOOST)

        if event.button == 5:
          self.listener.listen(GameDefine.COMMAND_UNBOOST)

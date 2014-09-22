import interact
import pygame
import sys

from src.define import *
from pygame.locals import *

class MouseInteract(interact.Interact):

  def checkInteraction(self):
    events = pygame.event.get()
    for event in events:

      if event.type == QUIT:
        pygame.quit()
        sys.exit()

      if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 3:
          self.listener.listen(GameDefine.COMMAND_RIGHT)

        if event.button == 2:
          self.listener.listen(GameDefine.COMMAND_LEFT)

import evtInteract
import pygame
import sys

from src.define import *
from pygame.locals import *

class KeyboardInteract(evtInteract.EvtInteract):

  def __init__(self):
    evtInteract.EvtInteract.__init__(self)
    self.goingRight = False
    self.goingLeft = False

  def checkInteraction(self):
    for event in self.events:

      if event.type == QUIT:
        pygame.quit()
        sys.exit()

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT and not self.goingLeft:
          self.listener.listen(GameDefine.COMMAND_LEFT)
          self.goingLeft = True

        if event.key == pygame.K_RIGHT and not self.goingRight:
          self.listener.listen(GameDefine.COMMAND_RIGHT)
          self.goingRight = True

        if event.key == pygame.K_SPACE:
          self.listener.listen(GameDefine.COMMAND_BOOST)

        if event.key == pygame.K_ESCAPE:
          self.listener.listen(GameDefine.COMMAND_EXIT)

      if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
          self.goingLeft = False

        if event.key == pygame.K_RIGHT:
          self.goingRight = False

        if event.key == pygame.K_SPACE:
          self.listener.listen(GameDefine.COMMAND_UNBOOST)

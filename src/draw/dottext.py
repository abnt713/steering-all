import pygame

from src.entities.relativeentity import RelativeEntity

class DotText(RelativeEntity):

  def __init__(self, text, size = 32, textColor = (0, 0, 0), bgColor = (255, 255, 255), font = "assets/fonts/VCR_OSD_MONO.ttf"):
    fontObj = pygame.font.Font(font, size)
    textObj = fontObj.render(text, True, textColor)

    textWidth = textObj.get_width()
    textHeight = textObj.get_height()

    RelativeEntity.__init__(self, textWidth, textHeight)
    surf = pygame.Surface(fontObj.size(text), pygame.SRCALPHA, 32)
    surf.fill(bgColor)
    self.surface = surf.convert()
    self.surface.blit(textObj, (0,0))

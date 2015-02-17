import pygame

from src.entities.relativeentity import RelativeEntity

class DotText(RelativeEntity):

    def __init__(self, text, size=32, textColor=(0, 0, 0), bgColor=(255, 255, 255), font="assets/fonts/VCR_OSD_MONO.ttf"):
        self.surface = None
        self.parent = None
        self.setText(text, size, textColor, bgColor, font)

    def setText(self, text, size=32, textColor=(0, 0, 0), bgColor=(255, 255, 255), font="assets/fonts/VCR_OSD_MONO.ttf"):
        if self.surface is not None:
            self.surface.fill(bgColor)

        fontObj = pygame.font.Font(font, size)
        textObj = fontObj.render(text, True, textColor)

        self.width = textObj.get_width()
        self.height = textObj.get_height()

        RelativeEntity.__init__(self, self.width, self.height)
        surf = pygame.Surface(fontObj.size(text), pygame.SRCALPHA, 32)
        surf.fill(bgColor)
        self.surface = surf.convert()
        self.surface.blit(textObj, (0, 0))

    def attachToCollection(self, parent):
        self.parent = parent

    def step(self):
        pass

    def createSurface(self):
        pass




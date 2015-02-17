from src.dot.entities.dotgoblet import DotGoblet
from src.dot.entities.dotflag import DotFlag
from src.dot.entities.dotheart import DotHeart
from src.dot.dottext import DotText
from src.utils.musiclibrary import play_sound
from dotgame import *


class MenuWorld(dotworld.DotWorld):

    SELECTION_RACE = 0
    SELECTION_CREDITS = 1
    SELECTION_OPTIONS = 2

    UNSELECTED_ALPHA = 125

    def __init__(self):
        dotworld.DotWorld.__init__(self)

        self.label = DotText("", 32)
        self.logo = DotText("", 32, (0, 0, 0), (255, 255, 255), "assets/fonts/8-BIT-WONDER.ttf")
        self.goblet = DotGoblet()
        self.flag = DotFlag()
        self.heart = DotHeart()

        self.possibleLabels = {
            self.SELECTION_RACE: "Iniciar corrida",
            self.SELECTION_CREDITS: "Creditos",
            self.SELECTION_OPTIONS: "Opcoes"
        }
        self.isPressing = False
        self.selected = self.SELECTION_RACE

    def onAttachScreen(self):
        self.drawMenu()

    def drawMenu(self):
        self.goblet = DotGoblet()
        self.flag = DotFlag()
        self.heart = DotHeart()

        self.logo.setText("Steering All", 32, (0, 0, 0), (255, 255, 255), "assets/fonts/8-BIT-WONDER.ttf")
        self.logo.x = dotget(3)
        self.logo.centerX(self.screen.width)

        selectedItem = self.getSelectedItem()
        selectedItem.setMedium()
        selectedItem.createSurface()
        selectedItem.centerX(self.screen.width)
        selectedItem.centerY(self.screen.height)

        self.label.setText(self.possibleLabels[self.selected], 32)
        self.label.marginTop(dotget(1))
        self.label.below(selectedItem)
        self.label.centerX(self.screen.width)

        previousItem = self.getPreviousItem()
        previousItem.setDotAlpha(self.UNSELECTED_ALPHA)
        previousItem.setSmall()
        previousItem.createSurface()
        previousItem.marginLeft(dotget(1))
        previousItem.alignLeft()

        previousItem.centerY(self.screen.height)

        nextItem = self.getNextItem()
        nextItem.setDotAlpha(self.UNSELECTED_ALPHA)
        nextItem.setSmall()
        nextItem.createSurface()
        nextItem.marginRight(dotget(1))
        nextItem.alignRight(self.screen.width)

        nextItem.centerY(self.screen.height)


    def getSelectedItem(self):
        if self.selected == self.SELECTION_RACE:
            return self.goblet

        if self.selected == self.SELECTION_CREDITS:
            return self.heart

        if self.selected == self.SELECTION_OPTIONS:
            return self.flag

    def getPreviousItem(self):
        if self.selected == self.SELECTION_RACE:
            return self.flag

        if self.selected == self.SELECTION_CREDITS:
            return self.goblet

        if self.selected == self.SELECTION_OPTIONS:
            return self.heart

    def getNextItem(self):
        if self.selected == self.SELECTION_RACE:
            return self.heart

        if self.selected == self.SELECTION_CREDITS:
            return self.flag

        if self.selected == self.SELECTION_OPTIONS:
            return self.goblet

    def listen(self, inputResult):
        if inputResult == GameDefine.COMMAND_EXIT:
            self.screen.turnOff()

        if inputResult == GameDefine.COMMAND_RIGHT:
            play_sound('assets/music/effects/select.wav')
            self.selected = (self.selected + 1) % 3
            self.drawMenu()

        if inputResult == GameDefine.COMMAND_LEFT:
            play_sound('assets/music/effects/select.wav')
            nextSelect = (self.selected - 1)
            if(nextSelect < 0):
                nextSelect = 2
            self.selected = nextSelect
            self.drawMenu()

        if inputResult == GameDefine.COMMAND_BOOST:
            play_sound('assets/music/effects/levelup.wav')
            self.isPressing = True

        if (inputResult == GameDefine.COMMAND_UNBOOST) and self.isPressing == True:
            self.screen.setWorld(DotGame(3, 0, 1, True))
            del self

    def step(self):
        self.logo.draw(self.screen.displaysurf)
        self.goblet.draw(self.screen.displaysurf)
        self.flag.draw(self.screen.displaysurf)
        self.heart.draw(self.screen.displaysurf)
        self.label.draw(self.screen.displaysurf)

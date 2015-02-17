import dotworld
import gameover

from src.spawner.dotcarspawner import *
from src.spawner.dotborderspawner import *
from src.dot.entities.dothud import DotHUD


from src.dot.entities.dottrail import DotTrail


class DotGame(dotworld.DotWorld):
    def __init__(self, lives=3, score=0, level=1, startMusic = False):
        self.startMusic = startMusic
        self.has_signal = True
        self.score = score
        self.lives = lives
        self.level = level
        self.hud = DotHUD(lives)
        self.enemySpawner = None
        dotworld.DotWorld.__init__(self)

    def onAttachScreen(self):
        self.trail = DotTrail(self.screen, self.score, self.level)
        self.trail.createSurface()
        self.trail.alignTop()
        self.trail.centerX(self.screen.width)

        self.hud.createSurface()
        self.hud.alignLeft()
        self.hud.alignTop()

        self.enemySpawner = DotCarSpawner(3, 2)
        self.borderSpawner = DotBorderSpawner(1)

        if self.startMusic:
            pygame.mixer.music.load("assets/music/racing-theme.mp3")
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1, 0.0)

    def listen(self, inputResult):
        if inputResult == GameDefine.COMMAND_EXIT:
            self.screen.turnOff()

        if inputResult == GameDefine.COMMAND_SIGNAL_LOST:
            self.has_signal = False

        if inputResult == GameDefine.COMMAND_SIGNAL_FOUND:
            self.has_signal = True

        self.trail.listen(inputResult)

    def step(self):
        self.enemySpawner.spawn(self.trail)
        self.borderSpawner.spawn(self.trail)

        self.trail.draw(self.screen.displaysurf)

        self.hud.set_score(self.trail.score / GameDefine.SCORE_DECIMAL)
        self.hud.set_speed(self.trail.actualFallSpeed / self.trail.defaultFallSpeed)
        self.hud.set_level(self.trail.level)
        self.hud.set_lost(not self.has_signal)
        self.hud.draw(self.screen.displaysurf)

        if self.lives <= 0:
            self.screen.setWorld(gameover.GameOver(self.trail.score))
            del self

        elif not self.trail.isActive:
            self.screen.setWorld(DotGame(self.lives - 1, self.trail.score, self.trail.level))
            del self

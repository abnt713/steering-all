class WorldBuilder:

  fps = 60

  def addSpawner(self, spawner):
    self.spawner.addSpawner(spawner)

  def setSpawnerCollector(self, spawnerCollection):
    self.spawner = spawnerCollection

  def setDisplaysurf(self, displaysurf):
    self.displaysurf = displaysurf

  def setWorld(self, world):
    self.world = world

  def setWorldRenderer(self, renderer):
    self.worldRenderer = renderer

  def step(self):
    self.spawner.update(self.world)
    self.world.update()
    self.renderWorld()

  def renderWorld(self):
    self.worldRenderer.render(self.world, self.displaysurf)

  def getAdjustedDisplaySize(self):
    width = self.world.width + self.worldRenderer.getExtraWidth()
    height = self.world.height + self.worldRenderer.getExtraHeight()

    return (width, height)

  def dispose(self):
    pass

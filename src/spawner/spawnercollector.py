class SpawnerCollector:

  def __init__(self):
    self.spawners = []

  def addSpawner(self, spawner):
    spawner.setCollector(self)
    self.spawners.append(spawner)

  def update(self, world):
    for spawner in self.spawners:
      spawner.spawn(world)

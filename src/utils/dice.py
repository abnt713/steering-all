import random

class PercentChance:

  def __init__(self, chance):
    self.chance = chance

  def setChance(self, chance):
    self.chance = chance

  def roll(self):
    selected = random.randint(0, 100)
    if selected < self.chance:
      return True
    else:
      return False


class Dice:

  def __init__(self, start, end):
    self.start = start
    self.end = end

  def roll(self):
    return random.randint(self.start, self.end)

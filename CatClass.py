class Cat:

  def __init__(self, color, name, isMale, meow):
    self.color = color
    self.name = name
    self.isMale = isMale
    self.age = 0

  def sleep(self, duration):
    print(self.name + "slept for " + self(duration) + "minutes.")

  def ager(self):
    self.age += 1

  def noise(self):
    print(self.meow)

  def getAge(self):
    return self.age

  def getName(self):
    return self.name

  def setName(self):
    self.name = newName

Buddy = Cat("black", "Buddy", True, "Meow!")
Buddy.sleep(120)
Buddy.meow()

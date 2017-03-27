class Rectangle:

  def __init__(self, length, width):
      self.length = length
      self.width = width

  def getlenth(self):
      return self.length

  def getwidth(self):
      return self.width

  def isSquare(self):
      if self.width != self.length:
          return False
      else:
          return True

  def area(self):
      area = self.width * self.length
      return area

A = Rectangle(10, 12)
print(A.isSquare())
print(A.area())

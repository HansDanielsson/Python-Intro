class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def getxy(self):
    return self.x, self.y


class Circle:
  def __init__(self, x, y, r):
    self.p = Point(x, y)
    self.r = r
    self.m = False
  
  def moveto(self, x, y):
    self.p = Point(x, y)
    self.m = True
  
  def ismoved(self):
    return self.m

p1 = Circle(12, 4, 5)
p2 = Circle(5, 2, 10)

p2.moveto(10,10)

print(p2.ismoved())

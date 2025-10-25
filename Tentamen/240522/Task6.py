class Circle:
  def __init__(self, x = 0, y = 0, r = 0):
    self.x = x
    self.y = y
    self.r = r
    
  def new(self, r):
    ny = Circle(self.x, self.y, r)
    return ny
  
  def sync(self, org):
    if isinstance(org, Circle):
      self.x = org.x
      self.y = org.y
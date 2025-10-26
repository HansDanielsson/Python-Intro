class UValue:
  def __init__(self, v = 0.0, u = 0.0):
    self._v = v
    self._u = u
  
  def addacc(self, other):
    if not isinstance(other, UValue):
      raise NotImplementedError("addacc add UValue types")
    self._v += other._v
    self._u += other._u
    
  def add(self, other):
    if not isinstance(other, UValue):
      raise NotImplementedError("add UValue types")
    return UValue(self._v + other._v, self._u + other._u)
  
  def getvalue(self):
    return (self._v, self._u)

t1 = UValue(34.6, 1.3)
t2 = UValue(15.2, 1.5)
t1.addacc(t2)
print(t1._v, t1._u)
t3 = t1.add(t2)
print(t1._v, t1._u)
print(t2._v, t2._u)
print(t3._v, t3._u)

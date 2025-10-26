class Interval:
  def __init__(self,start=0, stop=0):
    self._s = start
    self._e = stop
    if stop < start:
      self._e = start
  
  def contains(self, nr):
    return (self._s <= nr) and (nr <= self._e)
  
  def newinterval(self):
    return Interval(self._s, self._e)
  
  def containsinterval(self, other):
    return (other._s > self._s) and (other._e < self._e)
  
  def getstart(self):
    return self._s

s1 = Interval(1,10)
s2 = Interval(4,7)
print(s1.getstart())
print(s2.getstart())
print(s1.contains(5))
print(s1.contains(20))
s3 = s1.newinterval()
print(s1.containsinterval(s2))

class Logger:
  def __init__(self, maxl):
    self.m = maxl
    self.i = 0
    self.e = []
  
  def add(self, e):
    if self.m < self.i:
      raise ValueError("log full")
    self.e.append(e)
    self.i += 1
  
  def get(self, pos):
    if pos < 0 or pos > self.i:
      raise ValueError("Index error")
    return self.e[self.i - pos - 1]
  
  def combine(self, other):
    for e in other.e:
      if self.m < self.i:
        raise ValueError("Log full")
      self.e.append(e)
      self.i += 1

s1 = Logger(10)
s1.add([1,2,3])
s1.add("hejsan")
s1.add(34)
print(s1.get(0))
print(s1.get(1))
print(s1.get(2))

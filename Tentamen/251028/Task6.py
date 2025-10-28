class Message:
  def __init__(self,msg,i):
    self._msg = msg
    self.ital = int(i)
  
  def inherit(self, ital):
    return Message(self._msg, ital)
  
  def add(self, msg):
    self.ital += msg.ital
  
  def getvalue(self):
    return int(self.ital)
  
  def getname(self):
    return str(self._msg)

p1 = Message("namn1", 10)
p2 = Message("Namn2", 20)

p3 = p2.inherit(100)

print(p1.getname())
print(p1.getvalue())
print(p2.getname())
print(p2.getvalue())
print(p3.getname())
print(p3.getvalue())

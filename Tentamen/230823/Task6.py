class KeyValuePair:
  def __init__(self, key=0, value=0):
    self._k = key
    self._v = value
  
  def setvalue(self, value = 0):
    self._v = value
  
  def getkeyvalue(self):
    return self._k, self._v
  
  def newvalue(self, value=0):
    return KeyValuePair(self._k, value)

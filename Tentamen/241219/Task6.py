class Dynstring:
  def __init__(self, initial_string=""):
    self._string = initial_string
    
  def copy(self):
    return Dynstring (self._string)
    
  def add(self, other):
    if not isinstance(other, Dynstring):
      raise TypeError("Argument must be an instance of dynstring")
    self._string += other._string

  def __str__(self):
    return self._string

# Example usage:

str1 = Dynstring("Hello")
str3 = str1.copy()
str2 = Dynstring(" World")
str1.add(str2)

print(str1)  # Output: Hello World
print(str3)  # Output: Hello
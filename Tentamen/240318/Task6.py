class Complex:
  def __init__(self, real = 0.0, imag = 0.0):
    self.real = real
    self.imag = imag
        
  def re(self):
    return float(self.real)

  def im(self):
    return float(self.imag)

  def __add__(self, other):
    if not isinstance(other, Complex):
      return NotImplemented("Can only add Complex to Complex")
    return Complex(self.real + other.real, self.imag + other.imag)
      
  def add(self, other):
    if not isinstance(other, Complex):
      raise TypeError("Can only add Complex to Complex")
    return Complex(self.real + other.real, self.imag + other.imag)

  def __str__(self):
    return f"{self.real} + {self.imag}i"
      
t1 = Complex(2.5, 3.5)
print(t1)
t2 = Complex(1.5, 2.5)
print(t2)
t3 = t1 + t2
t4 = t1.add(t2)
print(t1)
print(t2)
print(t3)
print(t4)
print(t1.re())
print(t1.im())

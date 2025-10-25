class Pstring:
    def __init__(self, initial_string=""):
        self._parts = initial_string

    def prefix(self, n):
        return Pstring(self._parts[:n])
    
    def gets(self):
        return self._parts

    def add(self, other):
        if isinstance(other, Pstring):
            self._parts += other._parts
        else:
            raise TypeError("add() argument must be Pstring")

s1 = Pstring("Hello")
print(s1.gets())

s2 = Pstring("World")
print(s2.gets())

s3 = s1.prefix(4)
print(s1.gets())
print(s3.gets())

s1.add(s2)
print(s1.gets())
print(s2.gets())

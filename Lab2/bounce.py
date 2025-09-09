"""
  bounce(n):This function prints the numbers from n down to 0 and then back up to n.
  bounce2(n):This function does the same as bounce but uses iteration instead of recursion.
"""
def bounce(n):
  if (n >= 0):
    print(n)
    bounce(n - 1)
    if (n != 0): # to avoid printing 0 twice
      print(n)
      
def bounce2(n):
  index = n
  while index >= 0:
    print(index)
    index -= 1
  index = 1
  while index <= n:
    print(index)
    index += 1
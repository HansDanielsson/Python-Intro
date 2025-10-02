import sys
sys.path.append('../Lab2')
from bounce import bounce
from tvarsumman import tvarsumman
from derivative import testfunc

def dobounce():
  n = int(input("Ange n: "))
  bounce.bounce(n)

def dotvarsumman():
  n = int(input("Ange ett heltal: "))
  result = tvarsumman.tvarsumman(n)
  print(f"Tvärsumman av {n} är {result}")

def donewtonraphson():
  n = float(input("Ange ett tal: "))
  result = derivative.testfunc(n)
  print(f"Newton-Raphson för {n} är {result}")

def main():
  meny = True
  while meny:
    print("1. Bounce")
    print("2. Tvärsumma")
    print("3. Newton-Raphson")
    print("4. Avsluta")
    val = input("Välj ett alternativ (1-4): ")

    if val in ['1', '2', '3']:
      
      if val == '1':
        dobounce()
      elif val == '2':
        dotvarsumman()
      elif val == '3':
        donewtonraphson()
    elif val == '5':
      meny = False
      print("Avslutar programmet.")
    else:
      print("Ogiltigt val, försök igen.")
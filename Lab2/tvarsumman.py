import math
def tvarsumman(n):
  heltalet = math.trunc(n / 10) # remove the last digits
  entalet = n % 10
  if (heltalet != 0):
    return entalet + tvarsumman(heltalet)
  return entalet

def tvarsumman2(n):
  summa = 0
  while n != 0:
    heltalet = math.trunc(n / 10) # remove the last digits
    entalet = n % 10
    summa += entalet
    n = heltalet
  return summa
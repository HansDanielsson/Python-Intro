def readintlist(filename, x):
  intlst=[]
  try:
    f=open(filename,"r")
    for line in f:
      try:
        tal = int(line)
      except:
        tal = x
      finally:
        intlst.append(tal)
    f.close()
  except:
    raise ValueError("Filename error")
  return intlst

def readui():
  try:
    lst=readintlist(input("Ange filnamn: "), 0)
  except:
    lst = []
  print(lst)

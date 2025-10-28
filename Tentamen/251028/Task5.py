def readintlist(filename):
  try:
    f = open(filename,"r") # x
  except:
    return []
  try:
    lst=[]
    for line in f:
      lst.append(int(line))
    f.close()
    return lst
  except:
    raise ValueError

def readui():
  try:
    lst=readintlist(input("Ange filnamn: "))
    print(lst)
  except:
    print("filfel!")

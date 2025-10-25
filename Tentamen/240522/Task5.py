def readlist(filename):
  lst = []
  try:
    f = open(filename,"r")
    for line in f:
      lst.append(float(line))
    f.close()
  except Exception:
    raise ValueError("Filen saknas.")
  return lst

def readui():
  try:
    print(readlist(input("Ange filnamnet: ")))
  except ValueError as e:
    print(e)
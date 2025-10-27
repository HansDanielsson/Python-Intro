def loadint(fname):
  try:
    f = open(fname,"r")
    v = int(f.readline())
    f.close()
    return v
  except:
    raise ValueError("Read error")

def example():
  try:
    print(loadint(input("Ange filnamn: ")))
  except Exception as e:
    print(e)

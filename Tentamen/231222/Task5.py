def fileread(filename):
  try:
    f1 = open(filename,"r")
  except:
    raise FileExistsError("Filen finns ej")

  rad1 = f1.readline()
  rad2 = f1.readline()
  f1.close()
  if not rad1 or not rad2:
    return 0
  if abs(float(rad2)) < 1e-10:
    return float(rad1)
  return float(rad1) / float(rad2)

def filetest():
  try:
    div = fileread(input("Ange filnamn: "))
    print("Div = ", div)
  except Exception as e:
    print(e)

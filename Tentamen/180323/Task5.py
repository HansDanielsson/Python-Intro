def save(fname, svalue):
  try:
    f = open(fname,"x")
    f.write(svalue)
    f.close()
  except:
    raise IOError("File already exists")

def app():
  try:
    save(input("Ange filnamn: "), input("Ange value: "))
  except Exception as e:
    print(e)

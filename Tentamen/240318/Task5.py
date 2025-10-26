def filewrite(filename, lst):
  try:
    f = open(filename,"r+")
    for e in lst:
      f.write(str(e) + "\n")
    f.close()
  except Exception as e:
    raise FileExistsError("File exists")
  
def writeui():
  try:
    filewrite(input("Ange filnamnet: "), range(int(input("Ange ett heltal: "))))
  except FileExistsError as fe:
    print(fe)

def fileaddint(filename, value):
  oldvalue = 0
  try:
    f = open(filename, "r")
    rad = f.readline()
    f.close()
    try:
      oldvalue = int(rad)
    except:
      raise FileNotFoundError("File error")
  except:
    raise FileNotFoundError("File error")
  finally:
    f = open(filename, "w")
    f.write(str(oldvalue + value))
    f.close()
  
def addui():
  try:
    fileaddint(input("Ange filnamn: "), int(input("Ange value: ")))
  except Exception as e:
    print(e)
  print("Done")

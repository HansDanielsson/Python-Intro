def writetofile(filename, slst):
  try:
    f = open(filename,"x")
    for e in slst:
      if e == "":
        raise ValueError("Empty string")
      f.write(e+"\n")
    f.close()
  except FileExistsError:
    print("File exists")
  except Exception as e:
    print("Error:", e)

def inputlist():
  slst = []
  while True:
    s = input()
    if s=="exit":
      break
    slst.append(s)
  return slst

def writeui():
  slst = inputlist()
  filename = input("Enter filename: ")
  writetofile(filename, slst)
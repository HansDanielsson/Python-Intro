def writeintlist(filename, intlist):
  try:
    f = open(filename, "x")
    for e in intlist:
      f.write(str(e) + "\n")
    f.close()
  except Exception as e:
    print("File already exists")

def inputint():
  lst = []
  while True:
    s=input("Number: ")
    if s=="":
      return lst
    lst.append(int(s))

def intui():
  lst = inputint()
  filename = input("Filename: ")
  writeintlist(filename, lst)
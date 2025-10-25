numlst = [5,4,3,2,1]
b = numlst[0] == len(numlst)
if numlst[1] < numlst[2] and b:
  print("Forsta")
elif not b or len(numlst) > numlst[2]:
  print("Andra")
else:
  print("Tredje")
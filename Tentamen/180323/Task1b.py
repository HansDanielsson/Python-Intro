ls = [[6],[5],[4]]
b=3
if b<len(ls[2]) or len(ls)<b:
  print("Första")
elif ls[1][0] > ls[0][0]:
  print("Andra")
else:
  print("Tredje")

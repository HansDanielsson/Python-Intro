d = {}
d[8] = 0
d[0] = 8
while d[0] > 0:
  print(d[0])
  d[d[0]] = d[0] - 1
print("a terminerar")

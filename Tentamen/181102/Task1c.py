ls=[9,8,7]
i =0
while i<len(ls)-1:
  ls[i] = ls[i] - ls[i+1]
  print(ls)
  i+=1

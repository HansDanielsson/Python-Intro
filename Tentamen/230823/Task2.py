def isweap(lst):
  for i in range(int(len(lst)/2.0)):
    if lst[i] >= lst[2*i+1]:
      return False
  return True

print(isweap([0,1,2,3,4,15,16,7,8,9,10,11]))

def zipmultiply(lst1, lst2):
  i = 0
  while i<len(lst1) and i<len(lst2):
    lst1[i] = lst1[i]*lst2[i]
    i +=1

a0 = [2,5,1,3]
b0 = [1,2,4,3]
zipmultiply(a0,b0)
print(a0)

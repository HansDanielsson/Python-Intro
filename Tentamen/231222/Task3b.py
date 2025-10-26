def zipmultiply1(lst1, lst2):
  i = 0
  lst3 = lst1[:]
  while i<len(lst1) and i<len(lst2):
    lst3[i] = lst1[i] * lst2[i]
    i+=1
  return lst3

a1 = [2,5,1,3]
b1 = [1,2,4,3]
c1 = zipmultiply1(a1,b1)
print(c1)
c1[0] = 99
print(a1)

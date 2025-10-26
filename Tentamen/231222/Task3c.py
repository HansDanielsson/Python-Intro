def zipmultiply2(lst1, lst2):
  i = 0
  lst3 = lst1
  while i<len(lst1) and i<len(lst2):
    lst1[i] = lst1[i] * lst2[i]
    i += 1
  return lst3

a2 = [2,5,1,3]
b2 = [1,2,4,3]
c2 = zipmultiply2(a2,b2)
print(a2, b2, c2)
c2[0] = 99
print(a2)

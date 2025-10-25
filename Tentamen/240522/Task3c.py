def addcount3(lst):
  i = 0
  for e in lst:
    lst[i] = e + i
  return lst

ls3a = [2, 4, 1, 6]
ls3b = addcount3(ls3a)
print(ls3a)
ls3a[0]=99
print(ls3a)
print(ls3b)
def addcount2(lst):
  lst2 = lst
  i = 0
  for e in lst:
    lst2[i] = e + i
  return lst2

lst1a = [2, 4, 1, 6]
lst1b = addcount2(lst1a)
print(lst1a)
lst1a[0] = 99
print(lst1a)
print(lst1b)
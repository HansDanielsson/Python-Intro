def addcount1(lst):
  lst2 = []
  i = 0
  for e in lst:
    lst2.append(e + i)
  return lst2

lst1a = [2, 4, 1, 6]
lst1b = addcount1(lst1a)
lst1a[0] = 99
print(lst1a)
print(lst1b)
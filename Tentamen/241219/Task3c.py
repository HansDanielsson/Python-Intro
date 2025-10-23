def setminus2(lst, subtractlist):
  i=0
  while i<len(lst):
    if lst[i] in subtractlist:
      del lst[i]
    else:
      i+=1
  return lst

lst2a = [3, 2, 5, 7]
lst2b = [2, 5]
lst2c = setminus2(lst2a, lst2b)
lst2a[0] = 99  # Modify lst2a to show it is the same object as lst2c

print(lst2a)  # Should print [99, 7]
print(lst2b)  # Should print [2, 5]
print(lst2c)  # Should print [99, 7]
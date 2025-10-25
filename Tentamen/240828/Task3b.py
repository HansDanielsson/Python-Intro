def diff1(lst1, lst2):
  i = 0
  lst3 = lst1
  while i<len(lst1) and i<len(lst2):
    lst1[i] = lst1[i] - lst2[i]
    i += 1
  return lst3

lst1a = [3, 4, 3, 6]
lst1b = [1, 1, 2, 3]
lst1c = diff1(lst1a, lst1b)
lst1a[0] = 99

print(lst1a)  # Expected output: [2, 3, 1, 3]
print(lst1b)  # Expected output: [1, 1, 2, 3] 
print(lst1c)  # Expected output: [2, 3, 1, 3]

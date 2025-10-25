def diff0(lst1, lst2):
  i = 0
  while i<len(lst1) and i<len(lst2):
    lst1[i] = lst1[i] - lst2[i]
    i += 1

lst0a = [3, 4, 3, 6]
lst0b = [1, 1, 2, 3]
diff0(lst0a, lst0b)
print(lst0a)  # Expected output: [2, 3, 1, 3]
print(lst0b)  # Expected output: [1, 1, 2, 3]
def frequency(lst, x):
  count = 0
  i = 0
  while i < len(lst):
    if lst[i] == x:
      count += 1
    i += 1
  return count
print(frequency([1, 2, 3, 2, 4, 2], 2))  # Example usage
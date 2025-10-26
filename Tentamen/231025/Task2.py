def ispow2list(lst):
  i = 0
  while i < len(lst):
    if lst[i] != 2**i:
      return False
    i += 1
  return True

print(ispow2list([1, 2, 4, 8]))
print(ispow2list([1,2,4,8,9]))

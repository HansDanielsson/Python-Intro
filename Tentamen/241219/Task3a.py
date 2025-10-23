def setminus0(lst, subtractlst):
  i=0
  while i < len(lst):
    if lst[i] in subtractlst:
      del lst[i]
    else:
      i += 1

lst0a = [3, 2, 5, 7]
lst0b = [2, 5]
setminus0(lst0a, lst0b)
print(lst0a)  # Should print [3, 7]
print("Ny rad ")
print(lst0b)
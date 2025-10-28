def occur(lst, e):
  i = 0
  while i < len(lst):
    if lst[i] == e:
      return i
    i += 1
  return -1

print(occur([1,2,3,4,5,6,2,4], 5))

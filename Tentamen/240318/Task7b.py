def listrec(lst):
  if len(lst) == 0:
    return []
  if lst[0] % 2 == 0:
    return [int(lst[0] / 2)] + listrec(lst[1:])
  return [3 * lst[0] + 1] + listrec(lst[1:])
  
print(listrec([2,3,8,1]))

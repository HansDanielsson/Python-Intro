def listrec(lst):
  if not lst:
    return []
  one = int(lst[0])
  rest = []
  for e in lst:
    if e != one:
      rest.append(e)
  if one % 2 == 0:
    result = int(one / 2)
  else:
    result = 3 * one + 1
  return [result] + listrec(rest)

print(listrec([2,3,8,1]))

def unique(lst):
  if not lst:
    return []
  firstlst = lst[0]
  lastlst = unique(lst[1:])
  if firstlst not in lastlst:
    lastlst.append(firstlst)
  return lastlst
lstuni = unique([1, 2, 1, 3, 9, 2, 7, 6, 8, 3]),
print(lstuni)
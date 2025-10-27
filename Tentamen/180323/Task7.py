def flatten(lstlst):
  if len(lstlst) == 0:
    return []
  else:
    dela = lstlst[0]
    delb = lstlst[1:]
    return dela + flatten(delb)
print(flatten([[1,3,5], [4,1], [8,9,3]]))

def lenfilter(lstlst):
  if len(lstlst) == 0:
    return []
  return [len(lstlst[0])] + lenfilter(lstlst[1:])
  

print(lenfilter([[1,2,3],[],[4],[5,6]]))

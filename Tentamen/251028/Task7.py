def flatspecial(lstlst):
  if len(lstlst)==0:
    return [0]
  
  dela = lstlst[0]
  delb = lstlst[1:]
  
  if len(dela) == 0:
    dela = [0]
  
  return dela + flatspecial(delb)

print(flatspecial([[0, 1], [], [4,3,6], [8], []]))

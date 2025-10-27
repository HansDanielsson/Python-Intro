def mindiff(ls):
  i=0
  mind = abs(ls[0] - ls[1])
  while i < len(ls)-1:
    if abs(ls[i] - ls[i+1]) < mind:
      mind = abs(ls[i] - ls[i+1])
    i += 1
  return mind

print(mindiff([2,7,3,7,3,5,1,9]))

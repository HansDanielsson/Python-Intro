def min(lst):
  i=0
  e = lst[0]
  while i < len(lst):
    if lst[i]<e:
      e=lst[i]
    i+=1
  return e

print(min([5,2,7,1,8,-2]))

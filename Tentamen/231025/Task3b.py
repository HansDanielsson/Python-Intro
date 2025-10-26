def removeunsorted2(lst):
  i = 1
  rlst = [lst[0]]
  while i<len(lst):
    if lst[i-1] < lst[i]:
      rlst.append(lst[i])
    i +=1
  return rlst

b=[1,3,2,5,6]
b2 = removeunsorted2(b)
print(b2)
b2[0]=99
print(b)

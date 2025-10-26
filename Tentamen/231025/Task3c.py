def removeunsorted3(lst):
  i=1
  rlst = lst
  while i<len(lst):
    if lst[i-1]<lst[i]:
      i+=1
    else:
      rlst[i:i+1]=[]
  return rlst

c=[1,3,2,5,6]
c2=removeunsorted3(c)
print(c2)
c2[0]=99
print(c)

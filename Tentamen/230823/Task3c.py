def cliplarger2(numlist, cliplevel):
  i=0
  while i<len(numlist):
    if numlist[i]>cliplevel:
      numlist[i] = cliplevel
    i += 1
  return numlist

lst2a = [1,9,8,2,4]
lst2b = cliplarger2(lst2a,6)
print(lst2b)
lst2a[0]=99
print(lst2b)

def cliplarger1(numlist, cliplevel):
  i=0
  while i<len(numlist):
    if numlist[i]>cliplevel:
      numlist[i] = cliplevel
    i += 1
  return numlist[:]

lst1a = [1,9,8,2,4]
lst1b = cliplarger1(lst1a,6)
print(lst1a)
lst1a[0]=99
print(lst1b)

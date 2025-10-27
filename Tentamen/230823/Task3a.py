def cliplarger0(numlist, cliplevel):
  i=0
  newnumlist=[]
  while i<len(numlist):
    if numlist[i]>cliplevel:
      newnumlist.append(cliplevel)
    else:
      newnumlist.append(numlist[i])
    i += 1
  return newnumlist

lst0a = [1,9,8,2,4]
lst0b = cliplarger0(lst0a,6)
print(lst0a)

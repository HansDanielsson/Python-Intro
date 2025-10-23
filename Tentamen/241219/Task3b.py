def setminus1(lst, subtractlist):
  newlist=[]
  i=0
  while i<len(lst):
    if lst[i] not in subtractlist:
      newlist.append(lst[i])
    i+=1
  return newlist

lst1a = [3, 2, 5, 7]
lst1b = [2, 5]
lst1c = setminus1(lst1a, lst1b)

print(lst1a)  # Should print [3, 2, 5, 7]
print(lst1b)  # Should print [2, 5]
print(lst1c)  # Should print [3, 7]
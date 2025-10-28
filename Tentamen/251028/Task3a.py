def deleteunequal0(lst1, lst2):
  newlst = []
  i = 0
  while i < len(lst1):
    if lst1[i] == lst2[i]:
      newlst.append(lst1[i])
    i +=1
  return newlst

lst0a=[4,0,1,3,7]
lst0b=[4,1,2,3,7]
lst0r = deleteunequal0(lst0a, lst0b)
print("lst0a= ",lst0a)
print("lst0b= ",lst0b)
print("lst0r= ",lst0r)
lst0r[0] = 99
print("lst0a= ",lst0a)
print("lst0b= ",lst0b)
print("lst0r= ",lst0r)

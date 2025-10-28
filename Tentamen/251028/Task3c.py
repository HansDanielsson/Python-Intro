def deleteunequal2(lst1, lst2):
  newlst = lst2
  i = 0
  j = 0
  while i < len(lst1):
    if lst1[i] != lst2[j]:
      lst2[j:j+1] = []
    else:
      j = j + 1
    i = i + 1
  return newlst

lst2a = [4,0,1,3,7]
lst2b = [4,1,2,3,7]
lst2r = deleteunequal2(lst2a, lst2b)
print("lst2a = ", lst2a)
print("lst2b = ", lst2b)
print("lst2r = ", lst2r)
lst2r[0] = 99
print("lst2a = ", lst2a)
print("lst2b = ", lst2b)
print("lst2r = ", lst2r)

def deleteunequal1(lst1, lst2):
  i = 0
  while i < len(lst1):
    if lst1[i] != lst2[i]:
      lst1[i:i+1] = []
      lst2[i:i+1] = []
    else:
      i += 1

lst1a = [4,0,1,3,7]
lst1b = [4,1,2,3,7]
deleteunequal1(lst1a, lst1b)
print("lst1a = ",lst1a)
print("lst1b = ",lst1b)
lst1a[0] = 99
print("lst1b = ",lst1b)

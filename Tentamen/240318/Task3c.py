def insert3(lst,e):
  i=0
  while e>lst[i]:
    i = i + 1
    if i == len(lst):
      break
  lst[i:i] = [e]
  return lst

lb0 = [1,3,6,8,9]
lb1 = insert3(lb0,4)

print(lb0)
print(lb1)
lb1[0]=99
print(lb0)
print(lb1)

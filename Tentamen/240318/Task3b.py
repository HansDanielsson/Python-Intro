def insert2(lst , e):
  i = 0
  while e > lst[i]:
    i = i + 1
    if i == len(lst):
      break
  ls = lst[0:i] + [e] + lst[i+1:]
  return ls

lb0 = [1,3,6,8,9]
lb1 = insert2(lb0, 4)

print(lb0)
print(lb1)
lb1[0]=99
print(lb0)
print(lb1)

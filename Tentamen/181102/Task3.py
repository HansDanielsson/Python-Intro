def insert(lst1, lst2, p):
  if p>0:
    lst1[p:p] = lst2
  else:
    lst1 = lst2
  return lst1

l1 = [3,4,5]
l2 = insert(l1, [1,2], 1)
l1[0] = 10
l3 = insert(l2, [7,8], 0)

print("l1 = ", l1)
print("l2 = ", l2)
print("l3 = ", l3)

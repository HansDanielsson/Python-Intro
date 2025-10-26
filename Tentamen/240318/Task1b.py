lst=[5,3,9,2,7]
n = len(lst)
if lst[0] > n or len(lst) == lst[1]:
  print("A")
elif lst[2]-lst[0] == lst[1] + 1 and n==len(lst):
  print("B")
else:
  print("C")

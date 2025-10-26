def f(lst):
  i = 0
  prod = 1
  while i < len(lst):
    if lst[i] % 2 == 0:
      prod = prod * lst[i]
    i += 1
  return prod

print(f([1,2,4,3,6,5,1,3,4]))

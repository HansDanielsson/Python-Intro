def f(lst):
  i=1
  while i<len(lst):
    if lst[i] == 2*lst[i-1] + 1:
      i=i+1
    else:
      return False
  return True

print(f([1,3,7,15,31]))

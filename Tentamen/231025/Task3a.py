def removeunsorted1(lst):
  i = 1
  while i < len(lst):
    if lst[i-1] < lst[i]:
      i+=1
    else:
      lst[i:i+1] = []

a = [1,3,2,5,6]
removeunsorted1(a)
print(a)

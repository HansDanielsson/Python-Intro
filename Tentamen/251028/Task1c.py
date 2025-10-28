lst=[]
n = 4
m = 0
while len(lst) < n:
  lst = [n+m] + lst
  n = n-1
  m =m+1
  print(lst)

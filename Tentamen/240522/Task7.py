def smurf(lst, st):
  if not lst:
    return []
  return [st[lst[0]]] + smurf(lst[1:], st)

s1 = smurf([2,3,1,2], "abcd")
print(s1)
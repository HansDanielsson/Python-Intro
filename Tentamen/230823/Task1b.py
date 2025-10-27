w=[3,8,4,7]
q=[1,9,0]
n=len(w)
b=len(q)==w[0]
if b and len(q) == n:
  print("First")
elif w[0]==n or b:
  print("Second")
else:
  print("Third")

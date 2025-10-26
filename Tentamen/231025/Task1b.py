s="Eir"
n = len(s)
ls = [n, len(s), n-1]
b = ls[ls[2]] == n
if b and s == "Eir":
  print("Firse")
elif len(s) != ls[2]:
  print("Second")
else:
  print("Third")

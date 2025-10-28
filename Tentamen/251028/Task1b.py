s="abcde"
n = len(s)
if n < 5 or s[0] == s[3]:
  print("short")
elif len(s[1:]) < n and s[2] == "c":
  print("Long ok")
else:
  print("other")

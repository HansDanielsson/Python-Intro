s ="aouåeiyäö"
n = len(s) - 1
if s[1] == "o" and len(s) == n+1:
  print(s[:3])
elif s[n] == "ö":
  print("Test")
else:
  print("sommar")
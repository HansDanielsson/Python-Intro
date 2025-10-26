def filterdup(tu1, tu2):
  result = ()
  for i in range(len(tu1)):
    if (i % 2 == 0) and (tu1[i] == tu2[0]):
      result = result + (tu1[i]+tu1[i],)
    else:
      result = result + (tu1[i],)
  return result

print(filterdup(("Hej","hopp","Hej","Hej"),("Hej",)))

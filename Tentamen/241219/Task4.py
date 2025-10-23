def changecase(strlist):
  result = []
  for s in strlist:
    compstr = ""
    i = 0
    while i < len(s):
      ch = s[i]
      if ch.islower():
        compstr = compstr + ch.upper()
      else:
        compstr = compstr + ch.lower()
      i += 1
    result.append(compstr)
  return result
  
s1 = changecase(['A1b', 'b2A', 'cC3c'])
print(s1)  # Should print ['a1B', 'B2a', 'Cc3C']
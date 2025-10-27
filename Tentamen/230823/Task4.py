def substrswap(s1,s2):
  result = ""
  i = 0
  delstr = s2[1] + s2[0]
  while i < len(s1):
    if (s1[i] == s2[0]) and (s1[i+1] == s2[1]):
      result += delstr
      i += 1
    else:
      result += s1[i]
    i += 1
  return result

print(substrswap("aXYbXYc","XY"))

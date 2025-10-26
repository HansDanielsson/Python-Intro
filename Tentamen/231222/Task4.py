def julify(s1,s2):
  result = ""
  i = 0
  while i < len(s1):
    print(i)
    if s1[i] == s2[0] and s1[i+1] == s2[1]:
      result = result + "Jul"
      i += 1
    else:
      result = result + s1[i]
    i += 1
  return result

print(julify("abacabad","ab"))

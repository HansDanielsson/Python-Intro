def hist(s1):
  result = {}
  for ch in s1:
    antal = 0
    for i in range(len(s1)):
      if ch == s1[i]:
        antal += 1
    result[ch] = antal
  return result

print(hist("parallell"))

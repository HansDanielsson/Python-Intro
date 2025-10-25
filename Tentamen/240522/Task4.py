def replace(s1, s2):
  result = ""
  k = 0
  for i in range(len(s1)):
    if s1[i] == s2[0]:
      k += 1
      if k % 2 == 0:
        for _ in range(k):
          result += s2[0]
    else:
      result += s1[i]
  return result

s1 = replace("aWaXaYaZ", "a")
print(s1)
def keepcaps(s):
  result = ""
  for ch in s:
    if 'A' <= ch and ch <= 'Z':
      result += str(ch)
  return result

print(keepcaps("LuleåTekniskaUniversitet"))

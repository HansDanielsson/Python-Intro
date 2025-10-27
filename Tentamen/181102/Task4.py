def findrev(s1, s2, i):
  revs2 = ""
  for l in range(len(s2)):
    revs2 = s2[l] + revs2

  m = 0
  while m <= len(s1) - len(s2):
    if s1[m] == revs2[0]:
      found = True
      for ri in range(len(s2)):
        if revs2[ri] != s1[m+ri]:
          found = False
      if found:
        return m
    m += 1
  return i

print(findrev("Fin sensommardag", "mos", 40))
print(findrev("Fin sensommardag", "abc", 40))
print(findrev("Fin sensommardag", "g", 40))

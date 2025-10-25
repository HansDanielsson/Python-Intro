def countpos(lst):
  c = 0
  for e in lst:
    if e >= 0:
      c += 1
  return c

print(countpos([1, -2, 3, 4, -5, 0]))  # Expected output: 4
def revodd(lst):
  if len(lst) == 0:
    return []
  if lst[0] % 2 == 0:
    return revodd(lst[1:])
  return revodd(lst[1:]) + [lst[0]]

print(revodd([1,2,4,5,6,7]))

def pairsumfilt(lst1, lst2, s):
  result = []
  for k in range(len(lst1)):
    if lst1[k] + lst2[k] == s:
      result.append(lst1[k])
    else:
      result.append(lst2[k])
  return result

lstA = [1, 2, 2, 3, 7, 8]
lstB = [6, 3, 6, 4, 1, 0]
s = 7
res = pairsumfilt(lstA, lstB, s)

print(lstA)
print(lstB)
print(res)  # Expected output: [1, 3, 6, 3, 1, 0]
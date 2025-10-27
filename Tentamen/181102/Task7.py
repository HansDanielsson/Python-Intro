def sumpart(lst1, lst2):
  if len(lst1) == 0:
    return 0
  
  tal = lst1[0]
  resttal = lst1[1:]
  
  result = sumpart(resttal, lst2)
  if tal not in lst2:
    result += tal
  return result

print(sumpart([4,6,2,9,8], [4,9]))
def sumspecial(lst,r):
  # Basfall: nästan tom lista
  if len(lst) < 2:
    return -1
  
  deltal = lst[0]
  restlst = lst[1:]
  
  rest_sum = sumspecial(restlst, r)
  if (deltal != 0) and (restlst[0] / deltal == r):
    if rest_sum == -1:
      rest_sum = restlst[0]
    return deltal + rest_sum
  return rest_sum

print(sumspecial([1,2,4,8,16],2))
print(sumspecial([1,2,4,8,16],3))

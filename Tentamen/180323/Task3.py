def selectshortest(lsta, lstb):
  if len(lsta) > len(lstb):
    return lstb
  else:
    return lsta

def updatefirst(lst, e):
  lst[0] = e

lst1 = [4,6,8]
lst2 = selectshortest(lst1, [3,9])
updatefirst(lst2, 0)
lst3 = selectshortest(lst2, lst1)
lst2[0] = 99
print("lst1=", lst1)
print("lst2=", lst2)
print("lst3=", lst3)

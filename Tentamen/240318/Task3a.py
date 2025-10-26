def insert(lst, e):
  i = 0
  while e > lst[i]:
    print(i)
    i += 1
    if i == len(lst):
      break
  print("slut ", i)
  lst[i:i] = [e]

la = [1,3,6,8,9]
insert(la, 4)
print(la)

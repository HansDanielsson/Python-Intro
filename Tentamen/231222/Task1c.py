lst = [3,1,2]
while lst[0] != 2:
  lst = lst[1:]
  lst[0] = lst[0] + 1
  print(lst)
print("Finished")

def checksum(lst):
  i = 0
  one = True
  while i < len(lst):
    j = i + 1
    while j < len(lst):
      if (lst[i] + lst[j] == 10) and one:
        print("True")
        one = False
      j += 1
    i += 1
  if one:
    print("False")
    
checksum([1, 2, 3, 7, 8, 9])
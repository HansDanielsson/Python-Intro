lst = ["a", "b", "u", "q"]
i = len(lst) - 2
while i > 0:
  if lst[i] == "q":
    print("loop")
    continue
  i = i - 1
print("done")
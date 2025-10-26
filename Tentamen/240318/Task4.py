def split(s):
  result = []
  delstr=""
  for i in range(len(s)):
    if i == len(s) -1 or s[i] == " ":
      result = result + [delstr]
      delstr = ""
    else:
      delstr = delstr + s[i]
  return result

print(split("This is the exam for D0009E"))

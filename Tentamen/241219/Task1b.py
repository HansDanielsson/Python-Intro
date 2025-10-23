numbers = (4,3,2,1)
b = len(numbers) == numbers[0]
if not b or len(numbers) > numbers[1]:
  print("Jul!")
elif b and numbers[0] == numbers[1] + numbers[3]:
  print("Nyår!")
else:
  print("Tretton")
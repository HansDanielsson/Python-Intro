def deleteeven(lst):
  if not lst:
    return []
  if lst[0] % 2 == 0:
    return deleteeven(lst[1:])
  return deleteeven(lst[1:]) + [lst[0]]
# Example usage:
original_list = [2, 3, 5, 4, 4]
new_list = deleteeven(original_list)
print(original_list)  # Output: [2, 3, 5, 4, 4]
print(new_list)  # Output: [5, 3]
def symmetric_difference(set1, set2):
  return (set1 - set2) | (set2 - set1)

# Example usage:
set1 = {1, 2, 3, 4, 5}
set2 = {3, 5, 6, 7, 8}

symmetric_diff = symmetric_difference(set1, set2)
print(f"The symmetric difference between {set1} and {set2} is: {symmetric_diff}")
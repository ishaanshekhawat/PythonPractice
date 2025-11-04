# Define a list of numbers
ls = [3, 2, 6, 9, 8, 1, 2, 3, 4, 5]

# Outer loop: runs for each element in the list
# After each iteration, the largest unsorted element moves to its correct position at the end
for i in range(len(ls)):
    
    # Inner loop: compare adjacent elements up to the unsorted portion
    for j in range(0, len(ls) - i - 1):
        
        # If the current element is greater than the next one, swap them
        if ls[j] > ls[j + 1]:
            ls[j], ls[j + 1] = ls[j + 1], ls[j]
        
# Print the sorted list
print(ls)

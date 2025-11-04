# Given an list of integers called input, return True if any value appears at least twice in the array. Return False if every element in the input list is distinct.
# For example, if the input list was [1,3,5,7,1], then return True because the number 1 shows up twice.
# However, if the input was [1,3,5,7] then return False, because every element of the list is distinct.

# Function to check if a list contains any duplicate values
def contains_duplicate(input) -> bool:
    # Convert the list into a set.
    # A set automatically removes duplicate values.
    # If the length of the set is smaller than the list, it means some elements were duplicates.
    if len(input) != len(set(input)):
        return True  # Duplicate(s) found
    return False      # All elements are unique



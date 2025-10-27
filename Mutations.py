# Function to replace a character in a given string at a specific position
def mutate_string(string, position, character):
    # Create a new string by:
    # - Taking all characters before the given position
    # - Adding the new character
    # - Adding all characters after the given position
    s1 = string[:position] + character + string[position + 1:]
    
    # Return the new modified string
    return s1


# Main code block that executes when the program is run directly
if __name__ == '__main__':
    # Read the original string from user input
    s = input()
    
    # Read two values: the position (index) and the new character
    i, c = input().split()
    
    # Call the mutate_string function to replace the character at index 'i' with 'c'
    s_new = mutate_string(s, int(i), c)
    
    # Print the new string after mutation
    print(s_new)

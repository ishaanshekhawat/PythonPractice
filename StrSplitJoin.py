def split_and_join(line):
    # Split the input string 'line' into a list of words
    ls = line.split()
    
    # Join the list of words 'ls' with a hyphen ('-') between them
    jn = '-'.join(ls)
    
    # Return the modified string with words joined by hyphens
    return jn

# This block runs only if the script is executed directly (not imported)
if __name__ == '__main__':
    # Take input from the user
    line = input()
    
    # Call the 'split_and_join' function with the user's input and store the result
    result = split_and_join(line)
    
    # Output the result (string with words joined by hyphens)
    print(result)

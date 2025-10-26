def wrap(string, max_width):
    # Initialize an empty list to store the lines of wrapped text
    lines = []

    # Loop through the string, processing it in chunks of 'max_width'
    for i in range(0, len(string), max_width):
        # Append each chunk (substring of length 'max_width') to the 'lines' list
        lines.append(string[i:i+max_width])
    
    # Join all the lines with a newline character '\n' to create the wrapped text
    return '\n'.join(lines)

# This block runs only if the script is executed directly (not imported)
if __name__ == '__main__':
    # Input string from the user
    string = input()
    
    # Input max width (integer) from the user to control line length
    max_width = int(input())
    
    # Call the 'wrap' function with the string and max width, and store the result
    result = wrap(string, max_width)
    
    # Output the wrapped string (formatted into lines)
    print(result)

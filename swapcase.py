def swap_case(s):
    # Initialize an empty list to store the converted characters
    s1 = []
    
    # Iterate through each character in the input string
    for _ in s:
        # Get the ASCII value of the current character
        ascii = ord(_)
        
        # Check if the character is an uppercase letter (A–Z)
        if ascii >= 65 and ascii <= 90:
            # Convert uppercase to lowercase by adding 32 to its ASCII value
            ascii += 32
        
        # Check if the character is a lowercase letter (a–z)
        elif ascii >= 97 and ascii <= 122:
            # Convert lowercase to uppercase by subtracting 32 from its ASCII value
            ascii -= 32
        
        # Convert the modified ASCII value back to a character
        char = chr(ascii)
        
        # Append the converted character to the list
        s1.append(char)
    
    # Join the list of characters into a single string
    s2 = ''.join(s1)
    
    # Return the final string with swapped cases
    return s2

# This block runs only when the script is executed directly
if __name__ == '__main__':
    # Take input string from the user
    s = input()
    
    # Call the 'swap_case' function and store the result
    result = swap_case(s)
    
    # Print the result (string with swapped case)
    print(result)

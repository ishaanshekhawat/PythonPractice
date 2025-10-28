#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    result = ""  # Initialize an empty string to hold the result

    # Loop through each character in the input string
    for i in range(len(s)):
        # Check if the current character is the first character of a word
        if i == 0 or s[i - 1] == ' ':
            # If it's the first character of the string or a new word:
            # Check if the character is lowercase
            if s[i].islower():
                # Convert lowercase to uppercase by shifting its ASCII value
                result += chr(ord(s[i]) - 32)
            else:
                # If it's already uppercase or not a letter, keep it unchanged
                result += s[i]
        else:
            # If it's not the first letter of a word, just add the character as is
            result += s[i]
    
    # Return the modified string
    return result
        

if __name__ == '__main__':
    # Open the output file (this path is provided through environment variable OUTPUT_PATH)
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the input string
    s = input()

    # Call the solve function to process the string
    result = solve(s)

    # Write the result to the output file, followed by a newline
    fptr.write(result + '\n')

    # Close the output file
    fptr.close()

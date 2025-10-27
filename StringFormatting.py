# Function to convert a decimal number to its octal representation
def octal(n):
    octal = ""
    # Repeat until n becomes 0
    while n > 0:
        remainder = n % 8              # Get the remainder when dividing by 8
        octal = str(remainder) + octal # Add remainder to the left of the current string
        n = n // 8                     # Divide n by 8 (integer division)
    return octal                        # Return the final octal string


# Function to convert a decimal number to its hexadecimal representation
def hexa(n):
    hexa = ""
    while n > 0:
        rem = n % 16                   # Get the remainder when dividing by 16
        # Convert remainders 10–15 into corresponding hexadecimal letters
        if rem == 10:
            hexa = 'A' + hexa
        elif rem == 11:
            hexa = 'B' + hexa
        elif rem == 12:
            hexa = 'C' + hexa
        elif rem == 13:
            hexa = 'D' + hexa
        elif rem == 14:
            hexa = 'E' + hexa
        elif rem == 15:
            hexa = 'F' + hexa
        else:
            hexa = str(rem) + hexa     # For remainders less than 10, add the digit
        n = n // 16                    # Divide n by 16 (integer division)
    return hexa                        # Return the final hexadecimal string


# Function to convert a decimal number to its binary representation
def binary(n):
    binary = ""
    while n > 0:
        rem = n % 2                    # Get the remainder when dividing by 2
        binary = str(rem) + binary     # Add remainder to the left of the current string
        n = n // 2                     # Divide n by 2 (integer division)
    return binary                      # Return the final binary string


# Function to print numbers in decimal, octal, hexadecimal, and binary formats
def print_formatted(number):
    # Determine the width needed for proper alignment based on the largest binary value
    width = len(binary(number))
    
    # Loop through all numbers from 1 up to the given number
    for i in range(1, number + 1):
        # Print the number in decimal, octal, hexadecimal, and binary form
        # Each value is right-aligned to the calculated width for neat formatting
        print(
            str(i).rjust(width),        # Decimal value
            octal(i).rjust(width),      # Octal value
            hexa(i).rjust(width),       # Hexadecimal value
            binary(i).rjust(width)      # Binary value
        )


# Main program starts here
if __name__ == '__main__':
    # Read an integer input from the user
    n = int(input())
    
    # Print formatted output for all numbers from 1 to n
    print_formatted(n)

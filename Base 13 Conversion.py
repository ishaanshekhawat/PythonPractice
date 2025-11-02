# Given an integer num, return its string representation in base 13.

# In case you don’t use base 13 that much (who does, right?), here’s a quick rundown: just like base 10 uses digits from 0 to 9. But also for 10, 11 and 12, we use the letters A, B, and C.

# For example:

# 9 in base 13 is still "9"
# 10 in base 13 is "A"
# 11 in base 13 is "B"
# 12 in base 13 is "C"
# 13 in base 13 is "10"
# 14 in base 13 is "11"
# 49 in base 13 is "3A" 
# 69 in base 13 is "54"



def convertToBase13(num):
    # Variable to store remainder of division by 13
    rem = 0
    # String to accumulate the final base-13 representation
    result = ''

    # Check if the number is negative
    if str(num)[0] == '-':
        # Convert negative number to positive for easier processing
        num = int(str(num)[1:])
        
        # Loop to convert the number to base 13
        while(num > 0):
            # If remainder is less than 10, just use the digit
            if num % 13 < 10:
                rem = num % 13
                num = num // 13
            # If remainder is 10, use 'A' for base 13 representation
            elif num % 13 == 10:
                rem = 'A'
                num = num // 13
            # If remainder is 11, use 'B'
            elif num % 13 == 11:
                rem = 'B'
                num = num // 13
            # If remainder is 12, use 'C'
            elif num % 13 == 12:
                rem = 'C'
                num = num // 13
            
            # Prepend the remainder to the result string (since we're building the number backwards)
            result = str(rem) + result
        
        # Add negative sign at the beginning and return the result
        return '-' + result

    # Special case: if the number is 0, simply return '0'
    elif num == 0:
        return str(num)

    # For positive numbers, similar process as for negative
    else:
        while(num > 0):
            # If remainder is less than 10, just use the digit
            if num % 13 < 10:
                rem = num % 13
                num = num // 13
            # If remainder is 10, use 'A' for base 13 representation
            elif num % 13 == 10:
                rem = 'A'
                num = num // 13
            # If remainder is 11, use 'B'
            elif num % 13 == 11:
                rem = 'B'
                num = num // 13
            # If remainder is 12, use 'C'
            elif num % 13 == 12:
                rem = 'C'
                num = num // 13
            
            # Prepend the remainder to the result string
            result = str(rem) + result
        
        # Return the final result as the base-13 string representation
        return result

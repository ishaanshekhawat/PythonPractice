# Read the number of test cases (n) from input
n = int(input())

# Loop through each test case
for _ in range(n):
    try:
        # Read two integers a and b from input and attempt integer division
        a, b = map(int, input().split())

        # Perform integer division and print the result
        print(a // b)
    
    # Handle the case where division by zero occurs
    except ZeroDivisionError as e:
        # If division by zero happens, print the error message
        print("Error Code:", e)
    
    # Handle the case where invalid input is given (e.g., non-integer values)
    except ValueError as e:
        # If there’s a ValueError (like incorrect input format), print the error message
        print("Error Code:", e)

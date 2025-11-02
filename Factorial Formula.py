# Given a number n, write a formula that returns n!.
# In case you forgot the factorial formula, n! = n * (n - 1) * (n -2) * ....2*1.
# For example, 5! = 5 * 4 * 3 * 2 * 1 = 120 so we'd return 120.
# Assume n is a non-negative integer.

def factorial(n):
    # Initialize a variable to store the running product.
    # Start with 1 because multiplying by 1 doesn’t change the result.
    num = 1

    # Loop through all integers from 2 up to and including n
    # Each number is multiplied into 'num' to compute the factorial.
    for i in range(2, n + 1):
        num *= i  # Equivalent to: num = num * i

    # After the loop finishes, 'num' holds the factorial of n
    return num


# Example usage: prints the factorial of 6 (6 * 5 * 4 * 3 * 2 * 1 = 720)
print(factorial(6))

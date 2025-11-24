def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    prev2, prev1 = 0, 1  # Base cases: F(0) = 0, F(1) = 1
    for i in range(2, n + 1):
        current = prev1 + prev2  # F(i) = F(i-1) + F(i-2)
        prev2 = prev1
        prev1 = current
    return prev1

# Example:
print(fibonacci(6))  # Output: 8

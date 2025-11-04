# Write a function fizz_buzz_sum to find the sum of all multiples of 3 or 5 below a target value.
# For example, if the target value was 10, the multiples of 3 or 5 below 10 are 3, 5, 6, and 9.
# Because 3+5+6+9=23, our function would return 23.
from functools import reduce

def fizz_buzz_sum(target):
    mult3 = []
    mult5 = []
    for i in range(2, target):
        if i % 3 == 0:
            mult3.append(i)
        elif i % 5 == 0:
            mult5.append(i)
    
    return reduce(lambda x,y: x+y, (mult3+mult5))
# For this Fintech company, you need to build a compound interest calculator, using the four variables below as input:
# Principal: This is the starting amount you put into the account. It’s the base amount that will start earning interest right away.
# Interest Rate: This is the percentage of your current balance that the bank adds to your account as interest each year. For example, a 5% interest rate means the bank will add 5% of your balance to your account every year.
# Annual Contribution: This is a fixed amount you add to your investment at the end of each year, like a regular deposit you decide to make. Each time you make this contribution, it increases your balance, which in turn, increases the amount of interest you earn next year (since interest is calculated on the new, larger balance).
# Years to Invest: This is how long your money stays in the account, compounding annually. The longer you invest, the more times your balance grows, not only from the interest but also from the additional contributions.
# Using these four values, calculate the final amount you’ll have after the specified number of years, with annual compounding. In other words, at the end of each year, you’ll earn interest on your current balance, then make an additional contribution.
# Return the answer rounded to two decimal places.
# Example #1
# Input:
# principal	    rate	contribution	years
# 500	        10	        50	            3
# Output: 831.00
# Explanation:

# Year 1: Starting with 500, it grows by 10% (interest = 10% of 500 = 50), totaling 550. Adding 50 as an additional contribution results in 600.
# Year 2: 600 grows by 10% (interest = 10% of 600 = 60), totaling 660. Adding 50, we reach 710.
# Year 3: 710 grows by 10% (interest = 10% of 710 = 71), totaling 781. Adding 50 results in 831.

def compound_interest(principal, rate, contribution, years):
    for i in range(years):
        ci_for_that_year = principal*rate/100
        principal += ci_for_that_year + contribution
    return round(principal, 2)
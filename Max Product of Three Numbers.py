# Given a list of integers, return the maximum product of any three numbers in the array.

# For example, for A = [1, 3, 4, 5], you should return 60, since 3*4*5=60.

# For B = [−4, −2, 3, 5] you should return 40 since -4*−2*5=40

def max_three(input):
    # Initialize ct (current max product) to negative infinity
    # This ensures any real product will be larger than ct initially
    ct = float('-inf')

    # Iterate through all unique combinations of three different elements
    for i in range(len(input) - 2):
        for j in range(i + 1, len(input) - 1):
            for k in range(j + 1, len(input)):
                # Calculate the product of the three selected numbers
                product = input[i] * input[j] * input[k]

                # If the current product is greater than the current maximum, update ct
                if product > ct:
                    ct = product

    # After checking all triplets, return the maximum product found
    return ct


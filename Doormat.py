# Read two integers from user input: n (number of rows) and width (total width of the pattern)
n, width = map(int, input().split())

# Define the pattern to be used for the top and bottom parts of the design
p = '.|.'
# Define the message to be printed in the center of the pattern
sign = 'WELCOME'

# Loop to print the top part of the pattern (above the "WELCOME" sign)
for i in range(1, n, 2):
    # Print the pattern string 'p' repeated i times, centered in the given width, with '-' as padding
    print((p * i).center(width, '-'))

# Print the "WELCOME" message centered in the given width, with '-' as padding
print(sign.center(width, '-'))

# Loop to print the bottom part of the pattern (below the "WELCOME" sign)
for i in range(n - 2, 0, -2):
    # Print the pattern string 'p' repeated i times, centered in the given width, with '-' as padding
    print((p * i).center(width, '-'))

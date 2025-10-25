# Define a regular expression (regex) pattern to match commas (,) and periods (.)
regex_pattern = r"[,.]"  # Do not delete 'r'

# Import the regular expressions module
import re

# Take input from the user as a string
# Use re.split() to split the string wherever a comma or period appears
# Then, join the resulting list elements with newline characters ('\n')
# This effectively prints each segment of the input string on a new line.
print("\n".join(re.split(regex_pattern, input())))

# This program checks whether the input string contains:
# - Any alphanumeric characters
# - Any alphabetical characters
# - Any digits
# - Any lowercase letters
# - Any uppercase letters

if __name__ == '__main__':
    # Read a string from user input
    s = input()
    
# Initialize boolean flags for each condition
out1 = False  # Will be True if the string has at least one alphanumeric character
out2 = False  # Will be True if the string has at least one alphabetical character
out3 = False  # Will be True if the string has at least one digit
out4 = False  # Will be True if the string has at least one lowercase letter
out5 = False  # Will be True if the string has at least one uppercase letter

# Iterate through each character in the input string
for i in s:
    # Check if the character is alphanumeric (a letter or a digit)
    if i.isalnum():
        out1 = True
    # Check if the character is alphabetic (a letter only)
    if i.isalpha():
        out2 = True
    # Check if the character is a digit (0–9)
    if i.isdigit():
        out3 = True
    # Check if the character is lowercase (a–z)
    if i.islower():
        out4 = True
    # Check if the character is uppercase (A–Z)
    if i.isupper():
        out5 = True

# Print the results for each test in order
print(out1)  # True if there is any alphanumeric character
print(out2)  # True if there is any alphabetical character
print(out3)  # True if there is any digit
print(out4)  # True if there is any lowercase letter
print(out5)  # True if there is any uppercase letter

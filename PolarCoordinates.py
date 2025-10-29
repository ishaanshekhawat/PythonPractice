import cmath  # Importing the cmath module to handle complex numbers and related operations

# Taking user input as a string (expected input in the form of 'a+bj' or 'a-bj')
z = input()

# Initialize variable idx to -1, which will store the index of '+' or '-' sign in the complex number
idx = -1

# Loop through the string (starting from index 1) to find the position of '+' or '-' which separates real and imaginary parts
for i in range(1, len(z)):  # Iterate from index 1 to avoid the first character (assuming it could be '-')
    if z[i] == '+' or z[i] == '-':  # Check if the character is '+' or '-'
        idx = i  # Store the index of '+' or '-' as the separator
        break  # Exit the loop once the sign is found

# The real part of the complex number is everything before the sign
x = z[:idx]

# The imaginary part is everything from the sign to the last character 'j'
y = z[idx:-1]

# Convert the real and imaginary parts to floats, create a complex number, and calculate its magnitude
# round() is used to limit the output to 3 decimal places
print(round(abs(complex(float(x), float(y))), 3))  # Output the magnitude of the complex number

# Calculate and print the phase (angle) of the complex number, rounded to 3 decimal places
print(round(cmath.phase(complex(float(x), float(y))), 3))  # Output the phase (angle) in radians

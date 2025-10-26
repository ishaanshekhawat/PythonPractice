# This program creates a pattern using the character 'H' with specific formatting.

# Input for thickness of the pattern; should be an odd number
thickness = int(input())  # This must be an odd number
c = 'H'  # Character to create the pattern

# Top Cone
# Loop through each row to print the top cone part of the pattern
for i in range(thickness):
    # Create a row with rjust for the left side, c in the middle, and ljust for the right side
    # 'rjust' right-aligns the string with spaces, 'ljust' left-aligns the string with spaces
    print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

# Top Pillars
# Loop through to print the top pillar part of the pattern
for i in range(thickness + 1):
    # 'center' centers the string within a given width, with spaces on both sides
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

# Middle Belt
# Loop to print the middle belt (wide horizontal strip) of the pattern
for i in range((thickness + 1) // 2):
    # 'center' centers the string in a width equal to 6 times the thickness
    print((c*thickness*5).center(thickness*6))

# Bottom Pillars
# Loop through to print the bottom pillar part of the pattern
for i in range(thickness + 1):
    # Again, use 'center' to create the pillar pattern with proper spacing
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

# Bottom Cone
# Loop to print the bottom cone part of the pattern
for i in range(thickness):
    # 'rjust' right-aligns the left part of the cone, 'ljust' left-aligns the right part
    # The entire cone is then 'rjust' to center it at the bottom of the pattern
    print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

# Read a string input from the user
S = input()

# Loop through the string, stopping one character before the end
for i in range(len(S) - 1):
    # Check if both the current and next characters are alphanumeric (letters or digits)
    if S[i].isalnum() and S[i+1].isalnum():
        # Check if the two consecutive alphanumeric characters are the same
        if S[i] == S[i+1]:
            # If a repeating character is found, print it
            print(S[i])
            # Exit the loop immediately after finding the first occurrence
            break
# The 'else' block here runs only if the loop completes without finding a match
else:
    # Print -1 if no consecutive repeating alphanumeric character was found
    print(-1)



# Alternative Solution below --------------------------

# import re

# S = input()

# # Pattern explanation:
# # (\w)   -> capture any alphanumeric character (letter, digit, or underscore)
# # \1     -> backreference to the first captured character, means repeated consecutively

# match = re.search(r'(\w)\1', S)

# if match:
#     print(match.group(1))
# else:
#     print(-1)

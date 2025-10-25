S = input()

for i in range(len(S) - 1):
    if S[i].isalnum() and S[i+1].isalnum():
        if S[i] == S[i+1]:
            print(S[i])
            break
else:
    print(-1)


import re

# S = input()

# # Pattern explanation:
# # (\w)   -> capture any alphanumeric character (letter, digit, or underscore)
# # \1     -> backreference to the first captured character, means repeated consecutively

# match = re.search(r'(\w)\1', S)

# if match:
#     print(match.group(1))
# else:
#     print(-1)

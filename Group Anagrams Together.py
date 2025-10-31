# You are given a list of words.
# Your task is to group all the anagrams together — words that contain the same letters in any order.
# Return the groups as a list of lists, where each inner list contains all words that are anagrams of each other.

# Example Input - words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Example Output - [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

words = input().split()
d1 = {}

for word in words:
    temp = ''.join(sorted(word))
    if temp in d1:
        d1[temp].append(word)
    else:
        d1[temp] = []
        d1[temp].append(word)

output_list = []
for k,v in d1.items():
    output_list.append(v)

print(output_list)

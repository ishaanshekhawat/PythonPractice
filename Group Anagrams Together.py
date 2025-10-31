# You are given a list of words.
# Your task is to group all the anagrams together — words that contain the same letters in any order.
# Return the groups as a list of lists, where each inner list contains all words that are anagrams of each other.

# Example Input - words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Example Output - [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# Read a line of input and split it into individual words
words = input().split()

# Dictionary to group words by their sorted character sequence (anagrams)
d1 = {}

# Loop through each word to classify it
for word in words:
    # Sort the letters of the word and join them back into a string
    # This string will be the key for the dictionary
    temp = ''.join(sorted(word))
    
    if temp in d1:
        # If the sorted key already exists, append this word to its list
        d1[temp].append(word)
    else:
        # If the key doesn't exist, create a new list with this word
        d1[temp] = []
        d1[temp].append(word)

# Prepare the output list containing groups of anagrams
output_list = []
for k, v in d1.items():
    output_list.append(v)  # Each value is a list of words that are anagrams

# Print the list of grouped anagrams
print(output_list)

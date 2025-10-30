# You are given a paragraph of text as input.
# Your task is to analyze the paragraph and output the following:
#       Total number of words in the paragraph.
#       Number of unique words (case-insensitive).
#       A list of the top 3 most frequent words along with their counts, sorted by frequency (highest first).
#       A tuple containing the shortest and longest unique words (by length).

import re

# Take a paragraph as input from the user
para = input()

# Split the paragraph into words using common punctuation and spaces as delimiters
words = re.split(r'[ ,.;!/]+', para)

# Remove any empty strings that may result from splitting
# (e.g., if there are multiple spaces or punctuation at the ends)
for i in words:
    if i:             # if the word is not empty, keep it
        continue
    else:             # if the word is empty, remove it
        words.remove(i)

# Print the total number of words
print(f"Total number of words: {len(words)}")

# Create a dictionary to count occurrences of each word (case-insensitive)
word_dict = {}
for i in words:
    if i.lower() in word_dict:        # convert to lowercase for case-insensitive counting
        word_dict[i.lower()] += 1
    else:                          
        word_dict[i.lower()] = 1

# Create a list of words that appear only once (unique words)
unique_words = []
for k,v in word_dict.items():
    if v == 1:
        unique_words.append(k)

# Print the number of unique words
print(f'Number of unique words: {len(unique_words)}')

# Sort the dictionary by word frequency in descending order
sorted_wc = dict(sorted(word_dict.items(), key = lambda item:item[1], reverse=True))

# Extract the top 3 most frequent words
top_3 = []
ct = 0
for k,v in sorted_wc.items():
    top_3.append((k,v))            # store as tuple (word, count)
    ct += 1
    if ct == 3:                    # stop after 3 words
        break

# Print the top 3 frequent words with their counts
print(f'Top 3 frequent words: {top_3}')

# Initialize variables for finding shortest and longest words
lct = float('inf')            # start with infinity for shortest word
sct = 0                       # start with 0 for longest word

for i in words:
    if len(i) > sct:
        sct = len(i)
    if len(i) < lct:
        lct = len(i)

for i in words:
    if len(i) == sct:
        longest_word = i
    if len(i) == lct:
        shortest_word = i

sl_tuple = (shortest_word, longest_word)

print(f'Shortest and longest words: {sl_tuple}')

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
for i in words:
    if i:
        continue
    else:
        words.remove(i)

print(f"Total number of words: {len(words)}")

word_dict = {}

for i in words:
    if i.lower() in word_dict:
        word_dict[i.lower()] += 1
    else:
        word_dict[i.lower()] = 1

unique_words = []

for k,v in word_dict.items():
    if v == 1:
        unique_words.append(k)

print(f'Number of unique words: {len(unique_words)}')

sorted_wc = dict(sorted(word_dict.items(), key = lambda item:item[1], reverse=True))

t1 = ()
top_3 = []
ct = 0
for k,v in sorted_wc.items():
    t1 = (k,v)
    top_3.append(t1)
    ct += 1
    if ct == 3:
        break

print(f'Top 3 frequent words: {top_3}')

lct = float('inf')
sct = 0

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

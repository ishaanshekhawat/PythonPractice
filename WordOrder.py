# Take an integer input n, which represents the number of words the user will input
n = int(input())

# Initialize an empty set to store distinct words (set automatically handles duplicates)
distinct_words = set()

# Initialize an empty list to store all words as they are entered
all_words = []

# Loop n times to take n words as input
for i in range(n):
    i = input().strip()  # Take input word and remove any leading/trailing spaces
    distinct_words.add(i)  # Add the word to the set (automatically removes duplicates)
    all_words.append(i)  # Add the word to the list (for later counting)

# Print the number of distinct words (size of the set)
print(len(distinct_words))

# Initialize an empty dictionary to store the occurrences of each word
occurences = {}

# Loop through all words and count their occurrences
for i in all_words:
    if i in occurences:  # If the word is already in the dictionary, increment its count
        occurences[i] += 1
    else:  # If the word is not in the dictionary, add it with count 1
        occurences[i] = 1

# Initialize an empty list to store the final occurrence counts for each word in the order they appeared
final_list = []

# Loop through the dictionary to extract the occurrence count for each word
for k, v in occurences.items():  # k is the word, v is the count
    final_list.append(str(v))  # Convert the count to string and add to the list

# Join the list of counts into a single string with spaces and print it
print(' '.join(final_list))

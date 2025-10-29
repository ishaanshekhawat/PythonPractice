n = int(input())

distinct_words = set()
all_words = []

for i in range(n):
    i = input().strip()
    distinct_words.add(i)
    all_words.append(i)

print(len(distinct_words))

occurences = {}
for i in all_words:
    if i in occurences:
        occurences[i] += 1
    else:
        occurences[i] = 1

final_list = []

for k,v in occurences.items():
    final_list.append(str(v))

print(' '.join(final_list))
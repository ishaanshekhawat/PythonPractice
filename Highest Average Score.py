# Problem Statement
# You are given a list of tuples, where each tuple represents a student’s name and one of their test scores.
# Your task is to:
#   Compute each student’s average score.
#   Find the student(s) who have the highest average.
#   Return both:
#       The highest average score.
#       A list of student(s) who achieved it.

# Example Input
# records = [
#     ("Alice", 90),
#     ("Bob", 82),
#     ("Alice", 95),
#     ("Bob", 85),
#     ("Charlie", 95),
#     ("Charlie", 90)
# ]

# Expected Output
# Top student(s): ['Alice', 'Charlie']
# Highest average: 92.5
from functools import reduce

n = int(input())
records = []

for _ in range(n):
    name, score = input().split()
    records.append((name, int(score)))

def compile_score(records):
    stu_dict = {}
    for i in records:
        if i[0] in stu_dict:
            stu_dict[i[0]].append(i[1])
        else:
            stu_dict[i[0]] = []
            stu_dict[i[0]].append(i[1])
    
    return stu_dict

def avg_score(stu_dict):
    a_scores = []
    for k,v in stu_dict.items():
        avg = (reduce(lambda x,y:x+y, v))/len(v)
        a_scores.append((k, avg))
    
    return a_scores

sorted_stu = sorted(avg_score(compile_score(records)), key = lambda x: x[1], reverse=True)

top_students=[]

for i in range(len(sorted_stu)):
    if i==0:
        top_students.append(sorted_stu[i][0])
        highest_score = sorted_stu[i][1]
    elif sorted_stu[i][1] == sorted_stu[0][1]:
        top_students.append(sorted_stu[i][0])
    else:
        break
               

print(f"Top student(s): {top_students}")
print(f"Highest average: {highest_score}")

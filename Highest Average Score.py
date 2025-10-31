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

from functools import reduce  # Import reduce to calculate sum of scores

# Read the number of records from the user
n = int(input())
records = []

# Read each record (student name and score) and store as a tuple in the list
for _ in range(n):
    name, score = input().split()
    records.append((name, int(score)))

# Function to compile all scores for each student into a dictionary
def compile_score(records):
    stu_dict = {}  # Dictionary to store student names as keys and list of scores as values
    for i in records:
        if i[0] in stu_dict:
            stu_dict[i[0]].append(i[1])  # If student exists, append new score
        else:
            stu_dict[i[0]] = []          # If student not in dict, initialize empty list
            stu_dict[i[0]].append(i[1])  # Append the first score
    return stu_dict

# Function to calculate average score for each student
def avg_score(stu_dict):
    a_scores = []  # List to store tuples of (student_name, average_score)
    for k, v in stu_dict.items():
        avg = (reduce(lambda x, y: x + y, v)) / len(v)  # Compute average using reduce
        a_scores.append((k, avg))
    return a_scores

# Sort students by average score in descending order
sorted_stu = sorted(avg_score(compile_score(records)), key=lambda x: x[1], reverse=True)

top_students = []  # List to store names of students with highest average

# Iterate over the sorted list to find all students with the top average
for i in range(len(sorted_stu)):
    if i == 0:
        # First student has the highest score
        top_students.append(sorted_stu[i][0])
        highest_score = sorted_stu[i][1]
    elif sorted_stu[i][1] == sorted_stu[0][1]:
        # Any other student with the same highest score is also added
        top_students.append(sorted_stu[i][0])
    else:
        # Once a lower score is reached, stop checking
        break

# Print results
print(f"Top student(s): {top_students}")
print(f"Highest average: {highest_score}")

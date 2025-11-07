# At your big-tech company, teams are fighting tooth and nail to train their AI models on the company’s shiny new NVIDIA GPUs. 
# It’s like the Hunger Games but with less archery and more coding.

# The GPUs are in such high demand that some teams “accidentally” (totally on purpose) overlap their training sessions. 
# It’s chaos. The GPU cluster is booked for days on end, and now everyone’s looking for gaps to squeeze 
# in their own usage.

# Unlike those greedy GPU hogs, your team has been given strict instructions: you can only run your training 
# on days when nobody else is using the GPUs. Your VP made it crystal clear that overlapping sessions are not an option.

# You’re given two things:

# An integer days, representing the total number of days the GPUs are available (from day 1).
# A 2D array training_sessions where training_sessions[i] = [start_i, end_i] shows when team i is hogging the GPUs.
# Your mission is to figure out how many days the GPUs are sitting idle so that your team can swoop in and get 
# some guilt-free training time.

# Example #1
# Input: training_sessions = [[2, 4], [1, 5], [7, 8]], days = 9
# Output: 2

# Explanation:
# Day 6 and day 9 are the only days when the GPUs are free.

# Example #2
# Input: training_sessions = [[1, 4]], days = 4
# Output: 0

# Explanation:
# The GPUs didn’t get a single day off. Your team will just have to wait patiently until the chaos subsides.

def gpu_idle_days(days, training_sessions):
    s1 = set()
    for i in training_sessions:
        for j in range(i[0],i[1]+1):
            s1.add(j)
    ls = []
    for i in range(1,days+1):
        if i not in s1:
            ls.append(i)
    return len(ls)
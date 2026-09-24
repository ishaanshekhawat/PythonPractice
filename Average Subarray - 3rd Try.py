# https://datalemur.com/questions/python-average-subarray

def avg(ls):
    total = 0
    n = len(ls)
    for i in ls:
        total += i

    return total / n


def max_avg_subarray(nums, k):
    sub = []

    p = 0

    m_a = float('-inf')

    while p <= len(nums) - k:
        for i in range(0, k):
            sub.append(nums[p + i])
        if m_a < avg(sub):
            m_a = avg(sub)
        p += 1
        sub = []

    return round(m_a, 2)

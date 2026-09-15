# https://datalemur.com/questions/python-most-popular-integers

def most_popular(nums, n):
    d = {}

    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    s_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    res = []

    for k, v in s_d.items():
        if n == 0:
            break
        res.append(k)
        n -= 1

    return sorted(res)

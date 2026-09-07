# https://datalemur.com/questions/python-looping-number

def sum_of_sq(n):
  res = 0
  while n != 0:
    k = n % 10
    res += k**2
    n //= 10
  return res


def is_looping(n):
  if n == 1:
    return False
  
  seen = set()
  seen.add(n)
  
  while n != 1:
    if sum_of_sq(n) in seen:
      return True
    else:
      seen.add(sum_of_sq(n))
      n = sum_of_sq(n)
  
  return False

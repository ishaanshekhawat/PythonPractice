# https://datalemur.com/questions/python-average-subarray

def max_avg_subarray(nums, k):
  window_sum = sum(nums[:k])
  maxi = window_sum
  for i in range(len(nums)-k):
    window_sum -= nums[i]
    window_sum += nums[i+k]
    if window_sum > maxi:
      maxi = window_sum
  
  return round(maxi/k, 2)

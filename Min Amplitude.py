# https://datalemur.com/questions/python-min-amplitude

def quicksort(l):
  
    if len(l) <= 1:
      return l
    
    pivot = l[len(l)//2]

    left = [x for x in l if x < pivot]
    middle = [x for x in l if x == pivot]
    right = [x for x in l if x > pivot]

    return quicksort(left) + middle + quicksort(right)


def min_amplitude(arr):
    arr = quicksort(arr)
    
    i = 0
    j = len(arr) - 1
    mid = len(arr) // 2
    ct = 0
    
    while ct < 3 and ct < len(arr):
      if abs(arr[i] - arr[mid]) > abs(arr[j] - arr[mid]):
        arr[i] = arr[mid]
        i += 1
      else:
        arr[j] = arr[mid]
        j-= 1
      ct += 1
    
    arr = quicksort(arr)

    return arr[len(arr) - 1] - arr[0]

# https://datalemur.com/questions/python-gift-card-satisfaction

def quicksort(arr):
  
  if len(arr) <= 1:
    return arr
    
  pivot = arr[len(arr) // 2]
  
  left = [x for x in arr if x < pivot]
  middle = [x for x in arr if x == pivot]
  right = [x for x in arr if x > pivot]
  
  return quicksort(left) + middle + quicksort(right)
  

def max_satisfaction(expectations, cards):
    expectations = quicksort(expectations)
    cards = quicksort(cards)

    ct = 0
    i = 0
    j = 0

    while i < len(expectations) and j < len(cards):
        if cards[j] >= expectations[i]:
            ct += 1
            i += 1
            j += 1
        else:
            j += 1

    return ct
  

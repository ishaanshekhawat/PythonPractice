# https://platform.stratascratch.com/algorithms/10395-alternate-min-max-rearrangement

def modify_array(arr):
    """ 
    :type arr: List[int]
    :rtype: List[int]
    """
    
    arr.sort()
    
    ls = []
    
    left = 0
    right = len(arr)-1
    
    while left < right:
        ls.append(arr[left])
        ls.append(arr[right])
        left+=1
        right-=1
    
    return ls

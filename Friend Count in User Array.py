# https://platform.stratascratch.com/algorithms/10404-friend-count-in-user-array

def count_friends(user_ids):
    """
    :type user_ids: List[List[int]]
    :rtype: Dict[int, int]
    """
    
    d = {}
    
    for i in user_ids:
        for j in i:
            if j in d:
                d[j] += 1
            else:
                d[j] = 1
    
    return d

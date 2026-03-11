# https://platform.stratascratch.com/algorithms/10405-next-smallest-palindrome

def next_palindrome(n):
    """
    :type n: int
    :rtype: int
    """
    num = n + 1
    
    def checker(n):
        s = str(n)
        left = 0
        right =len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            return False
        
        return True
    
    while n < 1000000:
        if checker(num):
            return num
        num += 1

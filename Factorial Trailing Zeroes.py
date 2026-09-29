# https://datalemur.com/questions/python-factorial-trailing-zeroes

def trailing_zeroes(n):
    ct = 0
    
    for i in range(1, n+1):
        if i % 5 == 0:
            for j in range(1, 10):
                if i % (5**j) == 0:
                    ct+=1
                else:
                    break
    
    return ct

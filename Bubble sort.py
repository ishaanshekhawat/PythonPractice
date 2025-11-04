ls = [3,2,6,9,8,1,2,3,4,5]


for i in range(len(ls)):
    for j in range(0, len(ls)-i-1):
        if ls[j] > ls[j+1]:
            ls[j],ls[j+1] = ls[j+1],ls[j]
        
print(ls)
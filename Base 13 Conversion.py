# Given an integer num, return its string representation in base 13.

# In case you don’t use base 13 that much (who does, right?), here’s a quick rundown: just like base 10 uses digits from 0 to 9. But also for 10, 11 and 12, we use the letters A, B, and C.

# For example:

# 9 in base 13 is still "9"
# 10 in base 13 is "A"
# 11 in base 13 is "B"
# 12 in base 13 is "C"
# 13 in base 13 is "10"
# 14 in base 13 is "11"
# 49 in base 13 is "3A" 
# 69 in base 13 is "54"



def convertToBase13(num):
    rem = 0
    result = ''
    if str(num)[0] == '-':
        num = int(str(num)[1:])
        while(num>0):
            if num%13<10:
                rem = num % 13
                num = num//13
            elif num%13==10:
                rem = 'A'
                num = num//13
            elif num%13==11:
                rem = 'B'
                num = num//13
            elif num%13==12:
                rem = 'C'
                num = num//13
            result = str(rem) + result
        return '-' + result
    elif num == 0:
        return num
    else:
        while(num>0):
            if num%13<10:
                rem = num % 13
                num = num//13
            elif num%13==10:
                rem = 'A'
                num = num//13
            elif num%13==11:
                rem = 'B'
                num = num//13
            elif num%13==12:
                rem = 'C'
                num = num//13
            result = str(rem) + result
        return result
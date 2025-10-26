def swap_case(s):
    s1 = []
    for _ in s:
        ascii = ord(_)
        if ascii >= 65 and ascii <=90:
            ascii += 32
        elif ascii >= 97 and ascii <=122:
            ascii -= 32
        char = chr(ascii)
        s1.append(char)
    
    s2 = ''.join(s1)
    return s2

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
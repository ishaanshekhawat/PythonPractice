if __name__ == '__main__':
    s = input()
    
out1 = False
out2 = False
out3 = False
out4 = False
out5 = False

for i in s:
    if i.isalnum():
        out1 = True
    if i.isalpha():
        out2 = True
    if i.isdigit():
        out3 = True
    if i.islower():
        out4 = True
    if i.isupper():
        out5 = True

print(out1)
print(out2)
print(out3)
print(out4)
print(out5)
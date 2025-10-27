n, width = map(int, input().split())

p = '.|.'
sign = 'WELCOME'

for i in range(1, n, 2):
    print((p*i).center(width, '-'))

print(sign.center(width, '-'))

for i in range(n-2, 0, -2):
    print((p*i).center(width, '-'))
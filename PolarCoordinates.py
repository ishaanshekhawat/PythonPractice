import cmath

z = input()

idx = -1
for i in range(1,len(z)):           #-5-6j
    if z[i] == '+' or z[i] == '-':        
        idx = i
        break

x = z[:idx]
y=z[idx:-1]

print(round(abs(complex(float(x),float(y))), 3))
print(round(cmath.phase(complex(float(x),float(y))), 3))


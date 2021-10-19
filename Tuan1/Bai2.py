import math
print('Nhập x:')
x = int(input())
f = (x**2 + math.exp(x) + math.sin(x))/math.sqrt(x**2 + 1)
print('F(x) =', f)
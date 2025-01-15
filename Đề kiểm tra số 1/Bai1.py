import math
def gcd_lcm(a, b):
    return math.gcd(a, b), (a * b)//math.gcd(a, b)

a = int(input('Nhap a: '))
b = int(input('Nhap b: '))

print(f'UCLN cua {a} va {b} la: ', gcd_lcm(a, b)[0])
print(f'BCNN cua {a} va {b} la: ', gcd_lcm(a, b)[1])

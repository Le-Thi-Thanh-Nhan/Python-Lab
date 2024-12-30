#Cho hai số nguyên dương a, b. Hãy viết hàm tính ước số chúng lớn nhất, bội số chung nhỏ nhất của a,b.
import math
def gcd_lcm(a, b):
    gcd = math.gcd(a, b)
    lcm = (a * b)// gcd
    return gcd, lcm

a = int(input('Nhập số nguyên dương a: '))
b = int(input('Nhập số nguyên dương b: '))

gcd, lcm = gcd_lcm(a, b)
print(f'Ước chung lớn nhất cả {a} và {b} là: {gcd}')
print(f'Bội chung nhỏ nhất của {a} và {b} là: {lcm}')
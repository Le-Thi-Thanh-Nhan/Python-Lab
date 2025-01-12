n = int(input('Nhập số nguyên dương n: '))
s = 0
for i in range (1, n+1):
    s = s + 1/(2*i)
print('Tổng S = 1/2 + 1/4 + ... + 1/2n là:', s)

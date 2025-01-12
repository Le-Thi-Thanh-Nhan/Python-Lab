import math
n = int(input('Nhập số lượng phần tử của dãy số: '))
s = []

for i in range(n):
    s.append(int(input(f'Nhập phần tử thứ {i+1}: ')))

tong_chan = 0
for i in s:
    if i % 2 == 0:
        tong_chan += i

max_num = max(s)

print(f'Tổng các số chẵn trong dãy là: {tong_chan}')
print(f'Phần tử lớn nhất trong dãy là: {max_num}')
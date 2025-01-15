import math
n = int(input('Nhap so luong phan tu n: '))
s = []

for i in range (n):
    s.append(int(input(f'Nhap phan tu thu {i+1} : ')))

tong_chan = 0
for i in s:
    if i % 2 == 0:
        tong_chan += i

max_num = max(s)

print('Tong cac so chan trong day so la: ', tong_chan)
print('Phan tu lon nhat cua day la', max_num)
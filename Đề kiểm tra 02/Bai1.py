n = int(input('Nhap mot so nguyen duong n:'))
s = []
for i in range(0, n+1):
    if i % 2 == 0:
        s.append(i)
print(f'Day cac so chan tu 0 den {n} là: {s}')

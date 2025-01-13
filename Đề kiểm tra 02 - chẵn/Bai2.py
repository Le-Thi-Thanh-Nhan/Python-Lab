n = int(input('Nhap n: '))
s = []

for i in range(0, n):
    s.append(input(f'Nhap so nguyen thu {i + 1}: '))

s.sort()
print(f'Danh sach sau khi sap xep la: {s}')

s.sort(reverse=True)
print(f'Danh sach sau khi sap xep giam dan la: {s}')
#Sắp xếp tăng dần, giảm dần, tìm kiếm một số trong dãy số
s = list(map(int, input('Nhập dãy số cách nhau bởi dấu cách: ').split()))

 #sap xep tang dan
s.sort()
print(f'Dãy số sau khi sắp xếp tăng dần là: {s}')

 #sap xep giam dan
s.sort(reverse=True)
print(f'Dãy số sau khi sắp xếp giảm dần là: {s}')

x = int(input('Nhap so can tim: '))
if x in s:
    print(f'{x} có trong dãy số')
   
else:
    print(f'{x} không có trong dãy số')
    

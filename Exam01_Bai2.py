#Cho dãy n số nguyên (0<n<100). Hãy thực hiện:
#a) Tính tổng các phần tử là số chẵn
#b) Tìm phần tử lớn nhất của dãy

n = int(input("Nhập số lượng phần tử của dãy: "))
a = []
for i in range(n):
    temp = int(input(f"Nhập phần tử thứ {i+1}: "))
    a.append(temp)

tong = 0
for i in a:
    if i % 2 == 0:
        tong = tong + i
print("Tổng các phần tử chẵn = %d"%tong)

max_a = max(a)
print('Phần tử lớn nhất của dãy là: ', max_a)




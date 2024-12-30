#Bài 1: Cho số nguyên dương . Hãy viết hàm tính tổng
#S = 1 + 1/2! + 1/3! + ... + 1/n!
import math

def tinh_tong(n):
    S = 0
    for i in range(1, n + 1):
        S += 1 / math.factorial(i)
    return S + 1  # Cộng thêm 1 để bao gồm thành phần đầu tiên 1

# Nhập số nguyên dương từ bàn phím
n = int(input("Nhập một số nguyên dương: "))

# Tính tổng và in kết quả
S = tinh_tong(n)
print(f"Tổng S = {S}")

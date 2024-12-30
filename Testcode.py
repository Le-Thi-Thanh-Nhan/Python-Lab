# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Nhập số nguyên dương từ bàn phím
n = int(input("Nhập một số nguyên dương: "))

# Kiểm tra và in kết quả
if is_prime(n):
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} là hợp số.")

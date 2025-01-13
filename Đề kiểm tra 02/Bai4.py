# Nhập danh sách số nguyên từ bàn phím
arr = list(map(int, input("Nhập danh sách các số nguyên, cách nhau bằng dấu cách: ").split()))

# Áp dụng thuật toán Kadane
max_so_far = arr[0]
max_ending_here = arr[0]

for i in range(1, len(arr)):
    max_ending_here = max(arr[i], max_ending_here + arr[i])
    if max_ending_here > max_so_far:
        max_so_far = max_ending_here

# In kết quả
print("Tổng lớn nhất của dãy con liên tục là:", max_so_far)

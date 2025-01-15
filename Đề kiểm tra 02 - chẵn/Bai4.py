#tìm tất cả các hoán vị có thể của một chuỗi ký tự nhập vào từ người dùng
from itertools import permutations
chuoi = input('Nhap vao mot chuoi: ')
hoan_vi = permutations(chuoi)
print('Cac hoan vi co the cua chuoi la: ')
for p in hoan_vi:
    print(''.join(p))


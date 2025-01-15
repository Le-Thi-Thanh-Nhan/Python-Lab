class MATHANG:
    def __init__(self, maHang = '', tenHangSX = '', donGia = 0, soLuong = 0):
        self.maHang = maHang
        self.tenHangSX = tenHangSX
        self.donGia = donGia
        self.soLuong = soLuong

    def __del__(self):
        pass

    def Nhap(self):
        self.maHang = input('Nhap ma hang: ')
        self.tenHangSX = input('Nhap ten hang san xuat: ')
        self.donGia = input('Nhap don gia: ')
        self.soLuong = input('Nhap so luong: ')

    def Xuat(self):
        print('Ma hang: ', self.maHang)
        print('Ten hang san xuat: ', self.tenHangSX)
        print('Don gia: ', self.donGia)
        print('So luong: ', self.soLuong)

def main():
    n = int(input('Nhap so luong mat hang: '))
    dsMATHANG = []

    for i in range (n):
        print(f'Nhap mat hang thu {i + 1}: ')
        mh = MATHANG()
        mh.Nhap()
        dsMATHANG.append(mh)
        print()

    dsMATHANG.sort(key= lambda x: x.soLuong, reverse = True)

    print('DANH SACH MAT HANG SAP XEP THEO CHIEU GIAM DAN THEO SO LUONG: ')
    for i in range (len(dsMATHANG)):
        print(f'Thong tin mat hang thu {i+1}: ')
        dsMATHANG[i].Xuat()
        print()

    k = int(input('Nhap vi tri can xoa: '))
    dsMATHANG.pop(k-1)
    
    print('DANH SACH MAT HANG SAU KHI XOA: ')
    for i in range (len(dsMATHANG)):
        print(f'Thong tin mat hang thu {i+1}: ')
        dsMATHANG[i].Xuat()
        print()

if __name__ == '__main__':
    main()

    

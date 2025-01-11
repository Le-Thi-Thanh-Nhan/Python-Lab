class HANGHOA:
    def __init__(self, maHang = '', tenHang = '', donGia = 0.0):
        self.maHang = maHang
        self.tenHang = tenHang
        self.donGia = donGia

    def __del__(self):
        pass

    def Nhap(self):
        self.maHang = input('Nhập mã hàng: ')
        self.tenHang = input('Nhập tên hãng sản xuất: ')
        self.donGia = input('Nhập đơn giá: ')

    def Xuat(self):
        print('Mã hàng: ', self.maHang)
        print('Tên hãng: ', self.tenHang)
        print('Đơn giá: ', self.donGia)

def main():
    n = int(input('Nhập số lượng hàng hóa: '))
    dsHH = []
    for i in range(n):
        print('Nhập thông tin hàng hóa thứ ', i+1)
        hh = HANGHOA()
        hh.Nhap()
        dsHH.append(hh)
        print()
    
    for i in range(len(dsHH) - 1):
        for j in range(i+1, len(dsHH)):
            if dsHH[i].donGia < dsHH[j].donGia:
                dsHH[i], dsHH[j] = dsHH[j], dsHH[i]
    
    print('Danh sách hàng hóa sau khi sắp xếp theo giá giảm dần: ')
    for i in range(len(dsHH)):
        print('Thông tin hàng hóa thứ ', i+1)
        dsHH[i].Xuat()
        print()
        
    k = int(input('Nhập vị trí cần xóa: '))
    dsHH.pop(k-1)
    print('Danh sách hàng hóa sau khi xóa: ')
    for i in range(len(dsHH)):
        print('Thông tin hàng hóa thứ ', i+1)
        dsHH[i].Xuat()
        print()

if __name__ == '__main__':
    main()


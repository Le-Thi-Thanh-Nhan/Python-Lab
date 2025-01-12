import matplotlib.pyplot as plt
import numpy as np

# Tạo dữ liệu
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Vẽ đồ thị
plt.plot(x, y)

# Đặt tiêu đề cho biểu đồ
plt.title("Đồ thị hàm Cosine")

# Đặt nhãn cho trục x và trục y
plt.xlabel("Góc (radian)")
plt.ylabel("Giá trị Cosine")

# Đặt giới hạn cho trục x và trục y
plt.xlim(0, 2 * np.pi)
plt.ylim(-1, 1)

# Hiển thị biểu đồ
plt.show()

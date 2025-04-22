`matplotlib.pyplot` (thường được import với tên viết tắt là `plt`) là một thư viện cực kỳ phổ biến và mạnh mẽ trong Python dùng để vẽ các loại biểu đồ khác nhau, từ đơn giản đến phức tạp. Dưới đây là trình bày về cách sử dụng cơ bản thư viện này:

**1. Quy trình vẽ biểu đồ cơ bản với `matplotlib.pyplot`**

Hầu hết việc vẽ biểu đồ với `plt` đều tuân theo các bước chung sau:

1.  **Import thư viện:** Bước đầu tiên luôn là import thư viện.
    ```python
    import matplotlib.pyplot as plt
    ```
2.  **Chuẩn bị dữ liệu:** Bạn cần có dữ liệu muốn vẽ. Dữ liệu này có thể ở dạng danh sách (list), mảng NumPy (NumPy array), hoặc cột dữ liệu trong Pandas DataFrame/Series.
    ```python
    # Ví dụ dữ liệu
    x_values = [1, 2, 3, 4, 5]
    y_values = [2, 3, 5, 7, 11]
    categories = ['A', 'B', 'C', 'D']
    values = [10, 25, 15, 30]
    ```
3.  **Vẽ biểu đồ:** Sử dụng các hàm tương ứng của `plt` để vẽ loại biểu đồ bạn muốn.
    * `plt.plot()`: Vẽ biểu đồ đường (line chart).
    * `plt.scatter()`: Vẽ biểu đồ điểm (scatter plot).
    * `plt.bar()`: Vẽ biểu đồ cột đứng (vertical bar chart).
    * `plt.barh()`: Vẽ biểu đồ cột ngang (horizontal bar chart).
    * `plt.hist()`: Vẽ biểu đồ tần suất (histogram).
    * `plt.pie()`: Vẽ biểu đồ tròn (pie chart).
    * ... và nhiều hàm khác.
4.  **Tùy chỉnh biểu đồ (Quan trọng):** Thêm các yếu tố để biểu đồ trở nên rõ ràng và dễ hiểu hơn.
    * `plt.title("Tiêu đề biểu đồ")`: Đặt tiêu đề cho biểu đồ.
    * `plt.xlabel("Nhãn trục X")`: Đặt nhãn cho trục hoành (X).
    * `plt.ylabel("Nhãn trục Y")`: Đặt nhãn cho trục tung (Y).
    * `plt.legend()`: Hiển thị chú giải (hữu ích khi có nhiều đường/cột trên cùng biểu đồ).
    * `plt.grid(True)`: Hiển thị lưới.
    * `plt.xticks(...)`, `plt.yticks(...)`: Tùy chỉnh các giá trị hiển thị trên trục.
    * Thay đổi màu sắc, kiểu đường, kiểu điểm đánh dấu,...
5.  **Hiển thị hoặc lưu biểu đồ:**
    * `plt.show()`: Hiển thị biểu đồ lên màn hình.
    * `plt.savefig("ten_file.png")`: Lưu biểu đồ thành file ảnh (ví dụ: .png, .jpg, .pdf). **Lưu ý:** Gọi `plt.savefig()` *trước* `plt.show()`, nếu không file lưu có thể bị trống.

**2. Các loại biểu đồ phổ biến và ví dụ**

Dưới đây là ví dụ về cách vẽ một số loại biểu đồ thông dụng:

**a. Biểu đồ đường (Line Chart) - `plt.plot()`**

Thường dùng để thể hiện xu hướng thay đổi của dữ liệu theo thời gian hoặc một chuỗi liên tục.

```python
import matplotlib.pyplot as plt

# Dữ liệu
years = [2018, 2019, 2020, 2021, 2022]
sales = [100, 120, 90, 150, 180]

# Vẽ
plt.plot(years, sales, marker='o', linestyle='-', color='b') # marker='o' là điểm tròn, linestyle='-' là đường liền, color='b' là màu xanh dương

# Tùy chỉnh
plt.title("Doanh số bán hàng qua các năm")
plt.xlabel("Năm")
plt.ylabel("Doanh số (triệu)")
plt.grid(True)
plt.xticks(years) # Đảm bảo hiển thị các năm trên trục X

# Hiển thị
plt.show()
```

**b. Biểu đồ điểm (Scatter Plot) - `plt.scatter()`**

Thường dùng để xem mối quan hệ (tương quan) giữa hai biến số liệu.

```python
import matplotlib.pyplot as plt

# Dữ liệu
heights = [150, 160, 170, 180, 165, 175]
weights = [50, 60, 70, 80, 65, 75]

# Vẽ
plt.scatter(heights, weights, color='r', marker='x') # color='r' là đỏ, marker='x' là dấu x

# Tùy chỉnh
plt.title("Mối quan hệ giữa Chiều cao và Cân nặng")
plt.xlabel("Chiều cao (cm)")
plt.ylabel("Cân nặng (kg)")
plt.grid(True)

# Hiển thị
plt.show()
```

**c. Biểu đồ cột (Bar Chart) - `plt.bar()`**

Thường dùng để so sánh giá trị giữa các nhóm hoặc danh mục khác nhau.

```python
import matplotlib.pyplot as plt

# Dữ liệu
products = ['Sản phẩm A', 'Sản phẩm B', 'Sản phẩm C', 'Sản phẩm D']
units_sold = [500, 850, 300, 600]

# Vẽ
plt.bar(products, units_sold, color=['skyblue', 'lightcoral', 'lightgreen', 'gold']) # Có thể đặt màu cho từng cột

# Tùy chỉnh
plt.title("Số lượng bán ra của các sản phẩm")
plt.xlabel("Sản phẩm")
plt.ylabel("Số lượng bán ra")
plt.xticks(rotation=15) # Xoay nhẹ nhãn trục X nếu dài

# Hiển thị
plt.show()

# Ví dụ cột ngang: plt.barh(products, units_sold, ...)
```

**d. Biểu đồ tần suất (Histogram) - `plt.hist()`**

Dùng để xem sự phân bố của một tập dữ liệu số liệu (có bao nhiêu giá trị rơi vào từng khoảng).

```python
import matplotlib.pyplot as plt
import numpy as np # Thường dùng numpy để tạo dữ liệu mẫu

# Dữ liệu (ví dụ: điểm thi của sinh viên)
scores = np.random.randint(0, 101, size=100) # 100 điểm ngẫu nhiên từ 0 đến 100

# Vẽ histogram với 10 khoảng (bins)
plt.hist(scores, bins=10, color='purple', edgecolor='black') # edgecolor là màu viền cột

# Tùy chỉnh
plt.title("Phân bố điểm thi")
plt.xlabel("Khoảng điểm")
plt.ylabel("Số lượng sinh viên")

# Hiển thị
plt.show()
```

**e. Biểu đồ tròn (Pie Chart) - `plt.pie()`**

Dùng để thể hiện tỷ lệ phần trăm của các phần trong một tổng thể. Nên cẩn thận khi dùng với quá nhiều phần.

```python
import matplotlib.pyplot as plt

# Dữ liệu
labels = ['Nhóm 1', 'Nhóm 2', 'Nhóm 3', 'Nhóm 4']
sizes = [15, 30, 45, 10] # Tỷ lệ phần trăm (tổng nên là 100, hoặc matplotlib tự tính)
explode = (0, 0.1, 0, 0) # Tách "Nhóm 2" ra một chút

# Vẽ
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
# autopct hiển thị phần trăm, shadow tạo bóng, startangle xoay góc bắt đầu

# Tùy chỉnh
plt.title("Tỷ lệ các nhóm")
plt.axis('equal') # Đảm bảo biểu đồ tròn không bị méo

# Hiển thị
plt.show()
```

**3. Vẽ nhiều biểu đồ trên cùng một Figure (Subplots)**

Khi bạn muốn hiển thị nhiều biểu đồ liên quan cùng lúc, bạn có thể dùng subplots. Cách phổ biến là dùng `plt.subplots()`.

```python
import matplotlib.pyplot as plt
import numpy as np

# Dữ liệu
x = np.linspace(0, 10, 100) # 100 điểm từ 0 đến 10
y1 = np.sin(x)
y2 = np.cos(x)

# Tạo một Figure và một lưới chứa các Axes (subplot)
# fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5)) # 1 hàng, 2 cột
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5)) # Cách khác để lấy trực tiếp 2 axes

# Vẽ trên subplot thứ nhất (ax1)
ax1.plot(x, y1, color='blue', label='sin(x)')
ax1.set_title('Biểu đồ Sin')
ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)')
ax1.grid(True)
ax1.legend()

# Vẽ trên subplot thứ hai (ax2)
ax2.plot(x, y2, color='red', label='cos(x)')
ax2.set_title('Biểu đồ Cos')
ax2.set_xlabel('x')
ax2.set_ylabel('cos(x)')
ax2.grid(True)
ax2.legend()

# Điều chỉnh layout chung cho đẹp
plt.tight_layout()

# Hiển thị
plt.show()
```

**Tổng kết:**

`matplotlib.pyplot` cung cấp một giao diện rất linh hoạt để tạo ra hầu hết các loại biểu đồ tĩnh trong Python. Bằng cách kết hợp các hàm vẽ cơ bản và các tùy chỉnh, bạn có thể tạo ra những hình ảnh trực quan hóa dữ liệu hiệu quả. Cách tốt nhất để thành thạo là thực hành với dữ liệu của chính bạn!
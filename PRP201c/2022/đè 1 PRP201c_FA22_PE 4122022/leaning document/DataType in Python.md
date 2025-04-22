Python có nhiều kiểu dữ liệu (data types) được tích hợp sẵn để biểu diễn các loại thông tin khác nhau. Python là ngôn ngữ kiểu động, nghĩa là bạn không cần khai báo kiểu dữ liệu của biến một cách tường minh; Python sẽ tự xác định kiểu dựa trên giá trị được gán.

Dưới đây là các kiểu dữ liệu cơ bản và phổ biến trong Python:

**1. Kiểu Số (Numeric Types)**

* **`int` (Integer - Số nguyên):** Biểu diễn các số nguyên (không có phần thập phân), bao gồm số dương, số âm và số 0. Số nguyên trong Python có thể lớn tùy ý (chỉ giới hạn bởi bộ nhớ).
    * *Tính chất:* Bất biến (Immutable - giá trị không thể thay đổi sau khi tạo).
    * *Ví dụ:* `so_luong = 100`, `nhiet_do = -5`, `nam = 2025`
* **`float` (Floating-Point - Số thực):** Biểu diễn các số có phần thập phân hoặc số ở dạng mũ (khoa học).
    * *Tính chất:* Bất biến (Immutable).
    * *Ví dụ:* `pi = 3.14159`, `gia = 99.99`, `toc_do_anh_sang = 3e8` (tức là 3 * 10^8)
* **`complex` (Complex - Số phức):** Biểu diễn số phức với phần thực và phần ảo (kết thúc bằng `j` hoặc `J`). Ít phổ biến trong lập trình hàng ngày.
    * *Tính chất:* Bất biến (Immutable).
    * *Ví dụ:* `z = 3 + 4j`

**2. Kiểu Tuần tự (Sequence Types)** - Lưu trữ các mục theo một thứ tự cụ thể.

* **`str` (String - Chuỗi):** Biểu diễn một chuỗi các ký tự Unicode (văn bản). Được định nghĩa bằng dấu nháy đơn (`'`), nháy đôi (`"`) hoặc ba dấu nháy (`'''` hoặc `"""` cho chuỗi nhiều dòng).
    * *Tính chất:* Bất biến (Immutable).
    * *Ví dụ:* `ten = "Nguyễn Văn A"`, `loi_chao = 'Xin chào!'`, `mo_ta = """Đây là một\nmô tả nhiều dòng."""`
* **`list` (List - Danh sách):** Lưu trữ một dãy các mục (có thể thuộc các kiểu khác nhau) theo thứ tự. Các mục có thể được truy cập, thay đổi, thêm hoặc xóa thông qua chỉ số (index).
    * *Tính chất:* **Khả biến (Mutable - có thể thay đổi)**.
    * *Ví dụ:* `diem_so = [8, 9, 7, 10]`, `thong_tin = ["An", 25, 1.75, True]`, `danh_sach_rong = []`
* **`tuple` (Tuple - Bộ):** Tương tự như `list` nhưng các phần tử **không thể thay đổi** sau khi tạo. Thường dùng cho các tập hợp giá trị cố định.
    * *Tính chất:* Bất biến (Immutable).
    * *Ví dụ:* `toa_do = (10, 20)`, `mau_sac_rgb = (255, 0, 0)`
* **`range`:** Biểu diễn một dãy số bất biến, thường dùng để lặp trong vòng lặp `for`. Nó tạo ra các số khi cần thay vì lưu trữ toàn bộ dãy số.
    * *Tính chất:* Bất biến (Immutable).
    * *Ví dụ:* `range(5)` (đại diện 0, 1, 2, 3, 4), `range(1, 10, 2)` (đại diện 1, 3, 5, 7, 9)

**3. Kiểu Ánh xạ (Mapping Type)**

* **`dict` (Dictionary - Từ điển):** Lưu trữ dữ liệu dưới dạng các cặp **khóa:giá trị (key:value)**. Mỗi khóa (key) phải là duy nhất và thuộc kiểu bất biến (thường là `str` hoặc `int`). Giá trị (value) có thể là bất kỳ kiểu nào. Từ Python 3.7 trở đi, `dict` duy trì thứ tự các mục được thêm vào.
    * *Tính chất:* **Khả biến (Mutable)**.
    * *Ví dụ:* `sinh_vien = {"ma_sv": "SV001", "ten": "Bình", "tuoi": 20}`, `tu_dien_rong = {}`

**4. Kiểu Tập hợp (Set Types)** - Lưu trữ các phần tử **duy nhất**, không theo thứ tự.

* **`set` (Set - Tập hợp):** Lưu trữ một tập hợp các phần tử duy nhất (không trùng lặp), không có thứ tự cụ thể. Hiệu quả cho việc kiểm tra sự tồn tại của phần tử và các phép toán tập hợp (hợp, giao, hiệu). Các phần tử phải thuộc kiểu bất biến.
    * *Tính chất:* **Khả biến (Mutable)**.
    * *Ví dụ:* `so_nguyen_to = {2, 3, 5, 7, 7, 3}` (sẽ là `{2, 3, 5, 7}`), `ky_tu_duy_nhat = set("banana")` (sẽ là `{'b', 'a', 'n'}`)
* **`frozenset` (Frozen Set - Tập hợp cố định):** Phiên bản bất biến của `set`. Không thể thêm/xóa phần tử sau khi tạo. Có thể dùng làm khóa `dict` hoặc phần tử `set` khác.
    * *Tính chất:* Bất biến (Immutable).
    * *Ví dụ:* `tap_hop_bat_bien = frozenset([1, 2, 'a'])`

**5. Kiểu Luận lý (Boolean Type)**

* **`bool` (Boolean):** Chỉ có hai giá trị: `True` (Đúng) và `False` (Sai). Thường là kết quả của các phép so sánh hoặc điều kiện logic.
    * *Tính chất:* Bất biến (Immutable).
    * *Ví dụ:* `da_ket_hon = False`, `lon_hon_10 = (15 > 10)` (kết quả là `True`)

**6. Kiểu None (None Type)**

* **`NoneType`:** Có một giá trị duy nhất là `None`. Được dùng để biểu thị sự "không có giá trị", "rỗng" hoặc "null".
    * *Tính chất:* Bất biến (Immutable).
    * *Ví dụ:* `ket_qua = None`

**7. Kiểu Nhị phân (Binary Types)** - Dùng cho dữ liệu dạng byte.

* **`bytes`:** Dãy các byte (số nguyên từ 0-255) không thể thay đổi.
* **`bytearray`:** Dãy các byte có thể thay đổi.
* **`memoryview`:** Cung cấp cách truy cập bộ nhớ của dữ liệu nhị phân mà không cần sao chép.

**Kiểm tra kiểu dữ liệu:**

Bạn có thể dùng hàm `type()` để xác định kiểu dữ liệu của một biến:

```python
a = 10
b = "Xin chào"
c = [1, 2, 3]
d = {"id": 1}
e = True

print(type(a))  # Kết quả: <class 'int'>
print(type(b))  # Kết quả: <class 'str'>
print(type(c))  # Kết quả: <class 'list'>
print(type(d))  # Kết quả: <class 'dict'>
print(type(e))  # Kết quả: <class 'bool'>
```
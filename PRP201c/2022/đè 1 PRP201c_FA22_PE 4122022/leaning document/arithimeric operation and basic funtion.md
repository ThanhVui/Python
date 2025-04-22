Dưới đây là trình bày về các loại toán tử trong Python và các hàm/phương thức cơ bản thường dùng với các cấu trúc dữ liệu chính của nó.

**Phần 1: Các Toán tử trong Python (Operators)**

Toán tử là các ký hiệu đặc biệt dùng để thực hiện các phép toán trên các giá trị (toán hạng - operands).

**1. Toán tử Số học (Arithmetic Operators)**
Dùng để thực hiện các phép toán số học cơ bản.


* `+` : Phép cộng (Ví dụ: `5 + 3` kết quả là `8`)
* `-` : Phép trừ (Ví dụ: `5 - 3` kết quả là `2`)
* `*` : Phép nhân (Ví dụ: `5 * 3` kết quả là `15`)
* `/` : Phép chia (kết quả luôn là số thực - float) (Ví dụ: `5 / 2` kết quả là `2.5`)
* `%` : Phép chia lấy dư (Modulus) (Ví dụ: `5 % 2` kết quả là `1`)
* `**` : Phép lũy thừa (Ví dụ: `5 ** 2` kết quả là `25`)
* `//` : Phép chia lấy phần nguyên (Floor Division) (Ví dụ: `5 // 2` kết quả là `2`)


**2. Toán tử So sánh (Comparison Operators)**
Dùng để so sánh hai giá trị, kết quả trả về là `True` hoặc `False`.


* `==` : So sánh bằng (Ví dụ: `5 == 3` là `False`)
* `!=` : So sánh không bằng (Ví dụ: `5 != 3` là `True`)
* `>` : Lớn hơn (Ví dụ: `5 > 3` là `True`)
* `<` : Nhỏ hơn (Ví dụ: `5 < 3` là `False`)
* `>=` : Lớn hơn hoặc bằng (Ví dụ: `5 >= 5` là `True`)
* `<=` : Nhỏ hơn hoặc bằng (Ví dụ: `5 <= 3` là `False`)


**3. Toán tử Logic (Logical Operators)**
Dùng để kết hợp các biểu thức điều kiện, hoạt động trên các giá trị boolean (`True`, `False`).

* `and` : Logic VÀ (Trả về `True` nếu cả hai toán hạng đều `True`) (Ví dụ: `(5 > 3) and (2 < 4)` là `True`)
* `or` : Logic HOẶC (Trả về `True` nếu ít nhất một toán hạng là `True`) (Ví dụ: `(5 < 3) or (2 < 4)` là `True`)
* `not` : Logic PHỦ ĐỊNH (Đảo ngược trạng thái logic) (Ví dụ: `not (5 < 3)` là `True`)

**4. Toán tử Bitwise (Bitwise Operators)**
Thực hiện thao tác trên từng bit của các số nguyên. Ít phổ biến hơn cho người mới bắt đầu.

* `&` : Bitwise AND
* `|` : Bitwise OR
* `^` : Bitwise XOR
* `~` : Bitwise NOT (Phủ định bit)
* `<<` : Dịch trái (Left Shift)
* `>>` : Dịch phải (Right Shift)

**5. Toán tử Gán (Assignment Operators)**
Dùng để gán giá trị cho biến.

* `=` : Gán giá trị (Ví dụ: `x = 5`)
* `+=` : Cộng và gán (Ví dụ: `x += 3` tương đương `x = x + 3`)
* `-=`, `*=`, `/=`, `%=`, `**=`, `//=`, `&=`, `|=`, `^=`, `>>=`, `<<=`: Tương tự cho các phép toán khác.

**6. Toán tử Đồng nhất (Identity Operators)**
So sánh xem hai biến có trỏ đến **cùng một đối tượng** trong bộ nhớ hay không.

* `is` : Trả về `True` nếu hai biến là cùng một đối tượng.
* `is not` : Trả về `True` nếu hai biến không phải là cùng một đối tượng.


```python

a = [1, 2]
b = [1, 2]
c = a
print(a == b)    # Output: True (Giá trị giống nhau)
print(a is b)    # Output: False (Là hai đối tượng list khác nhau trong bộ nhớ)
print(a is c)    # Output: True (c và a trỏ đến cùng một đối tượng list)

```

**7. Toán tử Thành viên (Membership Operators)**

Kiểm tra xem một giá trị có tồn tại trong một chuỗi (string), danh sách (list), bộ (tuple), tập hợp (set), hoặc từ điển (dictionary - kiểm tra key) hay không.


* `in` : Trả về `True` nếu giá trị có trong chuỗi/tập hợp.
* `not in` : Trả về `True` nếu giá trị không có trong chuỗi/tập hợp.


```python
my_list = [1, 2, 3, 'a']
print(2 in my_list)      # Output: True
print('b' not in my_list) # Output: True
```


---


**Phần 2: Các Hàm và Phương thức Cơ bản với Cấu trúc Dữ liệu Python**


**1. Số (`int`, `float`)**


* **Hàm tích hợp sẵn:**
    * `abs(x)`: Trả về giá trị tuyệt đối của `x`.
    * `round(number, ndigits)`: Làm tròn số `number` đến `ndigits` chữ số thập phân (mặc định là 0).
    * `pow(base, exp)`: Tương đương `base ** exp`.
    * `int(x)`: Chuyển `x` thành số nguyên.
    * `float(x)`: Chuyển `x` thành số thực.

* **Module `math`:** Cần `import math`
    * `math.sqrt(x)`: Căn bậc hai.
    * `math.ceil(x)`: Làm tròn lên số nguyên gần nhất.
    * `math.floor(x)`: Làm tròn xuống số nguyên gần nhất.
    * `math.pi`, `math.e`: Hằng số Pi và e.


**2. Chuỗi (`str`) - Bất biến (Immutable)**

* **Phương thức (gọi bằng `chuoi.phuong_thuc()`):**
    * `.upper()` / `.lower()`: Chuyển thành chữ hoa/thường.
    * `.strip()` / `.lstrip()` / `.rstrip()`: Xóa khoảng trắng thừa ở hai đầu/trái/phải.
    * `.split(separator)`: Tách chuỗi thành list các chuỗi con dựa trên `separator`.
    * `separator.join(iterable)`: Nối các phần tử trong `iterable` thành một chuỗi bằng `separator`.
    * `.replace(old, new)`: Thay thế `old` bằng `new`.
    * `.startswith(prefix)` / `.endswith(suffix)`: Kiểm tra bắt đầu/kết thúc bằng chuỗi con.
    * `.find(sub)` / `.index(sub)`: Tìm vị trí `sub` (find trả về -1 nếu không thấy, index báo lỗi).
    * `.isdigit()` / `.isalpha()` / `.isalnum()`: Kiểm tra có phải toàn số/chữ/chữ và số không.
    * `.format(...)`: Định dạng chuỗi (cách cũ hơn f-string).


* **Hàm tích hợp sẵn:**

    * `len(chuoi)`: Trả về độ dài chuỗi.
* **Toán tử:** `+` (nối chuỗi), `*` (lặp lại chuỗi).
* **Indexing & Slicing:** `chuoi[index]`, `chuoi[start:stop:step]` để truy cập ký tự/chuỗi con.

**3. Danh sách (`list`) - Khả biến (Mutable)**

* **Phương thức:**
    * `.append(item)`: Thêm `item` vào cuối list.
    * `.extend(iterable)`: Nối các phần tử từ `iterable` vào cuối list.
    * `.insert(index, item)`: Chèn `item` vào vị trí `index`.
    * `.remove(item)`: Xóa phần tử `item` đầu tiên tìm thấy (báo lỗi nếu không có).
    * `.pop(index=-1)`: Xóa và trả về phần tử tại `index` (mặc định là cuối list).
    * `.clear()`: Xóa hết phần tử.
    * `.index(item)`: Trả về vị trí `item` đầu tiên (báo lỗi nếu không có).
    * `.count(item)`: Đếm số lần `item` xuất hiện.
    * `.sort()`: Sắp xếp list (thay đổi list gốc).
    * `.reverse()`: Đảo ngược thứ tự list (thay đổi list gốc).
    * `.copy()`: Tạo bản sao nông (shallow copy) của list.
* **Hàm tích hợp sẵn:**
    * `len(list)`: Số lượng phần tử.
    * `sum(list)`: Tổng các phần tử (nếu là số).
    * `min(list)` / `max(list)`: Phần tử nhỏ nhất/lớn nhất.
    * `sorted(list)`: Trả về một list mới đã được sắp xếp (không đổi list gốc).
* **Toán tử:** `+` (nối list), `*` (lặp lại list).
* **Indexing & Slicing:** `list[index]`, `list[start:stop:step]`, gán giá trị `list[index] = value`.

**4. Bộ (`tuple`) - Bất biến (Immutable)**

* **Phương thức:**
    * `.index(item)`: Tìm vị trí `item`.
    * `.count(item)`: Đếm số lần `item` xuất hiện.
* **Hàm tích hợp sẵn:** `len()`, `sum()`, `min()`, `max()`, `sorted()` (trả về list).
* **Toán tử:** `+`, `*`.
* **Indexing & Slicing:** `tuple[index]`, `tuple[start:stop:step]`.

**5. Từ điển (`dict`) - Khả biến (Mutable)**

* **Phương thức:**
    * `.keys()`: Trả về view chứa các key.
    * `.values()`: Trả về view chứa các value.
    * `.items()`: Trả về view chứa các cặp (key, value).
    * `.get(key, default=None)`: Lấy value của `key`, trả về `default` nếu key không tồn tại (không báo lỗi).
    * `.pop(key, default)`: Xóa và trả về value của `key` (báo lỗi nếu key không có và không có default).
    * `.popitem()`: Xóa và trả về cặp (key, value) cuối cùng (trong Python 3.7+).
    * `.update(other_dict)`: Cập nhật dict với các cặp key-value từ `other_dict`.
    * `.clear()`: Xóa hết các cặp key-value.
    * `.copy()`: Tạo bản sao nông.
* **Hàm tích hợp sẵn:** `len(dict)` (số cặp key-value).
* **Truy cập/Gán:** `dict[key]`, `dict[key] = value`.
* **Toán tử:** Dùng `in` để kiểm tra key có tồn tại không (`key in dict`).

**6. Tập hợp (`set`) - Khả biến (Mutable), phần tử duy nhất**

* **Phương thức:**
    * `.add(item)`: Thêm phần tử (nếu chưa có).
    * `.update(iterable)`: Thêm các phần tử từ `iterable`.
    * `.remove(item)`: Xóa `item` (báo lỗi nếu không có).
    * `.discard(item)`: Xóa `item` (không báo lỗi nếu không có).
    * `.pop()`: Xóa và trả về một phần tử bất kỳ.
    * `.clear()`: Xóa hết phần tử.
    * `.copy()`: Tạo bản sao nông.
    * `.union(other_set)` hoặc `set1 | set2`: Phép hợp.
    * `.intersection(other_set)` hoặc `set1 & set2`: Phép giao.
    * `.difference(other_set)` hoặc `set1 - set2`: Phép hiệu.
    * `.symmetric_difference(other_set)` hoặc `set1 ^ set2`: Phép hiệu đối xứng.
    * `.issubset(other_set)` hoặc `set1 <= set2`: Kiểm tra tập con.
    * `.issuperset(other_set)` hoặc `set1 >= set2`: Kiểm tra tập cha.
* **Hàm tích hợp sẵn:** `len(set)`.
* **Toán tử:** Dùng `in` để kiểm tra thành viên.


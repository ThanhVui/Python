Trong Python, việc đọc file là một chức năng cơ bản và bạn **không cần import một thư viện (library) đặc biệt nào** cho các thao tác đọc/ghi file văn bản thông thường. Chức năng này được tích hợp sẵn thông qua hàm `open()`.

Tuy nhiên, có nhiều **cách (phương thức)** khác nhau để đọc nội dung từ file sau khi đã mở nó. Dưới đây là các cách phổ biến:

**1. Sử dụng `with open(...)` (Cách khuyến nghị)**

Đây là cách tốt nhất và an toàn nhất để làm việc với file trong Python vì nó đảm bảo file sẽ **tự động được đóng lại** sau khi khối lệnh `with` kết thúc, ngay cả khi có lỗi xảy ra.

```python
# Giả sử file 'Text.txt' có nội dung là: 2 1 6 8
file_name = "Text.txt"

try:
    with open(file_name, 'r') as file_object:
        # Các cách đọc bên trong 'with':

        # Cách 1: Đọc toàn bộ nội dung file vào một chuỗi duy nhất
        content_str = file_object.read()
        print("Đọc bằng read():", repr(content_str)) # repr để thấy ký tự đặc biệt như \n
        # Bạn cần xử lý chuỗi này (ví dụ: tách bằng split())
        numbers_list = content_str.split() # Tách theo khoảng trắng/newline
        print("Danh sách số (dạng chuỗi):", numbers_list)

        # Cách 2: Đọc từng dòng một (nếu mỗi số/dữ liệu nằm trên một dòng riêng)
        # Dùng vòng lặp for - cách này hiệu quả về bộ nhớ cho file lớn
        print("Đọc từng dòng bằng vòng lặp:")
        lines_list = []
        for line in file_object:
            cleaned_line = line.strip() # Loại bỏ khoảng trắng thừa và ký tự xuống dòng (\n)
            if cleaned_line: # Đảm bảo dòng không rỗng
               lines_list.append(cleaned_line)
               print("Đã đọc dòng:", repr(cleaned_line))
        print("Danh sách các dòng:", lines_list)
        # Nếu mỗi dòng chỉ có 1 số, list này chính là list số (dạng chuỗi)
        # Nếu một dòng có nhiều số cách nhau bởi khoảng trắng, bạn cần split thêm:
        numbers_from_lines = []
        for line in lines_list:
            numbers_from_lines.extend(line.split())
        print("Số từ các dòng:", numbers_from_lines)


        # Cách 3: Đọc toàn bộ các dòng vào một danh sách (list)
        file_object.seek(0) # Quay lại đầu file nếu đã đọc trước đó
        all_lines = file_object.readlines() # Trả về list các chuỗi, mỗi chuỗi là 1 dòng còn \n
        print("Đọc bằng readlines():", all_lines)
        # Cần xử lý từng phần tử trong list này (dùng strip())
        cleaned_lines = [line.strip() for line in all_lines]
        print("Danh sách dòng đã làm sạch:", cleaned_lines)

        # Cách 4: Đọc một dòng duy nhất tại vị trí hiện tại
        file_object.seek(0) # Quay lại đầu file
        first_line = file_object.readline()
        print("Đọc bằng readline():", repr(first_line))
        second_line = file_object.readline() # Đọc dòng tiếp theo
        print("Đọc tiếp bằng readline():", repr(second_line))

    # File đã tự động được đóng ở đây

except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy file '{file_name}'")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")

```

* **`'r'`**: Chế độ đọc (read - mặc định). Các chế độ khác gồm `'w'` (ghi - write, xóa nội dung cũ), `'a'` (ghi nối - append), `'r+'` (đọc và ghi), `'b'` (chế độ nhị phân - binary), ...
* **`file_object.read()`**: Đọc toàn bộ file thành 1 string. Cẩn thận với file lớn.
* **`file_object.readline()`**: Đọc 1 dòng (đến ký tự `\n`).
* **`file_object.readlines()`**: Đọc toàn bộ file thành 1 list các string (mỗi string là 1 dòng). Tốn bộ nhớ nếu file lớn.
* **Vòng lặp `for line in file_object`**: Đọc file theo từng dòng, hiệu quả nhất về bộ nhớ cho file văn bản.

**2. Sử dụng `open()` và `close()` thủ công (Cách cũ, không khuyến nghị)**

Bạn phải tự mình gọi `file_object.close()` để đóng file. Nếu quên hoặc có lỗi xảy ra trước khi `close()`, file có thể không được đóng đúng cách.

```python
file_object = None # Khởi tạo để dùng trong finally
try:
    file_object = open("Text.txt", "r")
    content = file_object.read()
    # ... xử lý content ...
    print("Đọc bằng open/close thủ công:", content.split())
except FileNotFoundError:
    print("Lỗi: Không tìm thấy file")
finally:
    if file_object: # Kiểm tra file đã mở thành công chưa
        file_object.close() # Phải tự đóng file!
        print("File đã được đóng thủ công.")
```

**3. Sử dụng các thư viện cho định dạng file cụ thể (Không cần cho bài này)**

* **`csv`**: Đọc/ghi file CSV (Comma Separated Values).
* **`json`**: Đọc/ghi file định dạng JSON.
* **`pandas`**: Thư viện mạnh mẽ để đọc nhiều định dạng dữ liệu dạng bảng (CSV, Excel, JSON, SQL...) vào cấu trúc DataFrame (thường dùng trong phân tích dữ liệu).

**Đối với bài toán của bạn (câu 2):**

* Bạn cần đọc file "Text.txt". Giả sử nội dung file là các chữ số cách nhau bởi khoảng trắng (ví dụ: `2 1 6 8`) hoặc mỗi chữ số trên một dòng.
* Cách **khuyến nghị** là dùng `with open(...)`.
* Bên trong `with`, bạn có thể dùng `file_object.read().split()` nếu các số nằm trên cùng một dòng và cách nhau bởi khoảng trắng. Hoặc dùng vòng lặp `for line in file_object` rồi `line.strip()` nếu mỗi số nằm trên một dòng riêng. Kết quả cuối cùng bạn cần là một danh sách các chuỗi chứa chữ số: `['2', '1', '6', '8']`.





Dưới đây là một số regex bạn có thể sử dụng với `re.split()` trong Python để tách chuỗi theo các điều kiện khác nhau:

### 1. Tách theo khoảng trắng (bao gồm cả khoảng trắng đơn và nhiều khoảng trắng liên tiếp)
```python
import re

text = "2   1  6  8"
result = re.split(r'\s+', text)  # \s+ sẽ khớp với một hoặc nhiều khoảng trắng
print(result)  # Output: ['2', '1', '6', '8']
```

### 2. Tách theo số
```python
import re

text = "abc123def456ghi789"
result = re.split(r'\d+', text)  # \d+ sẽ khớp với một hoặc nhiều chữ số
print(result)  # Output: ['abc', 'def', 'ghi', '']
```

### 3. Tách theo ký tự không phải chữ cái hoặc số (non-alphanumeric)
```python
import re

text = "abc,123;def.456|ghi"
result = re.split(r'\W+', text)  # \W+ sẽ khớp với một hoặc nhiều ký tự không phải chữ cái hoặc số
print(result)  # Output: ['abc', '123', 'def', '456', 'ghi']
```

### 4. Tách theo cả khoảng trắng và dấu câu
```python
import re

text = "Hello, world! This is a test."
result = re.split(r'[,\s.!?]+', text)  # Khớp với dấu câu (, . ! ?) hoặc khoảng trắng
print(result)  # Output: ['Hello', 'world', 'This', 'is', 'a', 'test', '']
```

### 5. Tách theo một mẫu phức tạp (ví dụ: khoảng trắng hoặc dấu chấm phẩy)
```python
import re

text = "2; 1  6;8"
result = re.split(r'[;\s]+', text)  # Khớp với dấu chấm phẩy hoặc khoảng trắng
print(result)  # Output: ['2', '1', '6', '8']
```

### 6. Tách theo chữ cái
```python
import re

text = "123abc456def789ghi"
result = re.split(r'[a-zA-Z]+', text)  # Khớp với một hoặc nhiều chữ cái
print(result)  # Output: ['123', '456', '789', '']
```

Bạn có thể thay đổi các mẫu regex (`r'...'`) để phù hợp với yêu cầu cụ thể của mình.
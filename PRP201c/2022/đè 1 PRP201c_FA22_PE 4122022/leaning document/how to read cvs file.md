để đọc file CSV trong Python, bạn có thể sử dụng thư viện tích hợp sẵn `csv`. Thư viện này cung cấp các công cụ mạnh mẽ và dễ sử dụng để xử lý dữ liệu dạng bảng được phân tách bằng dấu phẩy (hoặc các dấu phân cách khác).

Dưới đây là các cách phổ biến để đọc file CSV bằng thư viện `csv`:

**Giả sử bạn có file `data.csv` với nội dung sau:**

```csv
ID,Ten,Email
1,Nguyen Van A,a.nguyen@example.com
2,Tran Thi B,b.tran@example.com
3,Le Van C,c.le@example.com
```

**Cách 1: Sử dụng `csv.reader` (Đọc từng dòng thành danh sách - list)**

Cách này đọc mỗi dòng trong file CSV thành một danh sách (list), trong đó mỗi phần tử là một giá trị trong cột của dòng đó.

```python
import csv

file_csv = 'data.csv'

try:
    # Mở file CSV để đọc ('r' mode)
    # encoding='utf-8' là lựa chọn phổ biến và an toàn cho nhiều loại dữ liệu
    # newline='' rất quan trọng để tránh các dòng trống không mong muốn khi đọc
    with open(file_csv, mode='r', newline='', encoding='utf-8') as file:
        # Tạo một đối tượng reader
        csv_reader = csv.reader(file)

        # Optional: Đọc dòng tiêu đề (header) nếu có và bỏ qua nó trong vòng lặp
        try:
            header = next(csv_reader)
            print(f"Dòng tiêu đề: {header}")
        except StopIteration:
            print("Lỗi: File CSV trống.")
            exit() # Thoát nếu file trống

        # Lặp qua từng dòng còn lại trong file CSV
        print("\nNội dung file:")
        for dong in csv_reader:
            # Mỗi 'dong' là một list các chuỗi, ví dụ: ['1', 'Nguyen Van A', 'a.nguyen@example.com']
            if dong: # Đảm bảo dòng không rỗng
                print(f"  ID: {dong[0]}, Tên: {dong[1]}, Email: {dong[2]}")
            else:
                print("  - Gặp dòng trống.")

except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy file '{file_csv}'")
except Exception as e:
    print(f"Đã xảy ra lỗi không mong muốn: {e}")
```

**Cách 2: Sử dụng `csv.DictReader` (Đọc từng dòng thành từ điển - dictionary)**

Cách này tiện lợi hơn vì nó đọc mỗi dòng thành một dictionary. Các *keys* của dictionary là tên cột lấy từ dòng tiêu đề (header row) của file CSV. Điều này giúp mã nguồn dễ đọc và dễ bảo trì hơn vì bạn truy cập dữ liệu qua tên cột thay vì chỉ số.

```python
import csv

file_csv = 'data.csv'

try:
    with open(file_csv, mode='r', newline='', encoding='utf-8') as file:
        # Tạo một đối tượng DictReader
        # Tự động sử dụng dòng đầu tiên làm tên cột (keys)
        csv_dict_reader = csv.DictReader(file)

        # Optional: In ra tên các cột đã được nhận dạng
        print(f"Tên các cột (từ header): {csv_dict_reader.fieldnames}")

        # Lặp qua từng dòng trong file
        print("\nNội dung file (dạng Dictionary):")
        for dong_dict in csv_dict_reader:
            # Mỗi 'dong_dict' là một dictionary, ví dụ:
            # {'ID': '1', 'Ten': 'Nguyen Van A', 'Email': 'a.nguyen@example.com'}
            if dong_dict: # Đảm bảo dictionary không rỗng (ít khi xảy ra với DictReader)
                print(f"  ID: {dong_dict['ID']}, Tên: {dong_dict['Ten']}, Email: {dong_dict['Email']}")
            # Lưu ý: Giá trị trong dictionary vẫn là dạng chuỗi (string)

except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy file '{file_csv}'")
except Exception as e:
    print(f"Đã xảy ra lỗi không mong muốn: {e}")

```

**Xử lý các tùy chọn khác:**

* **Dấu phân cách khác (Delimiter):** Nếu file của bạn không dùng dấu phẩy (`,`) mà dùng dấu chấm phẩy (`;`), dấu tab (`\t`), hoặc ký tự khác, bạn có thể chỉ định bằng tham số `delimiter`:
    ```python
    # Ví dụ cho file dùng dấu chấm phẩy
    csv_reader = csv.reader(file, delimiter=';')
    csv_dict_reader = csv.DictReader(file, delimiter=';')
    ```
* **Ký tự bao quanh (Quote Character):** Nếu các giá trị chứa dấu phân cách được bao quanh bởi dấu nháy kép (`"`) hoặc nháy đơn (`'`), `csv` thường tự động xử lý đúng. Bạn cũng có thể chỉ định nếu cần với `quotechar`.

**Lưu ý quan trọng:**

1.  **`with open(...)`:** Luôn sử dụng cấu trúc `with open(...)` để đảm bảo file được đóng tự động ngay cả khi có lỗi xảy ra.
2.  **`newline=''`:** Tham số này rất quan trọng khi mở file CSV. Nó ngăn Python tự động chuyển đổi các ký tự kết thúc dòng, giúp thư viện `csv` xử lý các dòng một cách chính xác trên các hệ điều hành khác nhau.
3.  **`encoding='utf-8'`:** UTF-8 là một bảng mã phổ biến, hỗ trợ nhiều loại ký tự (bao gồm tiếng Việt). Nếu bạn biết chắc file CSV của mình dùng bảng mã khác (như 'cp1252', 'latin1'), hãy thay đổi cho phù hợp.
4.  **Dữ liệu là chuỗi:** Cả `csv.reader` và `csv.DictReader` đều đọc tất cả dữ liệu dưới dạng chuỗi (string). Nếu bạn cần làm việc với số liệu (int, float), bạn phải tự chuyển đổi chúng sau khi đọc (ví dụ: `int(dong[0])` hoặc `float(dong_dict['Gia'])`).
5.  **Xử lý lỗi:** Sử dụng `try...except` để bắt các lỗi thường gặp như `FileNotFoundError` khi file không tồn tại hoặc các lỗi khác trong quá trình đọc file.


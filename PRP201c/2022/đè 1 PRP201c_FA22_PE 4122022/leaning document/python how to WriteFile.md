CChúng ta đã nói về cách đọc file. Giờ đến **cách ghi (write)** nội dung vào file trong Python. Tương tự như đọc, bạn cũng dùng hàm `open()` nhưng với các chế độ (mode) khác nhau.

**1. Các chế độ ghi (Writing Modes) trong `open()`:**

* **`'w'` (Write - Ghi đè):**
    * Mở file để ghi.
    * Nếu file **chưa tồn tại**, nó sẽ được **tạo mới**.
    * Nếu file **đã tồn tại**, toàn bộ nội dung cũ của file sẽ bị **xóa sạch** trước khi ghi nội dung mới. Hãy cẩn thận khi dùng chế độ này!
* **`'a'` (Append - Ghi nối tiếp):**
    * Mở file để ghi.
    * Nếu file **chưa tồn tại**, nó sẽ được **tạo mới**.
    * Nếu file **đã tồn tại**, con trỏ sẽ được đặt ở **cuối file**, và nội dung mới bạn ghi vào sẽ được **thêm vào sau** nội dung cũ, không làm mất dữ liệu cũ.
* **`'x'` (Exclusive Creation - Tạo độc quyền):**
    * Chỉ để **tạo một file mới** và mở để ghi.
    * Nếu file **đã tồn tại**, thao tác `open()` sẽ thất bại và gây ra lỗi `FileExistsError`. Chế độ này hữu ích khi bạn muốn chắc chắn rằng mình không vô tình ghi đè lên một file đã có.

*Lưu ý:* Bạn cũng có thể thêm `+` vào các chế độ (ví dụ `w+`, `a+`) để cho phép cả đọc và ghi, nhưng với mục đích chỉ ghi đơn thuần thì `'w'` hoặc `'a'` là đủ.

**2. Sử dụng `with open(...)` (Cách khuyến nghị)**

Tương tự như khi đọc, dùng `with` để quản lý việc mở và **tự động đóng file** là cách tốt nhất.

**3. Các phương thức ghi (Writing Methods):**

Sau khi mở file bằng `with open(...)` ở chế độ ghi (`'w'` hoặc `'a'`), bạn dùng các phương thức sau:

* **`file_object.write(string)`:**
    * Ghi một **chuỗi (string)** duy nhất vào file tại vị trí con trỏ hiện tại.
    * Phương thức này **không tự động thêm ký tự xuống dòng (`\n`)**. Nếu bạn muốn mỗi lần ghi là một dòng mới, bạn phải tự thêm `\n` vào cuối chuỗi.
    * Trả về số lượng ký tự đã được ghi.

* **`file_object.writelines(list_of_strings)`:**
    * Ghi một **danh sách (hoặc một đối tượng iterable khác) các chuỗi** vào file.
    * Nó sẽ ghi lần lượt từng chuỗi trong danh sách.
    * Giống như `write()`, phương thức này cũng **không tự động thêm ký tự xuống dòng (`\n`)** giữa các chuỗi. Bạn cần đảm bảo các chuỗi trong danh sách đã chứa sẵn `\n` nếu muốn chúng nằm trên các dòng riêng biệt.

**Ví dụ:**

```python
file_ghi = "output.txt"
dong1 = "Đây là dòng đầu tiên.\n" # Có \n để xuống dòng
dong2 = "Đây là dòng thứ hai."    # Không có \n

danh_sach_dong = ["Dòng A\n", "Dòng B\n", "Dòng C"]

# --- Ví dụ với chế độ 'w' (Ghi đè) ---
try:
    with open(file_ghi, 'w', encoding='utf-8') as f: # Dùng encoding='utf-8' cho tiếng Việt
        f.write(dong1)
        f.write(dong2)
        f.write("\nThêm một dòng nữa.\n") # Tự thêm \n khi cần

        # Ghi nhiều dòng từ list
        f.writelines(danh_sach_dong) # Ghi Dòng A\n, Dòng B\n, Dòng C liền nhau

    print(f"Đã ghi đè nội dung vào file '{file_ghi}' (chế độ 'w').")

    # Kiểm tra nội dung file output.txt bây giờ sẽ là:
    # Đây là dòng đầu tiên.
    # Đây là dòng thứ hai.
    # Thêm một dòng nữa.
    # Dòng A
    # Dòng B
    # Dòng C

except Exception as e:
    print(f"Lỗi khi ghi file (chế độ 'w'): {e}")


# --- Ví dụ với chế độ 'a' (Ghi nối tiếp) ---
try:
    with open(file_ghi, 'a', encoding='utf-8') as f: # Mở lại file ở chế độ append
        f.write("\n--- Phần ghi nối tiếp ---\n")
        f.write("Thêm dòng này vào cuối file.\n")

    print(f"Đã ghi nối tiếp vào file '{file_ghi}' (chế độ 'a').")

    # Kiểm tra nội dung file output.txt bây giờ sẽ có thêm phần mới ở cuối

except Exception as e:
    print(f"Lỗi khi ghi file (chế độ 'a'): {e}")
```

**Quan trọng:**

* Luôn dùng `encoding='utf-8'` khi làm việc với file văn bản có chứa tiếng Việt hoặc các ký tự đặc biệt khác để tránh lỗi mã hóa.
* Nhớ tự thêm ký tự xuống dòng `\n` khi sử dụng `write()` hoặc chuẩn bị các chuỗi trong `writelines()` nếu bạn muốn dữ liệu được ghi thành các dòng riêng biệt.
* Hãy cẩn thận với chế độ `'w'` vì nó sẽ xóa toàn bộ nội dung cũ của file.
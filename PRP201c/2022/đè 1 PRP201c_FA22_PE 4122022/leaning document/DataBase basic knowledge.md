Chào bạn, dưới đây là phần trình bày về cơ sở dữ liệu cơ bản, các câu lệnh SQL ví dụ và cách kết hợp với Python.

### I. Cơ Sở Dữ Liệu (Database - DB) là gì?

1.  **Khái niệm:**
    * Cơ sở dữ liệu (CSDL) là một tập hợp dữ liệu được tổ chức, lưu trữ và quản lý một cách có hệ thống trên máy tính.
    * Mục đích chính là để dễ dàng truy cập, quản lý và cập nhật dữ liệu.
    * Hãy tưởng tượng nó như một tủ hồ sơ điện tử siêu thông minh, nơi bạn có thể lưu trữ thông tin một cách ngăn nắp và tìm kiếm nhanh chóng.

2.  **Tại sao cần CSDL?**
    * **Lưu trữ hiệu quả:** Lưu trữ lượng lớn dữ liệu một cách có cấu trúc.
    * **Truy xuất nhanh chóng:** Tìm kiếm và lấy dữ liệu dễ dàng thông qua các truy vấn.
    * **Quản lý tập trung:** Dữ liệu được quản lý tại một nơi, dễ dàng bảo trì và cập nhật.
    * **An toàn và bảo mật:** Cung cấp các cơ chế kiểm soát truy cập và bảo vệ dữ liệu.
    * **Toàn vẹn dữ liệu:** Đảm bảo dữ liệu chính xác và nhất quán thông qua các ràng buộc.
    * **Chia sẻ dữ liệu:** Cho phép nhiều người dùng hoặc ứng dụng truy cập dữ liệu cùng lúc.

3.  **Loại CSDL phổ biến (Cho người mới bắt đầu):**
    * **Cơ sở dữ liệu quan hệ (Relational Database):** Đây là loại phổ biến nhất. Dữ liệu được tổ chức thành các bảng (tables). Mỗi bảng có các hàng (rows - bản ghi) và cột (columns - thuộc tính). Các bảng có thể liên kết với nhau thông qua các khóa (keys). Ví dụ: MySQL, PostgreSQL, SQLite, SQL Server, Oracle.

### II. Ngôn ngữ truy vấn có cấu trúc (SQL - Structured Query Language)

* SQL là ngôn ngữ tiêu chuẩn được sử dụng để giao tiếp với các CSDL quan hệ.
* Nó cho phép bạn thực hiện các thao tác chính như:
    * Định nghĩa cấu trúc dữ liệu (tạo bảng, sửa bảng...).
    * Truy vấn dữ liệu (lấy thông tin).
    * Chèn, cập nhật, xóa dữ liệu.
    * Quản lý quyền truy cập.

### III. Các câu lệnh SQL cơ bản (CRUD Operations)

Giả sử chúng ta có một bảng tên là `Students` (Sinh viên) với các cột: `id` (mã sinh viên - khóa chính), `name` (tên), `age` (tuổi), `major` (ngành học).

1.  **CREATE (Tạo):**
    * **Tạo Cơ sở dữ liệu:**
        ```sql
        CREATE DATABASE school_management;
        ```
    * **Tạo Bảng:** (Sau khi đã chọn CSDL `school_management` để làm việc)
        ```sql
        CREATE TABLE Students (
            id INT PRIMARY KEY AUTO_INCREMENT, -- Mã SV, tự động tăng
            name VARCHAR(100) NOT NULL,       -- Tên, không được để trống
            age INT,
            major VARCHAR(50)
        );
        ```
        * `INT`: Kiểu số nguyên.
        * `VARCHAR(n)`: Kiểu chuỗi ký tự có độ dài tối đa n.
        * `PRIMARY KEY`: Khóa chính, định danh duy nhất cho mỗi hàng.
        * `AUTO_INCREMENT`: Tự động tăng giá trị (thường dùng cho ID).
        * `NOT NULL`: Cột này không được phép có giá trị rỗng (NULL).

2.  **READ (Đọc / Truy vấn):** Dùng lệnh `SELECT`
    * **Lấy tất cả thông tin từ bảng:**
        ```sql
        SELECT * FROM Students;
        ```
    * **Lấy một số cột cụ thể:**
        ```sql
        SELECT name, major FROM Students;
        ```
    * **Lấy dữ liệu với điều kiện:** (Lấy sinh viên có tuổi lớn hơn 20)
        ```sql
        SELECT * FROM Students WHERE age > 20;
        ```
    * **Lấy dữ liệu và sắp xếp:** (Lấy sinh viên và sắp xếp theo tên A-Z)
        ```sql
        SELECT * FROM Students ORDER BY name ASC; -- ASC: tăng dần (mặc định), DESC: giảm dần
        ```
    * **Lấy dữ liệu với nhiều điều kiện:** (Lấy sinh viên ngành 'IT' và tuổi <= 22)
        ```sql
        SELECT name, age FROM Students WHERE major = 'IT' AND age <= 22;
        ```

3.  **UPDATE (Cập nhật):** Dùng lệnh `UPDATE`
    * **Cập nhật thông tin của một sinh viên cụ thể:** (Cập nhật ngành học cho sinh viên có id = 5)
        ```sql
        UPDATE Students
        SET major = 'Computer Science'
        WHERE id = 5;
        -- Lưu ý: Luôn dùng mệnh đề WHERE khi UPDATE để tránh cập nhật toàn bộ bảng!
        ```
    * **Cập nhật nhiều cột:**
        ```sql
        UPDATE Students
        SET age = 21, major = 'Data Science'
        WHERE id = 10;
        ```

4.  **DELETE (Xóa):** Dùng lệnh `DELETE`
    * **Xóa một sinh viên cụ thể:** (Xóa sinh viên có id = 3)
        ```sql
        DELETE FROM Students
        WHERE id = 3;
        -- Lưu ý: Luôn dùng mệnh đề WHERE khi DELETE để tránh xóa toàn bộ bảng!
        ```
    * **Xóa tất cả sinh viên thuộc một ngành:**
        ```sql
        DELETE FROM Students
        WHERE major = 'Economics';
        ```

5.  **INSERT (Chèn):** Dùng lệnh `INSERT INTO` để thêm dữ liệu mới
    * **Thêm một sinh viên mới:**
        ```sql
        INSERT INTO Students (name, age, major)
        VALUES ('Nguyen Van A', 21, 'IT');
        ```
    * **Thêm nhiều sinh viên cùng lúc (cú pháp có thể khác nhau tùy hệ CSDL):**
        ```sql
        INSERT INTO Students (name, age, major) VALUES
        ('Tran Thi B', 20, 'Marketing'),
        ('Le Van C', 22, 'IT');
        ```

### IV. Kết hợp Cơ sở dữ liệu với Python

Python có thể dễ dàng tương tác với hầu hết các loại CSDL thông qua các thư viện gọi là **database connectors** (hoặc drivers).

1.  **Tại sao dùng Python với CSDL?**
    * Tự động hóa các tác vụ liên quan đến dữ liệu.
    * Xây dựng ứng dụng web (với các framework như Django, Flask) cần lưu trữ và truy xuất dữ liệu.
    * Phân tích dữ liệu (kết hợp với Pandas, NumPy).
    * Tạo các kịch bản (scripts) để quản lý, sao lưu, hoặc di chuyển dữ liệu.

2.  **Các thư viện phổ biến:**
    * **`sqlite3`:** Có sẵn trong Python, dùng cho CSDL SQLite (CSDL dựa trên file, rất tiện lợi cho ứng dụng nhỏ hoặc học tập).
    * **`mysql-connector-python`:** Kết nối với MySQL. Cần cài đặt: `pip install mysql-connector-python`
    * **`psycopg2`:** Kết nối với PostgreSQL. Cần cài đặt: `pip install psycopg2-binary` (hoặc `psycopg2`)
    * **`pyodbc`:** Kết nối qua ODBC (có thể dùng cho SQL Server, Access...). Cần cài đặt: `pip install pyodbc`
    * **SQLAlchemy:** Một ORM (Object-Relational Mapper) mạnh mẽ, cung cấp cách tiếp cận hướng đối tượng để làm việc với CSDL, trừu tượng hóa nhiều câu lệnh SQL. Phù hợp cho các dự án lớn. Cần cài đặt: `pip install SQLAlchemy` (và connector tương ứng).

3.  **Quy trình cơ bản khi làm việc với CSDL trong Python:**

    * **Import thư viện:** `import sqlite3` (hoặc thư viện khác).
    * **Kết nối (Connect):** Tạo một đối tượng kết nối đến CSDL. Cần cung cấp thông tin như tên CSDL, host, user, password (tùy loại CSDL).
    * **Tạo Con trỏ (Cursor):** Con trỏ là đối tượng cho phép bạn thực thi các lệnh SQL.
    * **Thực thi (Execute):** Dùng con trỏ để thực thi các câu lệnh SQL (CREATE, INSERT, SELECT, UPDATE, DELETE). **Nên sử dụng tham số hóa (placeholders như `?` hoặc `%s`) để tránh lỗi SQL Injection.**
    * **Lấy kết quả (Fetch):** Nếu là lệnh `SELECT`, dùng các phương thức như `Workspaceone()` (lấy 1 hàng), `Workspaceall()` (lấy tất cả các hàng), `Workspacemany(n)` (lấy n hàng).
    * **Lưu thay đổi (Commit):** Đối với các lệnh làm thay đổi dữ liệu (INSERT, UPDATE, DELETE), cần gọi `connection.commit()` để lưu các thay đổi vào CSDL.
    * **Đóng kết nối (Close):** Luôn đóng con trỏ và kết nối sau khi sử dụng xong để giải phóng tài nguyên (`cursor.close()`, `connection.close()`). Sử dụng `try...finally` hoặc `with` statement là cách tốt nhất để đảm bảo kết nối luôn được đóng.

4.  **Ví dụ với `sqlite3` (Đơn giản nhất):**

```python
import sqlite3
import os

# Tên file CSDL
db_file = 'my_school.db'

# Xóa file db cũ nếu tồn tại (chỉ để chạy ví dụ này nhiều lần)
if os.path.exists(db_file):
    os.remove(db_file)

# Hàm để thực hiện các thao tác
def database_operations():
    conn = None # Khởi tạo biến kết nối
    try:
        # 1. Kết nối (sẽ tạo file nếu chưa có)
        conn = sqlite3.connect(db_file)
        print(f"Đã kết nối tới SQLite DB: {db_file}")

        # 2. Tạo con trỏ
        cursor = conn.cursor()
        print("Đã tạo con trỏ")

        # 3. Thực thi: Tạo bảng Students (nếu chưa tồn tại)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            id INTEGER PRIMARY KEY AUTOINCREMENT, -- SQLite dùng INTEGER PRIMARY KEY AUTOINCREMENT
            name TEXT NOT NULL,
            age INTEGER,
            major TEXT
        )
        ''')
        print("Đã tạo bảng Students (hoặc bảng đã tồn tại)")

        # 4. Thực thi: Chèn dữ liệu (dùng placeholder ? để an toàn)
        students_to_insert = [
            ('Nguyen Van A', 21, 'IT'),
            ('Tran Thi B', 20, 'Marketing'),
            ('Le Van C', 22, 'IT')
        ]
        cursor.executemany('INSERT INTO Students (name, age, major) VALUES (?, ?, ?)', students_to_insert)
        print(f"Đã chèn {len(students_to_insert)} sinh viên.")

        # 5. Lưu thay đổi vào CSDL
        conn.commit()
        print("Đã commit các thay đổi.")

        # 6. Thực thi: Truy vấn dữ liệu
        print("\n--- Lấy tất cả sinh viên: ---")
        cursor.execute('SELECT * FROM Students')
        all_students = cursor.fetchall() # Lấy tất cả kết quả
        for student in all_students:
            print(student) # Mỗi student là một tuple (id, name, age, major)

        print("\n--- Lấy sinh viên ngành IT: ---")
        cursor.execute('SELECT name, age FROM Students WHERE major = ?', ('IT',)) # Truyền tham số là tuple
        it_students = cursor.fetchall()
        for student in it_students:
            print(f"Tên: {student[0]}, Tuổi: {student[1]}")

        # 7. Thực thi: Cập nhật dữ liệu
        student_id_to_update = 1
        new_major = 'Software Engineering'
        cursor.execute('UPDATE Students SET major = ? WHERE id = ?', (new_major, student_id_to_update))
        conn.commit() # Commit sau khi cập nhật
        print(f"\nĐã cập nhật ngành cho sinh viên có ID {student_id_to_update} thành '{new_major}'.")

        # Kiểm tra lại sau khi cập nhật
        cursor.execute('SELECT * FROM Students WHERE id = ?', (student_id_to_update,))
        updated_student = cursor.fetchone() # Lấy một hàng
        print(f"Thông tin sau cập nhật: {updated_student}")

        # 8. Thực thi: Xóa dữ liệu
        student_id_to_delete = 2
        cursor.execute('DELETE FROM Students WHERE id = ?', (student_id_to_delete,))
        conn.commit() # Commit sau khi xóa
        print(f"\nĐã xóa sinh viên có ID {student_id_to_delete}.")

        # Kiểm tra lại toàn bộ bảng
        print("\n--- Danh sách sinh viên cuối cùng: ---")
        cursor.execute('SELECT * FROM Students')
        final_students = cursor.fetchall()
        for student in final_students:
            print(student)

    except sqlite3.Error as e:
        print(f"Lỗi SQLite xảy ra: {e}")
    except Exception as ex:
        print(f"Lỗi khác xảy ra: {ex}")
    finally:
        # 9. Đóng kết nối (luôn thực hiện dù có lỗi hay không)
        if conn:
            conn.close()
            print("\nĐã đóng kết nối CSDL.")

# Chạy hàm thực hiện
database_operations()
```

**Cách chạy ví dụ Python:**
1. Lưu đoạn code trên vào một file ví dụ `database_example.py`.
2. Mở terminal hoặc command prompt.
3. Chạy file bằng lệnh: `python database_example.py`
4. Bạn sẽ thấy các thông báo in ra màn hình và một file `my_school.db` được tạo trong cùng thư mục.


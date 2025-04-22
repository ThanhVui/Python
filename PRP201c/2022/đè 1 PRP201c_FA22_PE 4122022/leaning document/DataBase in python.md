Dưới đây là trình bày chi tiết về kiến thức cơ sở dữ liệu cần thiết và cách tương tác với chúng bằng Python.

**Phần 1: Kiến thức Cơ bản về Cơ sở dữ liệu (Database)**

1.  **Cơ sở dữ liệu (Database - CSDL) là gì?**
    * Là một tập hợp các dữ liệu có cấu trúc, được tổ chức và lưu trữ một cách hệ thống, thường là trên máy tính.
    * Được quản lý bởi một Hệ quản trị Cơ sở dữ liệu (Database Management System - DBMS).
    * Mục đích: Lưu trữ, quản lý, truy xuất và cập nhật dữ liệu một cách hiệu quả, an toàn và đáng tin cậy.

2.  **Các loại Cơ sở dữ liệu phổ biến:**
    * **CSDL Quan hệ (Relational Databases - SQL):**
        * Phổ biến nhất, dữ liệu được tổ chức thành các bảng (tables/relations).
        * Mỗi bảng có các hàng (rows/records) và cột (columns/attributes).
        * Sử dụng Ngôn ngữ Truy vấn Có cấu trúc (Structured Query Language - SQL).
        * **Ví dụ DBMS:** MySQL, PostgreSQL, SQLite, Microsoft SQL Server, Oracle.
        * **Khái niệm chính:** Bảng, Cột, Hàng, Khóa chính (Primary Key - PK), Khóa ngoại (Foreign Key - FK), Lược đồ (Schema), Mối quan hệ (1-1, 1-nhiều, nhiều-nhiều), Chuẩn hóa (Normalization).
    * **CSDL NoSQL (Not Only SQL):**
        * Mô hình dữ liệu linh hoạt hơn, thường có khả năng mở rộng (scalability) tốt hơn cho các trường hợp sử dụng cụ thể.
        * **Document Databases:** Lưu dữ liệu dưới dạng tài liệu (thường là JSON/BSON). *Ví dụ: MongoDB, Couchbase.*
        * **Key-Value Stores:** Lưu dữ liệu dạng cặp khóa-giá trị đơn giản. *Ví dụ: Redis, Memcached.*
        * **Column-Family Stores:** Lưu dữ liệu theo cột thay vì hàng. *Ví dụ: Cassandra, HBase.*
        * **Graph Databases:** Tập trung vào mối quan hệ giữa các điểm dữ liệu (nodes và edges). *Ví dụ: Neo4j, ArangoDB.*

3.  **SQL (Structured Query Language):**
    * Ngôn ngữ tiêu chuẩn để giao tiếp với CSDL quan hệ.
    * **Các lệnh SQL cơ bản (CRUD và hơn thế nữa):**
        * `SELECT`: Truy xuất dữ liệu (`FROM`, `WHERE`, `JOIN`, `GROUP BY`, `HAVING`, `ORDER BY`).
        * `INSERT INTO`: Thêm dữ liệu mới.
        * `UPDATE`: Cập nhật dữ liệu hiện có (`SET`, `WHERE`).
        * `DELETE`: Xóa dữ liệu (`WHERE`).
        * `CREATE TABLE`: Tạo bảng mới.
        * `ALTER TABLE`: Sửa đổi cấu trúc bảng.
        * `DROP TABLE`: Xóa bảng.
        * `CREATE DATABASE`, `DROP DATABASE`: Quản lý CSDL.

4.  **Thao tác CRUD:**
    * Các hoạt động cơ bản trên dữ liệu: **C**reate (Tạo), **R**ead (Đọc), **U**pdate (Cập nhật), **D**elete (Xóa).
    * Ánh xạ trực tiếp tới các lệnh SQL: `INSERT`, `SELECT`, `UPDATE`, `DELETE`.

5.  **Giao dịch (Transactions):**
    * Một chuỗi các thao tác CSDL được xem như một đơn vị công việc logic duy nhất.
    * Đảm bảo tính toàn vẹn dữ liệu thông qua **ACID** (trong CSDL quan hệ):
        * **Atomicity (Nguyên tử):** Hoặc tất cả thao tác thành công, hoặc không thao tác nào thành công (rollback).
        * **Consistency (Nhất quán):** Giao dịch đưa CSDL từ trạng thái hợp lệ này sang trạng thái hợp lệ khác.
        * **Isolation (Cô lập):** Các giao dịch đồng thời không can thiệp lẫn nhau.
        * **Durability (Bền vững):** Một khi giao dịch đã được cam kết (commit), thay đổi là vĩnh viễn.

6.  **Lược đồ CSDL (Database Schema):**
    * Bản thiết kế chi tiết cấu trúc của CSDL: các bảng, cột, kiểu dữ liệu, mối quan hệ, ràng buộc (constraints).

7.  **Chỉ mục (Indexes):**
    * Cấu trúc dữ liệu đặc biệt giúp tăng tốc độ truy vấn dữ liệu (`SELECT`) bằng cách cho phép DBMS tìm kiếm nhanh hơn. Việc này đánh đổi bằng việc ghi (`INSERT`, `UPDATE`, `DELETE`) chậm hơn một chút và tốn thêm dung lượng lưu trữ.

**Phần 2: Tương tác với CSDL trong Python**

Python cung cấp nhiều cách để làm việc với CSDL, tuân theo một chuẩn chung và có các thư viện cho hầu hết các loại DBMS.

1.  **DB-API 2.0 (PEP 249):**
    * Là một đặc tả (specification) chuẩn của Python cho các module truy cập CSDL.
    * Mục đích: Cung cấp một giao diện lập trình **thống nhất** cho dù bạn đang làm việc với SQLite, MySQL, PostgreSQL hay CSDL quan hệ khác.
    * **Các đối tượng/khái niệm chính:**
        * `connect()`: Hàm để thiết lập kết nối tới CSDL. Trả về đối tượng `Connection`.
        * `Connection`: Đại diện cho phiên làm việc với CSDL. Có các phương thức như `cursor()`, `commit()` (lưu thay đổi), `rollback()` (hủy thay đổi), `close()` (đóng kết nối).
        * `Cursor`: Đối tượng dùng để thực thi các lệnh SQL và lấy kết quả trả về. Có các phương thức như `execute()` (thực thi 1 lệnh), `executemany()` (thực thi 1 lệnh với nhiều bộ dữ liệu), `Workspaceone()` (lấy 1 dòng kết quả), `Workspaceall()` (lấy tất cả kết quả), `Workspacemany()` (lấy nhiều dòng).

2.  **Module `sqlite3` (Tích hợp sẵn):**
    * Python có sẵn module `sqlite3` để làm việc với CSDL SQLite (CSDL dạng file, không cần server riêng).
    * Rất tiện lợi cho phát triển, thử nghiệm, ứng dụng nhỏ hoặc nhúng.
    * **Quy trình cơ bản:**
        ```python
        import sqlite3

        db_file = 'my_database.sqlite'

        try:
            # 1. Kết nối (dùng with để tự động đóng)
            with sqlite3.connect(db_file) as conn:
                # 2. Tạo đối tượng Cursor (dùng with để tự động đóng)
                with conn.cursor() as cursor:
                    # 3. Thực thi lệnh SQL (Ví dụ: Tạo bảng)
                    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            email TEXT UNIQUE
                        )
                    """)
                    print("Bảng 'users' đã sẵn sàng.")

                    # 4. Insert dữ liệu (SỬ DỤNG THAM SỐ HÓA '?')
                    user_name = "Alice"
                    user_email = "alice@example.com"
                    try:
                        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (user_name, user_email))
                        print(f"Đã thêm user: {user_name}")
                    except sqlite3.IntegrityError: # Xử lý lỗi nếu email đã tồn tại (do UNIQUE)
                        print(f"Email {user_email} đã tồn tại.")

                    # Thực thi nhiều bản ghi
                    users_to_add = [("Bob", "bob@example.com"), ("Charlie", "charlie@example.com")]
                    cursor.executemany("INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)", users_to_add)
                    print(f"Đã thêm {cursor.rowcount} users từ list.") # rowcount chỉ có ý nghĩa sau executemany

                    # 5. Truy vấn dữ liệu
                    cursor.execute("SELECT id, name, email FROM users WHERE name LIKE ?", ('A%',)) # Tìm user tên bắt đầu bằng 'A'

                    # 6. Lấy kết quả
                    print("\n--- Users bắt đầu bằng 'A' ---")
                    results = cursor.fetchall() # Lấy tất cả
                    if results:
                        for row in results:
                            print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}")
                    else:
                        print("Không tìm thấy user nào.")

                # 7. Commit (tự động khi kết thúc khối 'with conn:')
                # conn.commit() # Không cần thiết khi dùng with conn:

        except sqlite3.Error as e:
            print(f"Lỗi CSDL SQLite: {e}")
        # 8. Close (tự động khi kết thúc khối 'with conn:')
        ```
    * **Quan trọng:** Luôn dùng `?` làm placeholder trong `execute()` và truyền dữ liệu dưới dạng tuple để **tránh lỗi SQL Injection**.

3.  **Làm việc với CSDL Quan hệ khác (MySQL, PostgreSQL,...):**
    * Bạn cần cài đặt thư viện adapter (driver) tương ứng cho CSDL đó.
    * **Ví dụ thư viện:**
        * MySQL: `mysql-connector-python` hoặc `PyMySQL`
        * PostgreSQL: `psycopg2` (phổ biến) hoặc `psycopg` (mới hơn)
        * SQL Server: `pyodbc` (cần ODBC driver của hệ điều hành)
        * Oracle: `cx_Oracle` (cần Oracle Instant Client)
    * **Cài đặt:** Dùng pip, ví dụ: `pip install psycopg2-binary` (cho PostgreSQL).
    * **Kết nối:** Sử dụng hàm `connect()` của thư viện đó, cung cấp các thông tin kết nối cần thiết (host, port, user, password, database name).
        ```python
        # Ví dụ với PostgreSQL (đã cài psycopg2)
        import psycopg2

        try:
            with psycopg2.connect(
                host="your_host",
                database="your_db",
                user="your_user",
                password="your_password",
                port="your_port" # thường là 5432
            ) as conn:
                with conn.cursor() as cursor:
                    # Sử dụng cursor.execute(), fetchall(),... tương tự sqlite3
                    # Lưu ý: Placeholder thường là %s thay vì ?
                    cursor.execute("SELECT version();")
                    db_version = cursor.fetchone()
                    print(f"PostgreSQL version: {db_version[0]}")

                    cursor.execute("SELECT name FROM users WHERE email = %s", ("bob@example.com",)) # Dùng %s
                    # ... xử lý kết quả ...
        except psycopg2.Error as e:
            print(f"Lỗi CSDL PostgreSQL: {e}")
        ```
    * Các thao tác còn lại với `cursor`, `commit`, `rollback`, `close` tuân theo chuẩn DB-API 2.0, tương tự `sqlite3`.

4.  **Object-Relational Mappers (ORMs):**
    * Là các thư viện giúp ánh xạ các bảng/bản ghi trong CSDL thành các lớp/đối tượng trong Python.
    * Cho phép bạn tương tác với CSDL bằng cách gọi phương thức trên các đối tượng Python thay vì viết SQL thuần túy (mặc dù vẫn có thể viết SQL nếu cần).
    * **Ưu điểm:** Code Pythonic hơn, che giấu chi tiết SQL, có thể giúp chuyển đổi giữa các CSDL dễ hơn, quản lý mối quan hệ đối tượng.
    * **Nhược điểm:** Cần thời gian học, có thể tạo ra truy vấn SQL không tối ưu nếu không cẩn thận, thêm một lớp trừu tượng.
    * **Các ORM phổ biến:**
        * **SQLAlchemy:** Rất mạnh mẽ, linh hoạt, được sử dụng rộng rãi. Bao gồm cả Core (cho phép viết SQL bằng biểu thức Python) và ORM.
        * **Django ORM:** Tích hợp sẵn trong web framework Django.
        * **Peewee:** Nhẹ nhàng, đơn giản hơn.
    * **Ví dụ (ý tưởng với SQLAlchemy ORM):**
        ```python
        # (Cần cài đặt SQLAlchemy và cấu hình engine, session)
        # from sqlalchemy import create_engine, Column, Integer, String
        # from sqlalchemy.orm import sessionmaker, declarative_base

        # Base = declarative_base()

        # # Định nghĩa lớp tương ứng bảng users
        # class User(Base):
        #     __tablename__ = 'users'
        #     id = Column(Integer, primary_key=True)
        #     name = Column(String)
        #     email = Column(String, unique=True)

        # # Tạo session
        # Session = sessionmaker(bind=engine) # engine đã được tạo trước đó
        # session = Session()

        # # Thêm user mới
        # new_user = User(name="David", email="david@example.com")
        # session.add(new_user)
        # session.commit()

        # # Truy vấn user
        # alice = session.query(User).filter_by(name="Alice").first()
        # if alice:
        #      print(f"Found user via ORM: {alice.name}, {alice.email}")

        # session.close()
        ```

5.  **Làm việc với CSDL NoSQL:**
    * Mỗi loại CSDL NoSQL có thư viện Python riêng và cách tương tác khác nhau, không tuân theo DB-API 2.0.
    * **Ví dụ thư viện:**
        * MongoDB: `pymongo`
        * Redis: `redis-py`
        * Cassandra: `cassandra-driver`
    * **Ví dụ (ý tưởng với MongoDB):**
        ```python
        # (Cần cài pymongo: pip install pymongo)
        # from pymongo import MongoClient

        # # Kết nối
        # client = MongoClient('mongodb://localhost:27017/') # Địa chỉ MongoDB server

        # # Chọn database
        # db = client['mydatabase']

        # # Chọn collection (tương tự bảng)
        # users_collection = db['users']

        # # Chèn document (tương tự bản ghi)
        # user_doc = {"name": "Eve", "age": 25, "city": "Hanoi"}
        # result = users_collection.insert_one(user_doc)
        # print(f"Inserted document ID: {result.inserted_id}")

        # # Tìm document
        # eve = users_collection.find_one({"name": "Eve"})
        # if eve:
        #     print(f"Found document: {eve}")

        # # Tìm nhiều document
        # for user in users_collection.find({"age": {"$gte": 25}}): # Tìm user có tuổi >= 25
        #      print(user)

        # client.close()
        ```

6.  **Các Thực hành Tốt nhất (Best Practices):**
    * **Dùng `with` statement:** Luôn dùng `with` cho `connection` và `cursor` để đảm bảo chúng được đóng đúng cách.
    * **Tham số hóa Truy vấn:** **TUYỆT ĐỐI KHÔNG** dùng f-string hay định dạng chuỗi `%` để chèn biến vào SQL. Luôn dùng placeholders (`?`, `%s`) để chống SQL Injection.
    * **Connection Pooling:** Đối với ứng dụng web hoặc ứng dụng có nhiều kết nối đồng thời, sử dụng connection pool để quản lý và tái sử dụng kết nối hiệu quả, thay vì tạo/đóng kết nối liên tục. (Các thư viện như SQLAlchemy có hỗ trợ).
    * **Xử lý Lỗi:** Dùng `try...except` để bắt các lỗi liên quan đến CSDL (`sqlite3.Error`, `psycopg2.Error`, `pymysql.Error`,...) và xử lý một cách phù hợp.
    * **Quản lý Giao dịch:** Sử dụng `commit()` và `rollback()` một cách cẩn thận, đặc biệt khi một loạt thao tác cần thành công hoặc thất bại cùng nhau.
    * **Tách biệt Logic:** Giữ logic tương tác CSDL tách biệt khỏi logic nghiệp vụ/giao diện người dùng của ứng dụng.


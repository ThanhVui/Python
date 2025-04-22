import sqlite3
import os

# --- Configuration ---
# Sử dụng raw string (r"...") cho đường dẫn trên Windows
dbFile = r"D:\Ki 5\PRP201c\PRP201c_SP22_Block5_PE 1642022\employee.sqlite"
filePath = r"D:\Ki 5\PRP201c\PRP201c_SP22_Block5_PE 1642022\Data.txt"


def main():
    # Kiểm tra xem file dữ liệu có tồn tại không
    try:
        # Kết nối CSDL, 'with' sẽ tự động quản lý commit/rollback và close
        with sqlite3.connect(dbFile) as sqlObject:
            print(f"Connected to database: {dbFile}")
            cursor = sqlObject.cursor()

            # Tạo bảng nếu chưa tồn tại (đã được đặt trong try...except tổng)
            try:
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS employee (
                        Name TEXT NOT NULL,
                        rate REAL NOT NULL,
                        salary REAL NOT NULL,
                        Total REAL NOT NULL,
                        Tax REAL NOT NULL,
                        -- Lưu ý: Khóa chính phức hợp này khá bất thường
                        PRIMARY KEY (Name, rate, salary, Total, Tax)
                    )
                ''')
            except sqlite3.Error as e:
                print(f"Error creating table: {e}")
                exit(1) # Thoát nếu không tạo được bảng

            # Đọc dữ liệu từ file và xử lý từng dòng
            try:
                with open(filePath, "r") as fileObject:
                    line_number = 0
                    for line in fileObject:
                        line_number += 1
                        # Bỏ qua dòng trống
                        if not line.strip():
                            continue

                        # Tách dữ liệu trên dòng hiện tại
                        data = line.strip().split(",") # Giả sử dùng dấu phẩy

                        # Xử lý và chèn dữ liệu nếu đúng định dạng (3 phần tử)
                        if len(data) == 3:
                            try:
                                name = data[0].strip() # Bỏ khoảng trắng thừa ở tên
                                rate = float(data[1])
                                salary = float(data[2])

                                # Tính toán Total và Tax
                                Total = rate * salary
                                Tax = 0
                                if Total > 9000000:
                                    Tax = Total * 0.05
                                else:
                                    Tax = 0

                                # Chèn dữ liệu vào bảng (nằm trong vòng lặp)
                                # INSERT OR IGNORE sẽ bỏ qua nếu bản ghi đã tồn tại (dựa trên PK phức hợp)
                                cursor.execute('''
                                    INSERT OR IGNORE INTO employee(Name, rate, salary, Total, Tax)
                                    VALUES (?, ?, ?, ?, ?)
                                ''', (name, rate, salary, Total, Tax))
                                # print(f"Processed line {line_number}: {name}") # Bỏ comment nếu muốn xem log chi tiết

                            except ValueError:
                                print(f"Warning: Skipping line {line_number} due to invalid number format: {line.strip()}")
                            except sqlite3.Error as e:
                                print(f"Warning: Error inserting data from line {line_number} ('{line.strip()}'): {e}")
                                # Không cần rollback ở đây vì 'with' sẽ xử lý khi có lỗi không bắt được
                        else:
                            print(f"Warning: Skipping line {line_number} due to incorrect format (expected 3 parts): {line.strip()}")


            except FileNotFoundError:
                print(f"Error: File not found at {filePath}")
                exit(1) # Thoát nếu không tìm thấy file dữ liệu
            except Exception as e:
                print(f"Error reading or processing file {filePath}: {e}")
                exit(1)


            # Truy xuất và in dữ liệu theo yêu cầu
            try:
                cursor.execute('''
                    SELECT Name, rate, salary, Total, Tax
                    FROM employee
                    WHERE rate > 3
                    ORDER BY Name ASC
                ''')
                rows = cursor.fetchall()

                print("\n--- Employee List (rate > 3) ---")
                # In tiêu đề cột
                print(f"{'Name':<15}{'rate':<10}{'salary':<15}{'Total':<20}{'Tax':<15}")
                print("-" * 75) # Dòng kẻ phân cách

                if rows:
                    for row in rows:
                        # Định dạng số để dễ đọc hơn (ví dụ: Total, Tax)
                        print(f"{row[0]:<15}{row[1]:<10.2f}{row[2]:<15,.0f}{row[3]:<20,.2f}{row[4]:<15,.2f}")
                else:
                    print("No employees found with rate > 3.")

            except sqlite3.Error as e:
                print(f"Error retrieving data: {e}")
                exit(1)

    # Xử lý lỗi kết nối CSDL tổng quát
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit(1)




if __name__ == "__main__":
    main()
        
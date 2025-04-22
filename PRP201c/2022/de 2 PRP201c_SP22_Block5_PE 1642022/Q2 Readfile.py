

# **5. Từ điển (`dict`) - Khả biến (Mutable)**

# * **Phương thức:**
#     * `.keys()`: Trả về view chứa các key.
#     * `.values()`: Trả về view chứa các value.
#     * `.items()`: Trả về view chứa các cặp (key, value).
#     * `.get(key, default=None)`: Lấy value của `key`, trả về `default` nếu key không tồn tại (không báo lỗi).
#     * `.pop(key, default)`: Xóa và trả về value của `key` (báo lỗi nếu key không có và không có default).
#     * `.popitem()`: Xóa và trả về cặp (key, value) cuối cùng (trong Python 3.7+).
#     * `.update(other_dict)`: Cập nhật dict với các cặp key-value từ `other_dict`.
#     * `.clear()`: Xóa hết các cặp key-value.
#     * `.copy()`: Tạo bản sao nông.
# * **Hàm tích hợp sẵn:** `len(dict)` (số cặp key-value).
# * **Truy cập/Gán:** `dict[key]`, `dict[key] = value`.
# * **Toán tử:** Dùng `in` để kiểm tra key có tồn tại không (`key in dict`).

def main():
        
    filePath = input("Enter file: ")

    if(filePath == ""):
        filePath = r"Trace.txt"

    nameDictionary = {}
    try :
        with open(filePath, "r") as fileObject: 
            for line in fileObject: 
                if("name" in line) : 
                    nameLine = line.split(r":")[1].strip()
                    nameDictionary[nameLine] = nameDictionary.get(nameLine, 0) +1 
    except FileNotFoundError:
        print("File not found")
        exit(1)

    print("Troubleshoot wired LAN relate issues:")
    for key, value  in nameDictionary.items(): 
        print(f"{key} : {value}")



if __name__ == "__main__":
    main()
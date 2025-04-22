chúng ta hãy cùng tìm hiểu về Lập trình Hướng đối tượng (OOP - Object-Oriented Programming) trong Python, tập trung vào khái niệm `Class` (Lớp) và `Object` (Đối tượng).

### I. Lập trình Hướng đối tượng (OOP) là gì?

OOP là một **mô hình lập trình** (programming paradigm) dựa trên khái niệm "đối tượng" (objects). Thay vì chỉ viết các hàm hoặc thủ tục tuần tự, OOP tổ chức mã nguồn xung quanh dữ liệu (thuộc tính) và các hành vi (phương thức) được đóng gói lại với nhau thành các đơn vị gọi là đối tượng.

**Hãy tưởng tượng:** Khi bạn nhìn thế giới xung quanh, bạn thấy các "đối tượng" như: con người, xe cộ, nhà cửa, cây cối... Mỗi đối tượng này có những **đặc điểm** riêng (ví dụ: người thì có tên, tuổi, chiều cao; xe thì có màu sắc, hãng sản xuất, tốc độ tối đa) và có những **hành động** mà chúng có thể thực hiện (ví dụ: người có thể đi, nói, ăn; xe có thể chạy, dừng, bấm còi).

OOP cố gắng mô hình hóa cách tư duy này vào trong lập trình.

**Lợi ích chính của OOP:**

* **Tính module (Modularity):** Mã nguồn được chia thành các đối tượng độc lập, dễ quản lý và sửa lỗi.
* **Tái sử dụng mã (Code Reusability):** Thông qua kế thừa, bạn có thể tạo lớp mới dựa trên lớp đã có, tiết kiệm thời gian viết mã.
* **Dễ bảo trì (Maintainability):** Thay đổi trong một đối tượng ít ảnh hưởng đến các phần khác của chương trình.
* **Khả năng mở rộng (Scalability):** Dễ dàng thêm các tính năng mới bằng cách thêm lớp mới hoặc mở rộng lớp hiện có.
* **Mô hình hóa thế giới thực:** Giúp việc thiết kế và hiểu các hệ thống phức tạp trở nên trực quan hơn.

### II. Class (Lớp) - Khuôn mẫu

1.  **Khái niệm:**
    * `Class` là một **bản thiết kế (blueprint)**, một **khuôn mẫu (template)** hoặc một **định nghĩa** cho việc tạo ra các đối tượng.
    * Nó định nghĩa các **thuộc tính (attributes)** chung (dữ liệu, đặc điểm) và các **phương thức (methods)** chung (hành vi, hành động) mà tất cả các đối tượng được tạo ra từ lớp đó sẽ có.
    * Bản thân `Class` không phải là một đối tượng cụ thể, nó chỉ là *khái niệm* về loại đối tượng đó.

2.  **Ví dụ tương tự:**
    * Bản thiết kế của một ngôi nhà là `Class`. Các ngôi nhà cụ thể được xây dựng từ bản thiết kế đó là `Object`.
    * Khuôn làm bánh trung thu là `Class`. Những chiếc bánh cụ thể được làm ra từ khuôn đó là `Object`.
    * Định nghĩa về "Sinh Viên" (cần có mã số, tên, ngành học; có thể đăng ký môn học, xem điểm) là `Class`. Từng sinh viên cụ thể như "Nguyễn Văn A", "Trần Thị B" là `Object`.

3.  **Cú pháp trong Python:**
    ```python
    class TenLop:
        # Thuộc tính lớp (class attribute) - dùng chung cho mọi đối tượng
        ten_loai = "Đây là một ví dụ về Lớp"

        # Phương thức khởi tạo (constructor) - thường dùng để gán thuộc tính cho đối tượng
        def __init__(self, thuoc_tinh_1, thuoc_tinh_2):
            # Thuộc tính đối tượng (instance attribute) - riêng cho từng đối tượng
            self.thuoc_tinh_1 = thuoc_tinh_1
            self.thuoc_tinh_2 = thuoc_tinh_2
            print(f"Một đối tượng của {TenLop.__name__} đã được tạo!")

        # Phương thức của đối tượng (instance method)
        def phuong_thuc_1(self):
            print(f"Phương thức 1 đang được gọi cho đối tượng có thuộc tính: {self.thuoc_tinh_1}")
            # Các hành động khác...

        def phuong_thuc_2(self, tham_so_khac):
            print(f"Phương thức 2 với tham số: {tham_so_khac}")
            # Các hành động khác...

    # --- Hết phần định nghĩa Class ---
    ```

4.  **Các thành phần chính của Class:**
    * **`class TenLop:`**: Khai báo bắt đầu định nghĩa một lớp tên là `TenLop` (quy ước viết hoa chữ cái đầu).
    * **Thuộc tính (Attributes):**
        * **Thuộc tính lớp (Class Attribute):** Được định nghĩa trực tiếp bên trong lớp nhưng ngoài các phương thức. Giá trị của nó được chia sẻ cho *tất cả* các đối tượng tạo ra từ lớp đó (ví dụ: `ten_loai`).
        * **Thuộc tính đối tượng (Instance Attribute):** Thường được định nghĩa bên trong phương thức `__init__`. Mỗi đối tượng sẽ có bản sao và giá trị riêng cho các thuộc tính này (ví dụ: `self.thuoc_tinh_1`, `self.thuoc_tinh_2`).
    * **Phương thức (Methods):**
        * Là các hàm được định nghĩa bên trong lớp. Chúng mô tả các hành động mà đối tượng có thể thực hiện.
        * **`self`**: Tham số **đầu tiên** của hầu hết các phương thức trong lớp (đặc biệt là các phương thức của đối tượng). Nó đại diện cho chính **đối tượng cụ thể** đang gọi phương thức đó. Bạn cần dùng `self` để truy cập các thuộc tính và phương thức khác của chính đối tượng đó (ví dụ: `self.thuoc_tinh_1`, `self.phuong_thuc_2(...)`). Tên `self` là quy ước, bạn có thể dùng tên khác nhưng nên tuân theo quy ước này.
        * **`__init__(self, ...)` (Constructor/Initializer):** Đây là một phương thức *đặc biệt*. Nó được Python tự động gọi khi bạn tạo một đối tượng mới từ lớp. Nhiệm vụ chính của nó là *khởi tạo* các thuộc tính ban đầu cho đối tượng.

### III. Object (Đối tượng) - Thể hiện cụ thể

1.  **Khái niệm:**
    * `Object` là một **thể hiện (instance)** cụ thể của một `Class`.
    * Nó được tạo ra từ "khuôn mẫu" là `Class` và có các thuộc tính, phương thức đã được định nghĩa trong `Class` đó.
    * Mỗi `Object` có thể có các giá trị thuộc tính riêng biệt.

2.  **Ví dụ tương tự:**
    * Nếu `Class` là "XeHoi", thì một chiếc "Toyota Vios màu đỏ" và một chiếc "Honda Civic màu đen" là hai `Object` khác nhau của cùng một `Class`.
    * Nếu `Class` là "TaiKhoanNganHang", thì tài khoản của bạn và tài khoản của người khác là các `Object` riêng biệt, mỗi cái có số dư, lịch sử giao dịch khác nhau.

3.  **Tạo đối tượng (Instantiation) trong Python:**
    * Để tạo một đối tượng từ một lớp, bạn gọi tên lớp đó như gọi một hàm, và truyền các tham số cần thiết cho phương thức `__init__` (nếu có, trừ `self`).
    ```python
    # Tạo đối tượng thứ nhất từ lớp TenLop
    doi_tuong_1 = TenLop("Giá trị 1A", "Giá trị 2A")

    # Tạo đối tượng thứ hai từ lớp TenLop
    doi_tuong_2 = TenLop("Giá trị 1B", "Giá trị 2B")
    ```
    * Khi dòng `doi_tuong_1 = TenLop(...)` được thực thi:
        1.  Python tạo ra một đối tượng mới thuộc lớp `TenLop`.
        2.  Phương thức `__init__` của lớp `TenLop` được tự động gọi. Đối tượng mới tạo sẽ được truyền vào làm tham số `self`, còn các giá trị `"Giá trị 1A"`, `"Giá trị 2A"` sẽ được truyền lần lượt vào `thuoc_tinh_1`, `thuoc_tinh_2`.
        3.  Bên trong `__init__`, các thuộc tính của đối tượng được gán giá trị.
        4.  Đối tượng đã được khởi tạo xong và được gán cho biến `doi_tuong_1`.

4.  **Sử dụng đối tượng:**
    * **Truy cập thuộc tính:** Dùng dấu chấm (`.`) sau tên đối tượng.
        ```python
        print(doi_tuong_1.thuoc_tinh_1)  # Output: Giá trị 1A
        print(doi_tuong_2.thuoc_tinh_1)  # Output: Giá trị 1B

        # Truy cập thuộc tính lớp (có thể truy cập qua tên lớp hoặc đối tượng)
        print(TenLop.ten_loai)
        print(doi_tuong_1.ten_loai)
        ```
    * **Gọi phương thức:** Dùng dấu chấm (`.`) sau tên đối tượng và thêm cặp ngoặc `()`. Truyền các tham số cần thiết (nếu có, trừ `self`).
        ```python
        doi_tuong_1.phuong_thuc_1()
        # Output: Phương thức 1 đang được gọi cho đối tượng có thuộc tính: Giá trị 1A

        doi_tuong_2.phuong_thuc_2("Tham số XYZ")
        # Output: Phương thức 2 với tham số: Tham số XYZ
        ```

### IV. Ví dụ tổng hợp: Lớp `XeHoi`

```python
import time # Dùng để mô phỏng thời gian khởi động

class XeHoi:
    # Thuộc tính lớp
    so_banh = 4 # Hầu hết xe hơi đều có 4 bánh

    # Phương thức khởi tạo
    def __init__(self, hang_san_xuat, model, mau_sac, nam_san_xuat):
        # Thuộc tính đối tượng
        self.hang_sx = hang_san_xuat
        self.model = model
        self.mau_sac = mau_sac
        self.nam_sx = nam_san_xuat
        self.dang_chay = False # Trạng thái ban đầu là chưa chạy
        self.van_toc = 0 # Vận tốc ban đầu

    # Phương thức của đối tượng
    def khoi_dong(self):
        if not self.dang_chay:
            print(f"[{self.model}] Đang khởi động động cơ...")
            time.sleep(1) # Giả lập thời gian khởi động
            self.dang_chay = True
            print(f"[{self.model}] Động cơ đã khởi động.")
        else:
            print(f"[{self.model}] Xe đã chạy rồi!")

    def dung_may(self):
        if self.dang_chay:
            if self.van_toc == 0:
                print(f"[{self.model}] Đang tắt máy...")
                self.dang_chay = False
                print(f"[{self.model}] Đã tắt máy.")
            else:
                print(f"[{self.model}] Cần giảm tốc độ về 0 trước khi tắt máy!")
        else:
            print(f"[{self.model}] Xe đang không chạy.")

    def tang_toc(self, gia_toc):
        if self.dang_chay:
            self.van_toc += gia_toc
            print(f"[{self.model}] Tăng tốc. Vận tốc hiện tại: {self.van_toc} km/h")
        else:
            print(f"[{self.model}] Cần khởi động xe trước!")

    def giam_toc(self, giam_toc):
         if self.dang_chay:
            self.van_toc -= giam_toc
            if self.van_toc < 0:
                self.van_toc = 0
            print(f"[{self.model}] Giảm tốc. Vận tốc hiện tại: {self.van_toc} km/h")
            if self.van_toc == 0:
                 print(f"[{self.model}] Xe đã dừng hẳn.")
         else:
            print(f"[{self.model}] Xe không chạy, không thể giảm tốc.")

    def hien_thi_thong_tin(self):
        trang_thai = "Đang chạy" if self.dang_chay else "Đang tắt máy"
        print(f"\n--- Thông tin xe ---")
        print(f"Hãng: {self.hang_sx}")
        print(f"Model: {self.model}")
        print(f"Màu sắc: {self.mau_sac}")
        print(f"Năm sản xuất: {self.nam_sx}")
        print(f"Số bánh: {self.so_banh}") # Truy cập thuộc tính lớp
        print(f"Trạng thái: {trang_thai}")
        print(f"Vận tốc: {self.van_toc} km/h")
        print("--------------------\n")

# --- Tạo và sử dụng đối tượng ---

# Tạo đối tượng xe_1 từ lớp XeHoi
xe_1 = XeHoi("Toyota", "Vios", "Đỏ", 2023)

# Tạo đối tượng xe_2
xe_2 = XeHoi("Honda", "Civic", "Đen", 2024)

# Sử dụng các đối tượng
xe_1.hien_thi_thong_tin()
xe_2.hien_thi_thong_tin()

xe_1.khoi_dong()
xe_1.tang_toc(50)
xe_1.giam_toc(20)
xe_1.hien_thi_thong_tin()

xe_2.khoi_dong()
xe_2.tang_toc(70)
xe_2.hien_thi_thong_tin()

xe_1.dung_may() # Sẽ báo lỗi vì xe đang chạy
xe_1.giam_toc(30) # Giảm về 0
xe_1.dung_may() # Tắt máy thành công
xe_1.hien_thi_thong_tin()

print(f"Xe 1 có {xe_1.so_banh} bánh.")
print(f"Loại xe nói chung có {XeHoi.so_banh} bánh.")
```





Khác với các ngôn ngữ như Java, C# hay C++, Python **không có các từ khóa `public`, `private`, `protected`** để kiểm soát chặt chẽ mức độ truy cập vào thuộc tính và phương thức của một lớp từ bên ngoài.

Thay vào đó, Python sử dụng các **quy ước đặt tên (naming conventions)** và một cơ chế gọi là **name mangling (xáo trộn tên)** để *gợi ý* hoặc *hạn chế một phần* việc truy cập. Triết lý của Python là "We are all consenting adults here" - tạm dịch là "Chúng ta đều là người lớn và tự chịu trách nhiệm", tin tưởng lập trình viên sẽ không cố ý truy cập những phần không nên truy cập.

Dưới đây là các quy ước và cơ chế trong Python tương ứng với các khái niệm modifier:

### 1. Public (Công khai)

* **Cách thể hiện:** Không có dấu gạch dưới nào ở đầu tên.
    ```python
    class LopCongKhai:
        def __init__(self, gia_tri):
            self.thuoc_tinh_cong_khai = gia_tri # Public attribute

        def phuong_thuc_cong_khai(self): # Public method
            print(f"Đây là phương thức public với giá trị: {self.thuoc_tinh_cong_khai}")
    ```
* **Ý nghĩa:** Đây là mặc định. Mọi thuộc tính và phương thức không bắt đầu bằng dấu gạch dưới đều được coi là public. Chúng có thể được truy cập và sửa đổi tự do từ bất kỳ đâu (bên trong lớp, lớp con, hoặc từ bên ngoài đối tượng).
    ```python
    obj = LopCongKhai("Dữ liệu public")
    print(obj.thuoc_tinh_cong_khai)    # Truy cập OK
    obj.thuoc_tinh_cong_khai = "Đã thay đổi" # Sửa đổi OK
    print(obj.thuoc_tinh_cong_khai)
    obj.phuong_thuc_cong_khai()        # Gọi OK
    ```

### 2. "Protected" (Được bảo vệ) - Quy ước một dấu gạch dưới (`_`)

* **Cách thể hiện:** Tên bắt đầu bằng **một dấu gạch dưới** (`_`).
    ```python
    class LopCoProtected:
        def __init__(self, gia_tri):
            self._thuoc_tinh_protected = gia_tri # "Protected" attribute convention

        def _phuong_thuc_protected(self): # "Protected" method convention
            print(f"Đây là phương thức protected với giá trị: {self._thuoc_tinh_protected}")

        def phuong_thuc_public_goi_protected(self):
             print("Gọi phương thức protected từ bên trong lớp:")
             self._phuong_thuc_protected()
    ```
* **Ý nghĩa:** Đây **chỉ là một quy ước**, không có sự ràng buộc nào từ Python. Nó báo hiệu cho các lập trình viên khác rằng thuộc tính/phương thức này được dự định chỉ sử dụng **nội bộ** bên trong lớp hoặc các lớp con kế thừa nó. Bạn *không nên* truy cập trực tiếp từ bên ngoài đối tượng, mặc dù về mặt kỹ thuật Python *vẫn cho phép* bạn làm vậy.
    ```python
    obj_p = LopCoProtected("Dữ liệu protected")

    # VẪN CÓ THỂ truy cập từ bên ngoài (nhưng không nên làm vậy theo quy ước)
    print(obj_p._thuoc_tinh_protected)
    obj_p._thuoc_tinh_protected = "Thay đổi protected từ bên ngoài" # Vẫn sửa được
    print(obj_p._thuoc_tinh_protected)
    obj_p._phuong_thuc_protected() # Vẫn gọi được

    # Cách sử dụng đúng đắn hơn (nếu cần) là thông qua phương thức public
    obj_p.phuong_thuc_public_goi_protected()
    ```

### 3. "Private" (Riêng tư) - Cơ chế Name Mangling với hai dấu gạch dưới (`__`)

* **Cách thể hiện:** Tên bắt đầu bằng **hai dấu gạch dưới** (`__`) nhưng **không** kết thúc bằng hai dấu gạch dưới.
    ```python
    class LopCoPrivate:
        def __init__(self, gia_tri):
            self.__thuoc_tinh_private = gia_tri # "Private" attribute (name mangling)

        def __phuong_thuc_private(self): # "Private" method (name mangling)
            print(f"Đây là phương thức private với giá trị: {self.__thuoc_tinh_private}")

        def phuong_thuc_public_goi_private(self):
             print("Gọi phương thức private từ bên trong lớp:")
             self.__phuong_thuc_private()
    ```
* **Ý nghĩa:** Khi Python thấy một tên bắt đầu bằng `__`, nó sẽ tự động **thay đổi (xáo trộn - mangle)** tên đó thành `_TenLop__tenGoc`. Ví dụ, `__thuoc_tinh_private` trong `LopCoPrivate` sẽ được đổi thành `_LopCoPrivate__thuoc_tinh_private`.
    * Mục đích chính của cơ chế này là để **tránh xung đột tên** (name collision) khi làm việc với kế thừa. Nếu một lớp con cũng định nghĩa một thuộc tính/phương thức có tên `__ten_nao_do`, nó sẽ không vô tình ghi đè lên thuộc tính/phương thức `__ten_nao_do` của lớp cha vì tên đã bị xáo trộn khác nhau (`_LopCon__ten_nao_do` vs `_LopCha__ten_nao_do`).
    * Nó làm cho việc truy cập trực tiếp từ bên ngoài trở nên khó khăn hơn (vì tên gốc không còn tồn tại), nhưng **không phải là private thực sự**. Nếu bạn biết tên đã bị xáo trộn, bạn vẫn có thể truy cập được.
    ```python
    obj_pv = LopCoPrivate("Dữ liệu private")

    # Cố gắng truy cập trực tiếp bằng tên gốc -> SẼ GÂY LỖI AttributeError
    try:
        print(obj_pv.__thuoc_tinh_private)
    except AttributeError as e:
        print(f"Lỗi khi truy cập trực tiếp: {e}")

    try:
        obj_pv.__phuong_thuc_private()
    except AttributeError as e:
        print(f"Lỗi khi gọi trực tiếp: {e}")

    # Cách sử dụng đúng đắn là thông qua phương thức public
    obj_pv.phuong_thuc_public_goi_private()

    # VẪN CÓ THỂ truy cập được nếu biết tên đã bị xáo trộn (không nên làm)
    print("\nTruy cập bằng tên đã bị xáo trộn:")
    mangled_name = "_LopCoPrivate__thuoc_tinh_private"
    print(getattr(obj_pv, mangled_name)) # Hoặc print(obj_pv._LopCoPrivate__thuoc_tinh_private)

    mangled_method_name = "_LopCoPrivate__phuong_thuc_private"
    getattr(obj_pv, mangled_method_name)() # Hoặc obj_pv._LopCoPrivate__phuong_thuc_private()
    ```

### 4. Tóm tắt và Lưu ý

* **Public:** Mặc định, truy cập tự do.
* **Protected (`_`):** Quy ước cho sử dụng nội bộ/lớp con. Python không ngăn cản truy cập từ bên ngoài.
* **Private (`__`):** Kích hoạt Name Mangling (`_ClassName__name`) để tránh xung đột tên, làm khó truy cập trực tiếp từ bên ngoài nhưng không phải là private tuyệt đối.

### 5. Getter và Setter (Properties)

Khi bạn muốn kiểm soát chặt chẽ hơn việc truy cập hoặc sửa đổi một thuộc tính (ví dụ: kiểm tra ràng buộc giá trị, thực hiện hành động phụ khi giá trị thay đổi), cách làm "Pythonic" thường là sử dụng **Properties** kết hợp với thuộc tính "protected" hoặc "private".

```python
class Nguoi:
    def __init__(self, ten, tuoi):
        self.ten = ten # Public
        self._tuoi = 0 # "Protected" để lưu trữ giá trị tuổi thực sự
        self.set_tuoi(tuoi) # Sử dụng setter để gán giá trị ban đầu (có kiểm tra)

    # Getter method (sử dụng decorator @property)
    @property
    def tuoi(self):
        print(f"(Đang lấy giá trị tuổi)")
        return self._tuoi

    # Setter method (sử dụng decorator @ten_property.setter)
    @tuoi.setter
    def tuoi(self, gia_tri_moi):
        print(f"(Đang cập nhật tuổi thành {gia_tri_moi})")
        if isinstance(gia_tri_moi, int) and 0 <= gia_tri_moi <= 150:
            self._tuoi = gia_tri_moi
        else:
            print("Tuổi không hợp lệ! Tuổi phải là số nguyên từ 0 đến 150.")

    # Setter kiểu truyền thống (nếu không dùng property)
    def set_tuoi(self, gia_tri_moi):
        print(f"(Đang cập nhật tuổi thành {gia_tri_moi} - qua set_tuoi)")
        if isinstance(gia_tri_moi, int) and 0 <= gia_tri_moi <= 150:
            self._tuoi = gia_tri_moi
        else:
            print("Tuổi không hợp lệ! Tuổi phải là số nguyên từ 0 đến 150.")


# Sử dụng Property
nguoi1 = Nguoi("Bình", 25)
print(f"Tên: {nguoi1.ten}")

# Truy cập như thuộc tính bình thường, nhưng thực chất gọi getter
print(f"Tuổi: {nguoi1.tuoi}")

# Gán giá trị như thuộc tính bình thường, nhưng thực chất gọi setter
nguoi1.tuoi = 30
print(f"Tuổi mới: {nguoi1.tuoi}")

nguoi1.tuoi = 200 # Sẽ báo lỗi do setter kiểm tra
print(f"Tuổi sau khi cố gắng gán giá trị không hợp lệ: {nguoi1.tuoi}")

# Truy cập thuộc tính _tuoi (vẫn được nhưng không nên theo quy ước)
# print(nguoi1._tuoi)
```

Tóm lại, Python không dùng modifiers cứng nhắc mà dựa vào quy ước (`_`) và name mangling (`__`) để quản lý truy cập, đồng thời cung cấp cơ chế `property` mạnh mẽ để kiểm soát truy cập thuộc tính một cách linh hoạt khi cần thiết.
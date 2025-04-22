
# Q1 
import csv
from datetime import datetime
import re 
import matplotlib.pyplot as plt 
from sqlite3 import Connection

import requests
class Users : 
    def __init__(self, ID, name , email, location, gender , dateOfBirth , registrationDate):
        self.ID = ID 
        self.name = name 
        self.email= email 
        self.location = location 
        self.gender = gender 
        self.dateOfBirth = dateOfBirth 
        self.registrationDate = registrationDate 



def isValidIDNameEmail(ID, name, email): 

    if not ID.isdigit() :
        return False
    
    if not name.strip() : 
        return False 
    if not all(char.isalpha() or char.isspace() for char in name):
        return False
    emailRegex =  r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if not re.match(emailRegex,email): 
        return False
    
    return True 

def toDateTimeObject(dateStr): 
    format = "%Y-%m-%d"
    return datetime.strptime(dateStr,format)


def load_users_data(fileName): 
    usersObjectList = []
    with open(fileName , "r") as fileObject : 
        csvReader = csv.reader(fileObject)
        print(f"Header of csv file : {next(csvReader)}")

        for line in csvReader : 
            if len(line) == 7 and isValidIDNameEmail(line[0],line[1], line[2]): 
                line[5] = toDateTimeObject(line[5])
                line[6] = toDateTimeObject(line[6])
                usersObject =  Users(line[0],line[1], line[2], line[3] ,line[4],line[5],line[6])
                usersObjectList.append(usersObject)
            else :
                print(f"Skipping : {line}")
        
    return usersObjectList

# --- Discussion: Advantages and Disadvantages of using a List ---

# Advantages of using a list to store Users objects:
# 1. Simplicity: Lists are a fundamental Python data structure, easy to understand and use.
# 2. Built-in: No need to import special libraries just for storing the data in memory.
# 3. Ordered: Maintains the order in which userss were added (usually the order from the CSV file).
# 4. Mutable: Easy to add or remove userss from the list after loading.
# 5. Iteration: Simple to loop through all userss (e.g., for processing or display).

# Disadvantages of using a list:
# 1. Search Performance: Finding a specific users by ID or email requires iterating through potentially the entire list (O(n) complexity), which is slow for very large datasets. Dictionaries (using users_id as key) would be much faster (O(1) average complexity) for lookups.
# 2. Memory Usage: For extremely large datasets, storing all Users objects in a list in memory might consume a lot of RAM. Databases or generators might be more memory-efficient alternatives in such cases.
# 3. Data Analysis Features: Lists lack the built-in analytical capabilities of structures like Pandas DataFrames (e.g., easy filtering, grouping, aggregation). You'd have to implement these manually.

# Q2

def visualize_users_data(data):
    """
    Creates visualizations of users data.
    
    Args:
        data (list): List of Users objects
    """
    # Kiểm tra xem có dữ liệu không, nếu không có thì hiển thị thông báo và kết thúc hàm
    if not data:
        print("No data provided for visualization.")
        return

    # Khởi tạo các từ điển để lưu trữ dữ liệu đã xử lý cho việc vẽ biểu đồ
    registrations_by_year = {}  # Lưu số lượng đăng ký theo năm
    gender_by_location = {}     # Lưu phân bố giới tính theo địa điểm
    
    # Duyệt qua từng đối tượng Users trong danh sách data
    for users in data:
        # Lấy năm đăng ký từ thuộc tính RegisteredDate của users
        year = users.registrationDate.year
        
        # Đếm số lượng đăng ký cho mỗi năm, sử dụng get() để trả về 0 nếu năm chưa tồn tại
        registrations_by_year[year] = registrations_by_year.get(year, 0) + 1

        # Lấy thông tin địa điểm và giới tính
        loc = users.location.strip()  # Xóa khoảng trắng thừa
        gender = users.gender.capitalize()  # Viết hoa chữ cái đầu
        
        # Tạo cấu trúc dữ liệu cho địa điểm nếu chưa tồn tại
        if loc not in gender_by_location:
            gender_by_location[loc] = {'Male': 0, 'Female': 0}
        
        # Cập nhật số lượng người theo giới tính cho địa điểm
        gender_by_location[loc][gender] = gender_by_location[loc].get(gender, 0) + 1

    # Tạo một figure với hai subplots (biểu đồ con)
    # figsize: kích thước của toàn bộ figure (chiều rộng, chiều cao) tính bằng inches
    fig, axes = plt.subplots(1, 2, figsize=(18, 7))

    # Subplot 1: Biểu đồ đường thể hiện xu hướng đăng ký theo thời gian
    years = sorted(registrations_by_year.keys())  # Sắp xếp các năm theo thứ tự tăng dần
    counts = [registrations_by_year[y] for y in years]  # Lấy số lượng đăng ký tương ứng với mỗi năm
    
    ax1 = axes[0]  # Lấy trục đầu tiên trong mảng axes
    ax1.plot(years, counts, marker='o')  # Vẽ biểu đồ đường với dấu chấm tròn tại mỗi điểm dữ liệu
    ax1.set_title('Users Registration Trend Over Years')  # Đặt tiêu đề
    ax1.set_xlabel('Year')  # Đặt nhãn trục x
    ax1.set_ylabel('Registrations')  # Đặt nhãn trục y
    ax1.grid(True, linestyle='--', alpha=0.6)  # Thêm lưới với kiểu đường đứt nét và độ mờ 0.6

    # Subplot 2: Biểu đồ cột chồng thể hiện phân bố giới tính theo địa điểm
    locations = sorted(gender_by_location.keys())  # Sắp xếp các địa điểm theo thứ tự bảng chữ cái
    genders = ['Male', 'Female']  # Danh sách các giới tính
    
    # Tạo từ điển lưu số lượng mỗi giới tính cho từng địa điểm
    
#     'Male': [12, 8, 15, ...],  # Số lượng nam ở mỗi địa điểm (New York, London, Tokyo, ...)
#     'Female': [10, 7, 12, ...]  # Số lượng nữ ở mỗi địa điểm (New York, London, Tokyo, ...)

    gender_counts = {g: [gender_by_location[loc].get(g, 0) for loc in locations] for g in genders}
    
    ax2 = axes[1]  # Lấy trục thứ hai trong mảng axes
    bottom = [0] * len(locations)  # Khởi tạo mảng vị trí đáy cho biểu đồ cột chồng
    
    # Tính giá trị lớn nhất của tổng số người dùng tại một địa điểm
    max_userss_per_location = max(
        sum(gender_by_location[loc].get(g, 0) for g in genders)
        for loc in locations
    )
    
    # Đặt giới hạn trục y cao hơn 20% so với giá trị lớn nhất để có không gian hiển thị
    ax2.set_ylim(0, max_userss_per_location * 1.2)
    
    # Vẽ biểu đồ cột chồng cho từng giới tính
    for gender in genders:
        # Thêm một thanh cho mỗi giới tính, với vị trí đáy được xác định bởi biến bottom
        ax2.bar(locations, gender_counts[gender], label=gender, bottom=bottom)
        
        # Cập nhật vị trí đáy mới cho thanh tiếp theo
        bottom = [b + c for b, c in zip(bottom, gender_counts[gender])]
    
    ax2.set_title('Gender Distribution by Location')  # Đặt tiêu đề
    ax2.set_xlabel('Location')  # Đặt nhãn trục x
    ax2.set_ylabel('Userss')  # Đặt nhãn trục y
    ax2.set_xticks(range(len(locations)))  # Đặt vị trí các điểm trên trục x
    ax2.set_xticklabels(locations, rotation=45, ha='right')  # Đặt nhãn cho các điểm trên trục x với góc xoay 45 độ
    ax2.legend(title='Gender')  # Thêm chú thích với tiêu đề "Gender"

    # Điều chỉnh layout để các biểu đồ không bị chồng lấn
    plt.tight_layout()
    
    # Hiển thị biểu đồ
    plt.show()
    
    # In thông báo thành công
    print("Visualizations displayed successfully.\n")
    

# --- Discussion: Challenges of Handling Data Inconsistencies in Visualizations ---

# Handling data inconsistencies is crucial before visualization, otherwise the plots can be misleading or fail to generate. Common challenges include:
# 1. Missing Values (NaN/None):
#    - Challenge: How to represent missing data points? Should they be ignored, imputed (filled with a guessed value like mean, median, mode), or highlighted specifically?
#    - Impact: Ignoring might skew distributions (e.g., if missing data isn't random). Incorrect imputation can introduce bias. Plotting functions might fail if they encounter NaN.
# 2. Incorrect Data Types:
#    - Challenge: Numbers stored as strings, dates as generic strings without a consistent format.
#    - Impact: Prevents numerical calculations (e.g., calculating age from 'DateOfBirth' string), sorting (e.g., chronological order for dates), or correct plotting (e.g., treating '5' as a category instead of a number). Requires explicit conversion and error handling for unparseable values.
# 3. Inconsistent Formatting/Categorization:
#    - Challenge: Variations in text data like 'Male', 'male', 'M' for gender; 'New York', 'NY', 'new york' for location; different date formats ('MM/DD/YYYY', 'YYYY-MM-DD', 'DD Mon YYYY').
#    - Impact: Splits a single category into multiple ones, leading to incorrect counts and fragmented plots (e.g., multiple bars for 'New York' variants). Requires standardization/normalization (e.g., converting all to lowercase, using mapping dictionaries).
# 4. Outliers:
#    - Challenge: Extreme values that differ significantly from others (e.g., an age of 150, a registration date far in the future/past). Could be data entry errors or genuine rare cases.
#    - Impact: Can drastically affect scales of axes, making the main distribution hard to see. Can skew aggregate statistics used in plots (like average registration counts). Requires investigation (are they errors?) and deciding whether to remove, cap, or visualize them separately.
# 5. Conflicting Information:
#    - Challenge: Data that contradicts itself (e.g., registration date before date of birth).
#    - Impact: Indicates deeper data quality issues. Hard to resolve without domain knowledge or additional data sources. Plotting might proceed but represents flawed underlying data.


#Q3 
def createDataBaseFile(dbname): 
    with open(dbname, "w") as file :
        return True
def store_users_data_in_database(data): 
    dbName = "UsersData.db"
    createDataBaseFile(dbName)
    connect = Connection(dbName)
    cursor = connect.cursor()

    # Create Table with ID,Name,Email,Location,Gender,DateOfBirth,RegisteredDate
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                   ID INTEGER PRIMARY KEY , 
                   Name TEXT NOT NULL, 
                   Email TEXT NOT NULL, 
                   Location TEXT NOT NULL, 
                   Gender TEXT NOT NULL, 
                   DateOfBirth TEXT NOT NULL, 
                   RegisteredDate TEXT NOT NULL
                   ) ''')
    # Insert data to db 
    for users in data : 
        cursor.execute('''INSERT OR IGNORE INTO Users (ID, Name, Email, Location, Gender, DateOfBirth, RegisteredDate)  VALUES  (?,?,?,?,?,?,?)  ''',(users.ID, users.name, users.email, users.location, users.gender , users.dateOfBirth.strftime('%Y-%m-%d'), users.registrationDate.strftime('%Y-%m-%d')))
    
    # retrive top 5 location with highest number of register 
    cursor.execute(''' SELECT Users.Location , COUNT(*) as numberOfRegister FROM Users GROUP BY Users.Location ORDER BY numberOfRegister DESC LIMIT 5 ''')

    #display 
    que1 = cursor.fetchall()
    print("========== Top 5 Location with highest register ==========")
    print(f"{'Location':<35}{'Number of Register':<10}")
    for row in que1 : 
        print(f"{row[0]:<35}{row[1]:<10}")
    
    # number of registed users by gender after 2015 
    cursor.execute('''SELECT Gender, COUNT(*) as UsersCount FROM Users  WHERE RegisteredDate >= '2016-01-01' GROUP BY Gender
            ''')
    #display 
    que2 = cursor.fetchall()
    print("========== Number of register of each Gender after 2015 ==========")
    for row in que2 : 
          print(f"{row[0]:<10}{row[1]:<10}")
    cursor.close()
    connect.commit()

# Q4 
def fetch_and_update_users_info():
    apiUrl = 'https://randomuser.me/api/'  # Sửa URL từ 'randomusers.me' thành 'randomuser.me'
    
    # Kết nối database
    dbName = "UsersData.db"
    connect = Connection(dbName)
    cursor = connect.cursor()
    
    # Thêm cột vào bảng - thêm try-except để không gây lỗi nếu cột đã tồn tại

    cursor.execute('''ALTER TABLE Users ADD COLUMN Username TEXT''')  # Sửa UserName thành Username để khớp với query UPDATE
    cursor.execute('''ALTER TABLE Users ADD COLUMN PictureURL TEXT''')
    cursor.execute('''ALTER TABLE Users ADD COLUMN Timezone TEXT''')  # Sửa TimeZone thành Timezone để khớp với query UPDATE
    connect.commit()
    print("Added new columns to the Users table")

    # Lấy ID từ database
    cursor.execute('''SELECT ID FROM Users''')
    que1 = cursor.fetchall()
    ID = [line[0] for line in que1]
    
    if not ID:
        print("No user records found in the database to update.")
        cursor.close()
        connect.close()
        return
    
    # Cập nhật
    update_count = 0
    for id in ID:
     
        response = requests.get(apiUrl)
        if response.status_code == 200:
            data = response.json().get("results", [])[0]  # Lấy phần tử đầu tiên từ mảng kết quả
        else:
            print(f"Failed to fetch data for ID {id}. Status code: {response.status_code}")
            continue     
        
        # Cập nhật database
        UserName = data.get("login", {}).get("username", "")
        PictureUrl = data.get("picture", {}).get("large", "")
        TimeZone = data.get("location", {}).get("timezone", {}).get("description", "")  # Sửa offset thành description
        
       
        cursor.execute('''UPDATE Users SET Username = ?, PictureURL = ?, Timezone = ? WHERE ID = ?''', 
                          (UserName, PictureUrl, TimeZone, id))
        update_count += 1
        
        print(f"Sucessfully update {update_count} user ")
    
    connect.commit()
    connect.close()

# --- Discussion: Challenges of Working with Live APIs and JSON Data ---

# Working with live APIs and JSON data presents several challenges:

# 1. API Availability and Reliability:
#    - Challenge: Live APIs might be temporarily unavailable due to server issues, maintenance, or network problems.
#    - Impact: Code needs robust error handling (e.g., try-except blocks for requests.exceptions.RequestException) to manage connection timeouts, DNS errors, etc. Response times can vary, potentially slowing down the application.

# 2. Rate Limiting:
#    - Challenge: Many APIs limit the number of requests allowed within a specific time window to prevent abuse.
#    - Impact: Exceeding the limit usually results in an error (like HTTP 429 Too Many Requests). Applications might need logic to handle rate limits, such as pausing requests (backoff) or using API keys that offer higher limits. (randomuser.me is quite open, but this is crucial for most APIs).

# 3. API Changes and Versioning:
#    - Challenge: APIs evolve. The structure of the JSON response, endpoint URLs, or required parameters might change over time (breaking changes).
#    - Impact: This requires ongoing maintenance of the code that interacts with the API to ensure compatibility. Relying on specific API versions (if available) can help mitigate this.

# 4. Data Inconsistency and Quality:
#    - Challenge: Data returned from APIs might not always be consistent or complete. Fields could be missing, null, or have unexpected data types or formats (e.g., different date formats).
#    - Impact: Robust parsing logic is needed (e.g., using .get() with defaults in Python dictionaries, data validation) to handle missing or malformed data gracefully without crashing.
#    - Specific Challenge Here: The API (randomuser.me) generates random data, making it impossible to reliably "match" its generated users (and their API-specific IDs) with pre-existing users in a local database based on a shared ID. This highlights a data mapping/consistency challenge between external and internal data sources.

# 5. JSON Structure Complexity:
#    - Challenge: JSON responses can be deeply nested, requiring careful navigation to extract the desired data points.
#    - Impact: Mistakes in accessing nested keys/indices can lead to KeyErrors or IndexErrors. Libraries or helper functions might be needed for complex parsing.

# 6. Error Handling:
#    - Challenge: Comprehensive error handling is critical. This includes network errors, HTTP error statuses (like 4xx client errors, 5xx server errors), JSON decoding errors (if the response is not valid JSON), and logical errors during data processing after retrieval.

# 7. Security (Authentication/Authorization):
#    - Challenge: Many APIs require authentication (e.g., API keys, OAuth tokens) to identify and authorize the calling application.
#    - Impact: Securely managing these credentials is vital. (Not required for randomuser.me, but a major challenge in general).

 


#Q5


def demonstrateSysFunc():
    dbName = "UsersData.db"
    connect = Connection(dbName)
    cursor = connect.cursor()
    currentYear = 2025
    cursor.execute(''' SELECT Gender , strftime('%Y' ,RegisteredDate) as Years  FROM Users  WHERE Years >= ? ''', (currentYear -5 ,))

    registedByGeder = {"Male" : 0 , "Female" : 0}
    que1 = cursor.fetchall()
    for row in que1 : 
        registedByGeder[row[0]] = registedByGeder.get(row[0], 0) +1 
    
    total = registedByGeder["Male"] + registedByGeder["Female"]
    if total > 0:
        malePercent = registedByGeder["Male"] / total * 100 
        femalePercent = registedByGeder["Female"] / total * 100 
        
        print(f"Percent of Male   : {malePercent:.2f} %")
        print(f"Percent of Female : {femalePercent:.2f} %")
        
    

        
def main():
    print("\n==================== Q1 ====================\n")
    listUsers = load_users_data(r"D:\Ki 5\PRP201c\PRP201c_FA24_PE1_492118\PRP201c_FA24_PE1_492118\PaperNo_2\All\user_data.csv")
    print("\n==================== Q2 ====================\n")
    visualize_users_data(listUsers)
    print("\n==================== Q3 ====================\n")
    store_users_data_in_database(listUsers)
    print("\n==================== Q4 ====================\n")
    fetch_and_update_users_info()
    print("\n==================== Q5 ====================\n")
    demonstrateSysFunc()


if __name__ == "__main__" :
    main()
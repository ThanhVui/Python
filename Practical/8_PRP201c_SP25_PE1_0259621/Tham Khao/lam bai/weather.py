import json
import csv
import sqlite3
import matplotlib.pyplot as plt

# Câu 1: Đọc và in thông tin latitude, longitude, elevation, timezone
with open('berlin_14day_weather.json', 'r') as file:
    data = json.load(file)

latitude = data['latitude']
longitude = data['longitude']
elevation = data['elevation']
timezone = data['timezone']

print("Latitude:", latitude)
print("Longitude:", longitude)
print("Elevation:", elevation)
print("Timezone:", timezone)

# Câu 2: Tìm ngày có biến động nhiệt độ cao nhất
def find_max_fluctuation_day(data):
    dates = data['daily']['time']
    max_temps = data['daily']['temperature_2m_max']
    min_temps = data['daily']['temperature_2m_min']
    
    max_fluctuation = 0
    max_fluctuation_date = ''
    
    for i in range(len(dates)):
        fluctuation = max_temps[i] - min_temps[i]
        if fluctuation > max_fluctuation:
            max_fluctuation = fluctuation
            max_fluctuation_date = dates[i]
    
    print("\nNgày có biến động nhiệt độ cao nhất:")
    print("Ngày:", max_fluctuation_date)
    print("Biến động nhiệt độ:", max_fluctuation)

# Câu 3: Tìm các ngày có nhiệt độ tối đa dưới 15°C
def find_cold_days(data):
    dates = data['daily']['time']
    max_temps = data['daily']['temperature_2m_max']
    
    cold_days = []
    
    for i in range(len(dates)):
        if max_temps[i] < 15:
            cold_days.append(dates[i])
    
    print("\nCác ngày có nhiệt độ tối đa dưới 15°C:")
    if cold_days:
        for day in cold_days:
            print(day)
    else:
        print("Không có ngày nào có nhiệt độ tối đa dưới 15°C.")
    
    return cold_days

# Câu 4: Xuất các ngày lạnh ra file CSV
def export_cold_days_to_csv(data, cold_days):
    dates = data['daily']['time']
    max_temps = data['daily']['temperature_2m_max']
    min_temps = data['daily']['temperature_2m_min']
    
    with open('cold_days.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['date', 'max temp', 'min temp'])
        for day in cold_days:
            index = dates.index(day)
            writer.writerow([day, max_temps[index], min_temps[index]])
    
    print("\nĐã xuất các ngày lạnh ra file cold_days.csv")

# Câu 5: Tạo và điền dữ liệu vào cơ sở dữ liệu SQLite
def create_and_fill_database(data):
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_forecast (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            max_temp REAL,
            min_temp REAL,
            fluctuation REAL
        )
    ''')
    
    cursor.execute('DELETE FROM weather_forecast')
    
    dates = data['daily']['time']
    max_temps = data['daily']['temperature_2m_max']
    min_temps = data['daily']['temperature_2m_min']
    
    for i in range(len(dates)):
        fluctuation = max_temps[i] - min_temps[i]
        cursor.execute('''
            INSERT INTO weather_forecast (date, max_temp, min_temp, fluctuation)
            VALUES (?, ?, ?, ?)
        ''', (dates[i], max_temps[i], min_temps[i], fluctuation))
    
    conn.commit()
    conn.close()
    
    print("\nĐã tạo và điền dữ liệu vào cơ sở dữ liệu weather.db")

# Câu 6: Truy vấn các ngày có nhiệt độ tối thiểu dưới 9°C
def query_cold_nights():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT date FROM weather_forecast WHERE min_temp < 9')
    cold_nights = cursor.fetchall()
    
    print("\nCác ngày có nhiệt độ tối thiểu dưới 9°C:")
    if cold_nights:
        for night in cold_nights:
            print(night[0])
    else:
        print("Không có ngày nào có nhiệt độ tối thiểu dưới 9°C.")
    
    conn.close()

# Câu 7: Tạo báo cáo tóm tắt thời tiết
def generate_weather_summary():
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT max_temp, min_temp FROM weather_forecast')
    records = cursor.fetchall()
    
    max_temps = [record[0] for record in records]
    min_temps = [record[1] for record in records]
    
    avg_max_temp = sum(max_temps) / len(max_temps)
    avg_min_temp = sum(min_temps) / len(min_temps)
    
    cursor.execute('SELECT COUNT(*) FROM weather_forecast WHERE max_temp < 15')
    cold_days_count = cursor.fetchone()[0]
    
    cursor.execute('SELECT COUNT(*) FROM weather_forecast WHERE min_temp < 9')
    cold_nights_count = cursor.fetchone()[0]
    
    full_temp_range = max(max_temps) - min(min_temps)
    
    print("\nWeather Summary Report:")
    print(f"Average Max Temperature: {avg_max_temp:.1f}°C")
    print(f"Average Min Temperature: {avg_min_temp:.1f}°C")
    print(f"Number of Cold Days (Max Temp < 15°C): {cold_days_count}")
    print(f"Number of Cold Nights (Min Temp < 9°C): {cold_nights_count}")
    print(f"Full Temperature Range: {full_temp_range:.1f}°C")
    
    conn.close()

# Câu 8: Vẽ biểu đồ xu hướng nhiệt độ
def plot_temperature_trends(data):
    dates = data['daily']['time']
    max_temps = data['daily']['temperature_2m_max']
    min_temps = data['daily']['temperature_2m_min']
    
    plt.figure(figsize=(10, 5))
    plt.plot(dates, max_temps, label='Max Temperature', marker='o')
    plt.plot(dates, min_temps, label='Min Temperature', marker='o')
    
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Trends Over 14 Days')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()

# Gọi các hàm
find_max_fluctuation_day(data)
cold_days = find_cold_days(data)
export_cold_days_to_csv(data, cold_days)
create_and_fill_database(data)
query_cold_nights()
generate_weather_summary()
plot_temperature_trends(data)
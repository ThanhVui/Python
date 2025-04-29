# Import library
import json 
import csv
import sqlite3
import matplotlib.pyplot as plt

# ====================================Question 1=========================================
def read_file_print_info(file_name):
    print("====================================Question 1=========================================")
    json_data = {}
    try:
        with open(file_name, 'r') as json_file:
            data = json.load(json_file)
            # json_data = json.dumps(data, indent=4)
            # print(json_data)
            
            latitude = data['latitude']
            longitude = data['longitude']
            elevation = data['elevation']
            timezone = data['timezone']
            
            print(f"Latitude values: {latitude}")
            print(f"Longitude values: {longitude}")
            print(f"Elevation values: {elevation}")
            print(f"Timezone values: {timezone}")
            
            return data
    except FileNotFoundError as ex:
        print(f"Error while not found: {ex}")
        
# ====================================Question 2=========================================
def find_max_fluctuation_day(data):
    print("\n====================================Question 2=========================================")
    dates = data['daily']['time']
    print(dates)
    temperature_2m_max = data['daily']['temperature_2m_max']
    print(temperature_2m_max)
    temperature_2m_min = data['daily']['temperature_2m_min']
    print(temperature_2m_min)
    
    max_fluctuation = 0
    count = 0
    for index in range(len(dates)):
        date = dates[index]
        max_temperature = temperature_2m_max[index]
        min_temperature = temperature_2m_min[index]
        print(f"\nDate: {date} - Max Temperature: {max_temperature} - Min Temperature: {min_temperature}")
        
        fluctuation = max_temperature - min_temperature
        print(f"Date: {date} - Fluctuation: {fluctuation:.2f}")
        
        if fluctuation > max_fluctuation:
            max_fluctuation = fluctuation
            
        count += 1
        
    print(f"\nMax Fluctuation: {max_fluctuation:.2f}")
    print(f"Count: {count}")
    
# ====================================Question 3=========================================
def find_cold_days(data):
    print("\n====================================Question 3=========================================")
    cold_days = []
    dates = data['daily']['time']
    max_temperatures = data['daily']['temperature_2m_max']
    
    for index in range(len(dates)):
        date = dates[index]
        max_temperature = max_temperatures[index]
        if max_temperature < 15.0:
            cold_days.append(date)
            print(f"Date: {date} - Max Temperature: {max_temperature}")
    
    for cold_day in cold_days:
        print(f"Cold Day: {cold_day}")
    return cold_days

# ====================================Question 4=========================================
def export_cold_days_to_csv(data, cold_days):
    print("\n====================================Question 4=========================================")
    dates = data['daily']['time']
    temperature_2m_max = data['daily']['temperature_2m_max']
    temperature_2m_min = data['daily']['temperature_2m_min']
    
    with open(r'D:\Study-AI\Python\Practical\8_PRP201c_SP25_PE1_0259621\Tham Khao\lam bai\cold_days_thanh_vui.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['date', 'max_temps', 'min_temps'])
        
        for day in cold_days:
            index = dates.index(day)
            writer.writerow([day, temperature_2m_max[index], temperature_2m_min[index]])
        
        print("Save File cold_days.csv Successfully!")

# ====================================Question 5=========================================
def create_and_fill_database(data):
    print("\n====================================Question 5=========================================")
    try:
        with sqlite3.connect(r'D:\Study-AI\Python\Practical\8_PRP201c_SP25_PE1_0259621\Tham Khao\lam bai\weather_thanh_vui.db') as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS weather_forecast(
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                    date TEXT,
                    max_temps REAL,
                    min_temps REAL,
                    fluctuation REAL
                )""")

            cursor.execute("""
                DELETE FROM weather_forecast
                    """)

            dates = data['daily']['time']
            temperature_2m_max = data['daily']['temperature_2m_max']
            temperature_2m_min = data['daily']['temperature_2m_min']
            count = 0
            
            for index in range(len(dates)):
                date = dates[index]
                max_temperature = float(temperature_2m_max[index])
                min_temperature = float(temperature_2m_min[index])
                fluctuation = float(max_temperature - min_temperature)
                
                cursor.execute("""
                    INSERT OR IGNORE INTO weather_forecast (date, max_temps, min_temps, fluctuation)
                    VALUES(?, ?, ?, ?)
                            """, (date, max_temperature, min_temperature, fluctuation))
                count += 1
            print(f"Insert Into Table All {count} Temperatures Successfully!")
            conn.commit()
    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")
    except Exception as e:
        print(f"Error Exception: {e}")

# ====================================Question 6=========================================
def query_cold_nights(data):
    print("\n====================================Question 6=========================================")
    print("Some day have temperature below than 9C")
    if not data:
        print("Not found data to retrieve!")
        return
        
    try:
        with sqlite3.connect(r'D:\Study-AI\Python\Practical\8_PRP201c_SP25_PE1_0259621\Tham Khao\lam bai\weather_thanh_vui.db') as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT * FROM weather_forecast
                WHERE min_temps < 9
                """)

            list_cold_nights = cursor.fetchall()
            
            for row in list_cold_nights:
                print(f"ID: {row[0]} - Date: {row[1]} - Max temperature: {row[2]} - Min temperature: {row[3]} - Fluctuation: {row[4]:.2f}")
            
    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")
    except Exception as e:
        print(f"Error Exception: {e}")

# ====================================Question 7=========================================
def generate_weather_summary(data):
    print("\n====================================Question 7=========================================")
    
    dates = data['daily']['time']
    temperature_2m_max = data['daily']['temperature_2m_max']
    temperature_2m_min = data['daily']['temperature_2m_min']
    count_days = 0
    total_max_temperature = 0
    total_min_temperature = 0
    print(f"Max temperature: {temperature_2m_max}")
    
    for index in range(len(dates)):
        count_days += 1
        total_max_temperature += temperature_2m_max[index]
        total_min_temperature += temperature_2m_min[index]
    
    cold_days = find_cold_days(data)
    number_of_cold_days = 0
    for cold_day in cold_days:
        number_of_cold_days += 1
    
    # cold_nights = query_cold_nights(data)
    # for cold_night in cold_nights:
    #     number_of_cold_nights += 1
    with sqlite3.connect(r'D:\Study-AI\Python\Practical\8_PRP201c_SP25_PE1_0259621\Tham Khao\lam bai\weather_thanh_vui.db') as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT * FROM weather_forecast
                WHERE min_temps < 9
                """)

            list_cold_nights = cursor.fetchall()
            number_of_cold_nights = 0
            
            for row in list_cold_nights:
                number_of_cold_nights += 1
    
            cursor.execute("""
                SELECT id, date, max_temps, min_temps, fluctuation
                FROM weather_forecast
                           """)
            data_max_min = cursor.fetchall()
            max_temperatures = [row[2] for row in data_max_min]
            min_temperatures = [row[3] for row in data_max_min]
            full_temperature_range = max(max_temperatures) - min(min_temperatures)
    
    avg_max_temperature = total_max_temperature / count_days
    print(f"Average Max Temperature: {avg_max_temperature:.2f}")
    avg_min_temperature = total_min_temperature / count_days
    print(f"Average Min Temperature: {avg_min_temperature:.2f}")
    print(f"Number Of Cold Days: {number_of_cold_days}")
    print(f"Number Of Cold Nights: {number_of_cold_nights}")
    print(f"Full Temperature Range: {full_temperature_range:.2f}\u00B0C")
    
# ====================================Question 8=========================================
def plot_temperature_trends(data):
    print("\n====================================Question 8=========================================")
    
    dates = data['daily']['time']
    temperature_2m_max = data['daily']['temperature_2m_max']
    temperature_2m_min = data['daily']['temperature_2m_min']
    
    plt.figure(figsize=(10, 5))
    plt.plot(dates, temperature_2m_max, label='Max Temperature', marker='o')
    plt.plot(dates, temperature_2m_min, label='Min Temperature', marker='o')
    plt.title("Overview Temperature Max And Min")
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# =======================================Main============================================
def main():
# -------------------------------------Question 1:---------------------------------------
    file_name = 'D:/Study-AI/Python/Practical/8_PRP201c_SP25_PE1_0259621/Tham Khao/lam bai/berlin_14day_weather.json'
    data = read_file_print_info(file_name)
# -------------------------------------Question 2:---------------------------------------
    find_max_fluctuation_day(data)
# -------------------------------------Question 3:---------------------------------------
    cold_days = find_cold_days(data)
# -------------------------------------Question 4:---------------------------------------
    export_cold_days_to_csv(data, cold_days)
# -------------------------------------Question 5:---------------------------------------
    create_and_fill_database(data)
# -------------------------------------Question 6:---------------------------------------
    query_cold_nights(data)
# -------------------------------------Question 7:---------------------------------------
    generate_weather_summary(data)
# -------------------------------------Question 8:---------------------------------------
    plot_temperature_trends(data)
# ---------------------------------------Done--------------------------------------------
    print("All Done!")

# ========================================Main===========================================
if __name__ == "__main__":
    main()
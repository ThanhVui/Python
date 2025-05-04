# Import library
import json 
import csv
import sqlite3
import matplotlib.pyplot as plt

# ====================================Question 1=========================================
def load_and_print_summary(file_name):
    print(f"\n{'=' * 50} Question 1 {'=' * 50}")
    with open(file_name, mode='r', newline='') as json_data_file:
        data = json.load(json_data_file)
        print(data)
        data_json = json.dumps(data, indent=4)
        print(data_json)
        
        # Print summary
        latitude = data['latitude']
        longitude = data['longitude']
        timezone = data['timezone']
        elevation = data['elevation']
        
        print(f"The summary of latitude: {latitude}")
        print(f"The summary of longitude: {longitude}")
        print(f"The summary of timezone: {timezone}")
        print(f"The summary of elevation: {elevation}")
        
        return data
# ====================================Question 2=========================================
# -------------------------------------Task 1:-------------------------------------------
def find_top3_warmest_days(data):
    print(f"\n{'=' * 50} Question 2 {'=' * 50}")
    top3_warmest_days = []
    
    dates = data['daily']['time']
    max_temperatures = data['daily']['temperature_2m_max']
    
    for index in range(len(dates)):
        date = dates[index]
        max_temperature = max_temperatures[index]

        top3_warmest_days.append((date, max_temperature))
        
    top3_warmest_days_sorted = sorted(top3_warmest_days, key=lambda x : x[1], reverse=True)[:3]
         
    for row in top3_warmest_days_sorted:
        print(f"Date: {row[0]} - Temperature: {row[1]}")        
        
    return top3_warmest_days_sorted

# ====================================Question 3=========================================
# -------------------------------------Task 1:-------------------------------------------
def detect_stable_days(data):
    print(f"\n{'=' * 50} Question 3 {'=' * 50}")
    dates = data['daily']['time']
    max_temperatures = data['daily']['temperature_2m_max']
    min_temperatures = data['daily']['temperature_2m_min']
    
    list_stable_days = []
    
    for index in range(len(dates)):
        date = dates[index]
        max_temperature = max_temperatures[index]
        min_temperature = min_temperatures[index]
        
        stable_day = max_temperature - min_temperature
        
        if stable_day <= 5:
            list_stable_days.append((date, stable_day))
            
    for row in list_stable_days:
        print(f"Date: {row[0]} - Stable Temperature: {row[1]:.2f}")
    
    return list_stable_days

# ====================================Question 4=========================================
# -------------------------------------Task 1:-------------------------------------------
def export_stable_day_to_csv(data, list_stable_days):
    print(f"\n{'=' * 50} Question 4 {'=' * 50}")
    dates = data['daily']['time']
    max_temperatures = data['daily']['temperature_2m_max']
    min_temperatures = data['daily']['temperature_2m_min']
    
    with open(r"D:\Study-AI\Python\Practical\9_PRP201c_SP25_PE1_0259621\PaperNo_2\All\stable_days_thanh_vui.csv", mode='w', newline='', encoding='utf-8') as cvs_file:
        writer = csv.writer(cvs_file)
        writer.writerow(['dates', 'max_temps', 'min_temps', 'stable_temperature'])
        count = 0
        
        for row in list_stable_days:
            # Create index variable to find date
            index = dates.index(row[0])
            print(index)
            date = row[0]
            stable_day = row[1]
            max_temp = max_temperatures[index]
            min_temp = min_temperatures[index]
            
            print(date)
            print(f"{stable_day:.2f}")
            print(max_temp)
            print(min_temp)
            stable_day = f"{stable_day:.2f}"
            writer.writerow([date, max_temp, min_temp, stable_day])
            count += 1
            
        print(f"Loads {count} rows stable days successfully!")

# ====================================Question 5 ========================================
# -------------------------------------Task 1:-------------------------------------------
def store_data_in_sqlite(data):
    print(f"\n{'=' * 50} Question 5 {'=' * 50}")
    dates = data['daily']['time']
    max_temperatures = data['daily']['temperature_2m_max']
    min_temperatures = data['daily']['temperature_2m_min']
    
    # Create database and open database
    with sqlite3.connect(r"D:\Study-AI\Python\Practical\9_PRP201c_SP25_PE1_0259621\PaperNo_2\All\weather_thanh_vui.db") as conn:
        cursor = conn.cursor()
        
        # cursor.execute("""
        #         DROP TABLE weather_thanh_vui
        #         """)
                
        # Create table
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS weather_thanh_vui(
                           id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                           date TEXT,
                           max_temp REAL,
                           min_temp REAL,
                           stable_temp REAL
                       )
                       """)
        
        # Loop through data and insert data into table weather_thanh_vui
        count = 0
        for index in range(len(dates)):
            date = dates[index]
            max_temperature = max_temperatures[index]
            min_temperature = min_temperatures[index]
        
            stable_day = max_temperature - min_temperature
            
            # Insert data into table
            cursor.execute("""
                        INSERT OR IGNORE INTO weather_thanh_vui (date, max_temp, min_temp, stable_temp)
                        VALUES(?, ?, ?, ?)
                        """, (date, max_temperature, min_temperature, f"{stable_day:.2f}"))

            count += 1
        print(f"Insert {count} rows into table successfully!")
        # Commit
        conn.commit()

# ====================================Question 6 ========================================
# -------------------------------------Task 1:-------------------------------------------
def unstable_warm_days(data):
    print(f"\n{'=' * 50} Question 6 {'=' * 50}")
    dates = data['daily']['time']
    max_temperatures = data['daily']['temperature_2m_max']
    min_temperatures = data['daily']['temperature_2m_min']
    
    list_unstable_days = []
    
    for index in range(len(dates)):
        date = dates[index]
        max_temperature = max_temperatures[index]
        min_temperature = min_temperatures[index]
        
        stable_day = max_temperature - min_temperature
        
        if stable_day >= 8:
            list_unstable_days.append((date, stable_day))
            
    for row in list_unstable_days:
        print(f"Date: {row[0]} - Unstable Temperature: {row[1]:.2f}\u00b0C")
    
    return list_unstable_days

# ====================================Question 7 ========================================
# -------------------------------------Task 1:-------------------------------------------
def generate_forecast_statistics(data):
    print(f"\n{'=' * 50} Question 7 {'=' * 50}")
    dates = data['daily']['time']
    max_temperatures = data['daily']['temperature_2m_max']
    min_temperatures = data['daily']['temperature_2m_min']
    
    with sqlite3.connect(r"D:\Study-AI\Python\Practical\9_PRP201c_SP25_PE1_0259621\PaperNo_2\All\weather_thanh_vui.db") as conn:
        cursor = conn.cursor()
        
        cursor.execute("""
                    SELECT SUM(max_temp) as max_temp, SUM(min_temp) as min_temp, COUNT(max_temp) as count_temp
                    FROM weather_thanh_vui
                       """)
        sum_temps = cursor.fetchall()
        
        sum_max_temp = sum_temps[0][0]
        sum_min_temp = sum_temps[0][1]
        count_temp = sum_temps[0][2]
        print(sum_max_temp)
        print(sum_min_temp)
        print(count_temp)

    avg_max_temp = sum_max_temp / count_temp
    print(f"Average of Max Temperature: {avg_max_temp:.2f}\u00b0C")
    avg_min_temp = sum_min_temp / count_temp
    print(f"Average of Max Temperature: {avg_min_temp:.2f}\u00b0C")
    
    stable_day = detect_stable_days(data)[0]
    print(f"Stable Day: {stable_day[0]} - Temperature: {stable_day[1]}\u00b0C")
    
    unstable_day = unstable_warm_days(data)[0]
    print(f"Unstable Day: {unstable_day[0]} - Temperature: {unstable_day[1]}\u00b0C")
    
    full_temp = max(max_temperatures) - min(min_temperatures)
    print(f"Full Temperature: {full_temp}\u00b0C")

# ====================================Question 8 ========================================
# -------------------------------------Task 1:-------------------------------------------
def plot_stable_and_unstable_days(data, list_stable_days, list_unstable_days):
    print(f"\n{'=' * 50} Question 8 {'=' * 50}")
    
    stable_days = [row[1] for row in list_stable_days]
    day_stable = [row[0] for row in list_stable_days]
    unstable_days = [row[1] for row in list_unstable_days]
    day_unstable = [row[0] for row in list_unstable_days]

    print(stable_days)
    print(unstable_days)
    
    print(day_stable)
    print(day_unstable)
    
    plt.plot(day_stable, stable_days, marker='o')
    plt.plot(day_unstable, unstable_days, marker='o')
    plt.title("Stable And Unstable Days")
    plt.xlabel("Days")    
    plt.ylabel("Temperatures")    
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# =======================================Main============================================
def main():
# -------------------------------------Task 1:-------------------------------------------
    file_name = r'D:\Study-AI\Python\Practical\9_PRP201c_SP25_PE1_0259621\PaperNo_2\All\berlin_14day_weather.json'
    data = load_and_print_summary(file_name)
# -------------------------------------Task 2:-------------------------------------------
    top3_warmest_days = find_top3_warmest_days(data)
# -------------------------------------Task 3:-------------------------------------------
    list_stable_days = detect_stable_days(data)
# -------------------------------------Task 4:-------------------------------------------
    export_stable_day_to_csv(data, list_stable_days)
# -------------------------------------Task 5:-------------------------------------------
    store_data_in_sqlite(data)
# -------------------------------------Task 6:-------------------------------------------
    list_unstable_days = unstable_warm_days(data)
# -------------------------------------Task 7:-------------------------------------------
    generate_forecast_statistics(data)
# -------------------------------------Task 8:-------------------------------------------
    plot_stable_and_unstable_days(data, list_stable_days, list_unstable_days)
# ========================================Main===========================================
if __name__ == "__main__":
    main()
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
    return

# ====================================Question 6 ========================================
# -------------------------------------Task 1:-------------------------------------------
def unstable_warm_days(data):
    return

# ====================================Question 7 ========================================
# -------------------------------------Task 1:-------------------------------------------
def generate_forecast_statistics(data):
    return

# ====================================Question 8 ========================================
# -------------------------------------Task 1:-------------------------------------------
def plot_stable_and_unstable_days(data):
    return

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

# ========================================Main===========================================
if __name__ == "__main__":
    main()
# ===================================== Import Library ==========================================
import json
import csv
import sqlite3
import matplotlib.pyplot as plt

# ======================================= Question 1: ===========================================
def read_file_print_info(file_name):
    try:
        # Open file and read file
        with open(file_name, mode='r', newline='', encoding='utf-8') as json_file:
            data = json.load(json_file)
            data_format_json = json.dumps(data, indent=4)
            print(data_format_json)

            # Store values into variables
            latitude = data['latitude']
            longitude = data['longitude']
            elevation = data['elevation']
            timezone = data['timezone']
            
            # Print info all values
            print(f"Latitude: {latitude}")
            print(f"Longitude: {longitude}")
            print(f"Elevation: {elevation}")
            print(f"Timezone: {timezone}")
            
            # Return data after read all
            return data
    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except Exception as e:
        print(f"Error while handling data: {e}")
        
# ======================================= Question 2: ===========================================
def find_max_fluctuation_days(data):
    # List all date and temperature max and min in each day
    dates = data['daily']['time']
    temperature_2m_maxs = data['daily']['temperature_2m_max']
    temperature_2m_mins = data['daily']['temperature_2m_min']
    
    max_fluctuation = 0
    max_fluctuation_day = ''
    list_fluctuations = []
    
    # Loop through each day to find each fluctuation
    for index in range(len(dates)):
        date = dates[index]
        temp_max = temperature_2m_maxs[index]
        temp_min = temperature_2m_mins[index]
        
        # Calculate fluctuation of each day
        fluctuation = float(temp_max - temp_min)
        list_fluctuations.append((date, temp_max, temp_min, fluctuation))
        
        # Print fluctuation of each day
        print("Fluctuation of each day:")
        print(f"Date: {date} - Fluctuation: {fluctuation:.2f}\u00b0C")
        
        # Calculate fluctuation to find max fluctuation
        if fluctuation > max_fluctuation:
            max_fluctuation = fluctuation
            max_fluctuation_day = date
    
    print("\nMax fluctuation day:")
    print(f"Max fluctuation Day: {max_fluctuation_day}")
    print(f"Max fluctuation: {max_fluctuation:.2f}\u00b0C")
    
    # Return list_fluctuations
    return list_fluctuations

# ======================================= Question 3: ===========================================
def find_cold_days(data):
    # Create list cold days to return list cold days
    list_cold_days = []
    
    # List all date and temperature max and min in each day
    dates = data['daily']['time']
    temperature_2m_maxs = data['daily']['temperature_2m_max']
    
    # Loop through data to find cold days with max temperature less than 15
    for index in range(len(dates)):
        date = dates[index]
        temp_max = temperature_2m_maxs[index]
        
        # Calculate list cold days
        if temp_max < 15:
            list_cold_days.append(date)
    
    # Return list cold days
    return list_cold_days

# ======================================= Question 4: ===========================================
def write_list_cold_days_to_csv(data, list_cold_days):
    # Path of file
    file_csv_name = r"D:\Study-AI\Python\Practical\8_PRP201c_SP25_PE1_0259621\Tham Khao\lam bai\weather_thanh_vui.csv"
    
    # Get list dates and temperatures max and min
    dates = data['daily']['time']
    temperature_2m_maxs = data['daily']['temperature_2m_max']
    temperature_2m_mins = data['daily']['temperature_2m_min']
    
    # Create file or open file if exist to write file
    with open(file_csv_name, mode='w', newline='', encoding='utf-8') as csv_file:
        # Create method writer to write file
        writer = csv.writer(csv_file)
        # Write header for file column
        writer.writerow(['date', 'max_temp', 'min_temp'])
        
        count = 0
        # Loop through data list of cold days to store list of cold days into csv file
        for day in list_cold_days:
            index = dates.index(day)
            max_temp = f"{temperature_2m_maxs[index]:.2f}"
            min_temp = f"{temperature_2m_mins[index]:.2f}"
            
            writer.writerow([day, max_temp, min_temp])
            count += 1
            
    print(f"Write {count} days into list cold day to csv successfully!")
        
# ======================================= Question 5: ===========================================
def create_and_fill_database(data):
    # Create file path
    file_name_db = r"D:\Study-AI\Python\Practical\8_PRP201c_SP25_PE1_0259621\Tham Khao\lam bai\weather_02_vui.db"
    
    # Get list dates and temperatures max and min
    dates = data['daily']['time']
    temperature_2m_maxs = data['daily']['temperature_2m_max']
    temperature_2m_mins = data['daily']['temperature_2m_min']
    
    # Create database
    with sqlite3.connect(file_name_db) as conn:
        # Call cursor to execute query
        cursor = conn.cursor()
        
        cursor.execute("""
                       DROP TABLE weather_forecast
                       """)
        # Create table
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS weather_forecast(
                           id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                           date TEXT,
                           max_temp REAL,
                           min_temp REAL,
                           fluctuation REAL
                       )
                       """)
        
        # Count row insert into data
        count = 0
        # Insert data into table
        # Loop through data list of cold days to store list of cold days into csv file
        for index in range(len(dates)):
            date = dates[index]
            max_temp = temperature_2m_maxs[index]
            min_temp = temperature_2m_mins[index]
            fluctuation = max_temp - min_temp
            count += 1
            # Execute to insert into database
            cursor.execute("""
                        INSERT OR IGNORE INTO weather_forecast (date, max_temp, min_temp, fluctuation)
                        VALUES (?, ?, ?, ?)
                        """, (date, max_temp, min_temp, fluctuation))
        
        print(f"Insert {count} dates into database successfully!")
        
        conn.commit()
        
# ======================================= Question 6: ===========================================
def find_cold_nighs(data):
    # Create file path
    file_name_db = r"D:\Study-AI\Python\Practical\8_PRP201c_SP25_PE1_0259621\Tham Khao\lam bai\weather_02_vui.db"
    
    # Create list cold nights
    list_cold_nights = []
    
    # Create database
    with sqlite3.connect(file_name_db) as conn:
        # Call cursor to execute query
        cursor = conn.cursor()
        
        cursor.execute("""
                    SELECT date
                    FROM weather_forecast
                    WHERE min_temp < 9
                       """)
        
        list_cold_nights = [row[0] for row in cursor.fetchall()]
        
        conn.commit()
        
    # Return list cold nights
    return list_cold_nights

# ======================================= Question 7: ===========================================
def weather_summary_report(data):
    # Get list dates and temperatures max and min
    dates = data['daily']['time']
    temperature_2m_maxs = data['daily']['temperature_2m_max']
    temperature_2m_mins = data['daily']['temperature_2m_min']
    sum_temperature_2m_maxs = sum(temperature_2m_maxs)            
    sum_temperature_2m_mins = sum(temperature_2m_mins)            
    
    # Calculate count of days
    count_day = 0
    for day in dates:
        count_day += 1
    
    avg_temperature_2m_maxs = sum_temperature_2m_maxs / count_day
    avg_temperature_2m_mins = sum_temperature_2m_mins / count_day
    
    # Cold days
    cold_days = find_cold_days(data)
    number_of_cold_days = len(cold_days)
    
    # Cold nights
    cold_nights = find_cold_nighs(data)
    number_of_cold_nights = len(cold_nights)
    
    # Full temperature range
    full_temp = max(temperature_2m_maxs) - max(temperature_2m_mins)
    
    # Print summary
    print("Weather Summary Report:")
    print(f"Average Of Max Temperature Days: {avg_temperature_2m_maxs:.2f}\u00b0C")
    print(f"Average Of Max Temperature Days: {avg_temperature_2m_mins:.2f}\u00b0C")
    print(f"Number Of Cold Days: {number_of_cold_days}")
    print(f"Number Of Cold Nights: {number_of_cold_nights}")
    print(f"Full Temperature Range: {full_temp:.2f}\u00b0C")
    
# ======================================= Question 8: ===========================================
def visualize_temperature_min_max(data):
    # Extract data
    dates = data['daily']['time']
    temperature_2m_maxs = data['daily']['temperature_2m_max']
    temperature_2m_mins = data['daily']['temperature_2m_min']

    # Create figure and plot lines with enhancements
    plt.figure(figsize=(10, 5))
    
    plt.plot(dates, temperature_2m_maxs, marker='o', linestyle='-', color='red',
             label='Max Temperature (°C)', linewidth=2, markersize=6)
    plt.plot(dates, temperature_2m_mins, marker='o', linestyle='--', color='blue',
             label='Min Temperature (°C)', linewidth=2, markersize=6)

    # Optional: Fill area between min and max to emphasize difference
    plt.fill_between(dates, temperature_2m_mins, temperature_2m_maxs, color='orange', alpha=0.2)

    # Add labels and title
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Temperature (°C)', fontsize=12)
    plt.title('Daily Max and Min Temperatures', fontsize=14, fontweight='bold')

    # Improve legend
    plt.legend(loc='upper right', fontsize=10, frameon=True, shadow=True)

    # Grid and layout
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Show plot
    plt.show()

# ====================================== Main Function ==========================================
def main():
# --------------------------------------- Question 1: -------------------------------------------
    print(f"\n{'=' * 50} Question 1 {'=' * 50}")
    file_name = r"D:\Study-AI\Python\Practical\8_PRP201c_SP25_PE1_0259621\Tham Khao\lam bai\berlin_14day_weather.json"
    data = read_file_print_info(file_name)
    
    # Get list dates and temperatures max and min
    dates = data['daily']['time']
    temperature_2m_maxs = data['daily']['temperature_2m_max']
    temperature_2m_mins = data['daily']['temperature_2m_min']
    
# --------------------------------------- Question 2: -------------------------------------------
    print(f"\n{'=' * 50} Question 2 {'=' * 50}")
    list_fluctuations = find_max_fluctuation_days(data)

# --------------------------------------- Question 3: -------------------------------------------
    print(f"\n{'=' * 50} Question 3 {'=' * 50}")
    print(f"List cold days:")
    list_cold_days = find_cold_days(data)
    for day in list_cold_days:
        index = dates.index(day)
        print(f"Date: {dates[index]} - Max Temperature: {temperature_2m_maxs[index]:.2f}\u00b0C")

# --------------------------------------- Question 4: -------------------------------------------
    print(f"\n{'=' * 50} Question 4 {'=' * 50}")    
    write_list_cold_days_to_csv(data, list_cold_days)
    
# --------------------------------------- Question 5: -------------------------------------------
    print(f"\n{'=' * 50} Question 5 {'=' * 50}")    
    create_and_fill_database(data)
    
# --------------------------------------- Question 6: -------------------------------------------
    print(f"\n{'=' * 50} Question 6 {'=' * 50}")    
    print(f"List cold nights:")
    list_cold_nights = find_cold_nighs(data)
    for day in list_cold_nights:
        index = dates.index(day)
        print(f"Date: {dates[index]} - Min Temperature: {temperature_2m_mins[index]:.2f}\u00b0C")
        
# --------------------------------------- Question 7: -------------------------------------------
    print(f"\n{'=' * 50} Question 7 {'=' * 50}")    
    weather_summary_report(data)
    
# --------------------------------------- Question 8: -------------------------------------------
    print(f"\n{'=' * 50} Question 8 {'=' * 50}")    
    visualize_temperature_min_max(data)
    
    print("All Done! Get 10 Points")

# ========================================== Main ===============================================
if __name__ == "__main__":
    main()
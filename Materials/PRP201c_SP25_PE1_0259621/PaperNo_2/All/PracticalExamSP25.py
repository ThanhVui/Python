# Import library
import json 
import csv
import sqlite3
import matplotlib.pyplot as plt

# ====================================Question 1=========================================
def load_and_print_summary(file_name):
    data_json = []
    data_json = json.dumps(file_name, indent=4)
    print(data_json)
    
    with open(data_json) as json_data_file:
        data = json.load(json_data_file)
    # data_json_load = json.load(data)
    # for row in data:
    #     print(row["timezone"])
    
    # with json.loads(file_name) as file_json:
    #     print(file_json)
        # data_json
    # list_of_data = {}
    # try:
        # list_of_data = json.loads(file_name)
    # data_json = json.load(file_name)
    # # print(int(data_json['latitude']))
    # for row in data_json:
    #     print(f"{row}")
        
    # json.loads(file_name).raw_decode(idx=0)
    # print(list_of_data)
    # for row in list_of_data:
    #     print(f"{row}")
        
        # df = pd.DataFrame(file_name)
    print("Read json successfully!")
    # except Exception as e:
    #     print(f"Error while handling Json: {e}")


# ====================================Question 2=========================================
def find_top3_warmest_days(data):
    return

# ====================================Question 3=========================================
def detect_stable_days(data):
    return

# ====================================Question 4=========================================
def export_stable_day_to_csv(data):
    return

# ====================================Question 5 ========================================
def store_data_in_sqlite(data):
    return

# ====================================Question 6 ========================================
def unstable_warm_days(data):
    return

# ====================================Question 7 ========================================
def generate_forecast_statistics(data):
    return

# ====================================Question 8 ========================================
def plot_stable_and_unstable_days(data):
    return

# =======================================Main============================================
def main():
# -------------------------------------Question 1:---------------------------------------
    file_name = 'berlin_14day_weather.json'
    data = load_and_print_summary(file_name)
# -------------------------------------Question 2:---------------------------------------
    find_top3_warmest_days(data)
# -------------------------------------Question 3:---------------------------------------
    detect_stable_days(data)
# -------------------------------------Question 4:---------------------------------------
    export_stable_day_to_csv(data)
# -------------------------------------Question 5:---------------------------------------
    store_data_in_sqlite(data)
# -------------------------------------Question 6:---------------------------------------
    unstable_warm_days(data)
# -------------------------------------Question 7:---------------------------------------
    generate_forecast_statistics(data)
# -------------------------------------Question 8:---------------------------------------
    plot_stable_and_unstable_days(data)
    
# ========================================Main===========================================
if __name__ == "__main__":
    main()
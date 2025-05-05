# ===================================== Import Library ==========================================
import csv
import sqlite3
import matplotlib.pyplot as plt
import datetime

# ======================================= Question 1: ===========================================
def load_and_print_summary(file_name):
    with open(file_name, mode='r', newline='', encoding='utf-8') as csv_file:
        data = csv.DictReader(csv_file)
        
        count_student = 0
        for row in data:
            count_student += 1
        
        print(f"The number of students: {count_student} students")
        
# ======================================= Question 2: ===========================================
def find_most_active_student(file_name):
    print("Most Active Students:")
    with open(file_name, mode='r', newline='', encoding='utf-8') as csv_file:
        
        data = csv.DictReader(csv_file)
        
        for row in data:
            date = row['date']
            if date < '2025-03-19':
                # print(date)
                print(f"Name: {row['student_name']} - Number Of Reservation: {len(row['room'].split())}")
        
# ======================================= Question 3: ===========================================
def list_fully_booked_days(file_name):
    print("List Full Booked Days:")
    with open(file_name, mode='r', newline='', encoding='utf-8') as csv_file:
        
        data = csv.DictReader(csv_file)
        
        full_booked_days = []
        
        for row in data:
            date = row['date']
                
            room = row['room']
            if date == '2025-03-18':
                full_booked_days.append((row['student_id'], row['student_name'], row['room'], row['date'], row['time_slot']))
                print(f"Date with full booked days: {date}")
        print(f"Number of booked in days: {len(full_booked_days)}") 
        
        return full_booked_days      
# ======================================= Question 4: ===========================================
def export_reservation_by_day(file_name):
    date_input = input("Please Input Date: ")
    file_name_csv = fr"reservation_{date_input}.csv"
    with open(file_name_csv, mode='w', newline='', encoding='utf-8') as csv_file_write:
        write = csv.writer(csv_file_write)
        write.writerow(['student_id', 'student_name', 'room', 'date', 'time_slot'])
        
        with open(file_name, mode='r', newline='', encoding='utf-8') as csv_file_read:
        
            data = csv.DictReader(csv_file_read)
            count = 0
            for row in data:
                student_id = row['student_id']
                student_name = row['student_name']
                room = row['room']
                date = row['date']
                time_slot = row['time_slot']
                
                if date == date_input:
                    write.writerow([student_id, student_name, room, date, time_slot])
                    count += 1
                    
            print(f"Create new file with {date_input} file csv and there are {count} rows successfully!")         
    
# ======================================= Question 5: ===========================================
def store_data_in_sqlite(file_name):
    print("Store data into database in SQLite:")
    # Create database
    file_database = r"lab_booking.db"
    with sqlite3.connect(file_database) as conn:
        cursor = conn.cursor()
        
        cursor.execute("""
                       DROP TABLE IF EXISTS lab_schedule
                       """)
        
        # Create table
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS lab_schedule (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           student_id TEXT,
                           student_name TEXT,
                           room TEXT,
                           date TEXT,
                           time_slot TEXT
                       )
                       """)
        
        # Get data and store data into database
        with open(file_name, mode='r', newline='', encoding='utf-8') as csv_file:
        
            data = csv.DictReader(csv_file)
            count = 0
            
            for row in data:
                student_id = row['student_id']
                student_name = row['student_name']
                room = row['room']
                date = row['date']
                time_slot = row['time_slot']
                
                cursor.execute("""
                            INSERT OR IGNORE INTO lab_schedule (student_id, student_name, room, date, time_slot)
                            VALUES (?, ?, ?, ?, ?)
                            """, (student_id, student_name, room, date, time_slot))
            
                count += 1
            print(f"Store {count} students into database successfully!")
            # Save
            conn.commit()
            
# ======================================= Question 6: ===========================================
def afternoon_booking_per_lab(file_name):
    print("Afternoon Booking Per Lab:")
    
    file_database = r"lab_booking.db"
    with sqlite3.connect(file_database) as conn:
        cursor = conn.cursor()
        
        cursor.execute("""
                    SELECT id, student_id, student_name, room, date, time_slot
                    FROM lab_schedule
                    WHERE time_slot > '12:00'
                       """)
        
        afternoon_bookings = cursor.fetchall()
        
        count = 0
        for row in afternoon_bookings:
            print(f"Room Name: {row[3]}")
            count += 1
            
        print(f"The number of afternoon booking room per lab: {count}")

# ======================================= Question 7: ===========================================
def weekly_report_summary(file_name):
    print("Weekly report summary:")
    # Get data and store data into database
    with open(file_name, mode='r', newline='', encoding='utf-8') as csv_file:
    
        data = csv.DictReader(csv_file)
        count_booking = 0
        count_lab = 0
        
        for row in data:
            student_id = row['student_id']
            student_name = row['student_name']
            room = row['room']
            reservation = row['room'].split()
            date = row['date']
            time_slot = row['time_slot']
            
            if reservation[2] in reservation:
                count_lab += 1 
            
            count_booking += 1

        print(f"Total Booking: {count_booking}")
        print(f"Number of unique students: {count_booking}")
        print(f"Number of booking per lab: {count_lab}")
    
# ======================================= Question 8: ===========================================
def visualize_booking_trend(file_name):
    # Get data and store data into database
    with open(file_name, mode='r', newline='', encoding='utf-8') as csv_file:
    
        data = csv.DictReader(csv_file)
        count_booking = 0

        list_date = []
        list_booking = []
        
        for row in data:
            student_id = row['student_id']
            student_name = row['student_name']
            room = row['room']
            reservation = row['room'].split()
            date = row['date']
            time_slot = row['time_slot']
            
            list_date.append(date)
            list_booking.append(len(reservation))
            
            count_booking += 1
        print(list_date)
        print(list_booking)
        
    plt.plot(list_date, list_booking, marker='o')
    plt.title("Daily Booking Trend")
    plt.xlabel("Date")
    plt.ylabel("Booking Count")
    plt.grid()
    plt.tight_layout()
    plt.show()
    
# ====================================== Main Function ==========================================
def main():
# --------------------------------------- Question 1: -------------------------------------------
    print(f"\n{'=' * 50} Question 1 {'=' * 50}")
    file_name = r"lab_reservation.txt"
    load_and_print_summary(file_name)
    
# --------------------------------------- Question 2: -------------------------------------------
    print(f"\n{'=' * 50} Question 2 {'=' * 50}")
    find_most_active_student(file_name)
    
# --------------------------------------- Question 3: -------------------------------------------
    print(f"\n{'=' * 50} Question 3 {'=' * 50}")
    full_booked_days = list_fully_booked_days(file_name)
    
# --------------------------------------- Question 4: -------------------------------------------
    print(f"\n{'=' * 50} Question 4 {'=' * 50}")
    export_reservation_by_day(file_name)
# --------------------------------------- Question 5: -------------------------------------------
    print(f"\n{'=' * 50} Question 5 {'=' * 50}")
    store_data_in_sqlite(file_name)
# --------------------------------------- Question 6: -------------------------------------------
    print(f"\n{'=' * 50} Question 6 {'=' * 50}")
    afternoon_booking_per_lab(file_name)
# --------------------------------------- Question 7: -------------------------------------------
    print(f"\n{'=' * 50} Question 7 {'=' * 50}")
    weekly_report_summary(file_name)
# --------------------------------------- Question 8: -------------------------------------------
    print(f"\n{'=' * 50} Question 8 {'=' * 50}")
    visualize_booking_trend(file_name)
    print("All Done!")

# ========================================== Main ===============================================
if __name__ == "__main__":
    main()
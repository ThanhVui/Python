import csv
from datetime import datetime
import sqlite3
import requests
import matplotlib.pyplot as plt

# Question 1:
# Task 1: 
class User:
    def __init__(self, id, name, email, location, gender, date_of_birth, registered_date):
        self.id = id
        self.name = name
        self.email = email
        self.location = location
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.registered_date = registered_date
# Task 2:
def load_user_data(filename):
    list_user_data = []
    try:
        with open(filename, 'r', encoding='utf-8', newline='') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                # Validate User information
                if not row['ID'] or not row['Name'] or not row['Email']:
                    print('Row contain empty attribute in user information!')
                    continue
                try:
                    ID = int(row['ID'])       
                    Name = str(row['Name'])
                    Email = str(row['Email'])
                    Location = str(row['Location'])
                    Gender = str(row['Gender'])
                    DateOfBirth = datetime.datetime.strptime(row['DateOfBirth'], "%Y-%m-%d")
                    RegisteredDate = datetime.datetime.strptime(row['RegisteredDate'], "%Y-%m-%d")
                    user = User(ID, Name, Email, Location, Gender, DateOfBirth, RegisteredDate)
                    list_user_data.append(user)
                except Exception as ex:
                    print(f"Error while parsing row: {row} => {ex}")
    except FileNotFoundError:
        print(f"File not found '{filename}'")
    except Exception as e:
        print(f"Error while handling read file: {e}")
    return list_user_data
# Task 3:
""""
- Advantages of using list to store User objects:
+ Simplicity: List is a fundamental of Python data structure, easy to understand and use.
+ Build-in: No need to import special libraries just for storing the data in memory.
+ Ordered: Maintains the order in which users were added.
+ Mutable: Easy to add or remove users from the list after loading.
+ Iteration: Simple to loop through all users.

- Disadvantages of using list to store User objects:
+ Search performance: With is O(n) complexity, which is slow for very large datasets. 
+ Memory usage: For extremely large datasets, storing all Users objects in a list in memory might consume a lot of RAM.
Databases or generators might be more memory-efficient alternatives in such case.
+ Data analyst features: Lists lack the built-in analytical capabilities of structures like Pandas Dataframes.
"""

# Question 2:
# Task 1:
# Line chart:
def visualize_user_data(data):
    # Check validate data found or not found there are data in file or not
    if not data:
        print("Not found data to visualize user!")
        return
    # Collect data to visualize user
    registrations_by_year = {}
    gender_by_location = {}
    
    # Iteration through data to get all users
    for user in data:
        # Collect registrations_by_year to dictionary
        year = user.registered_date.year
        # Count the number of each year
        registrations_by_year[year] = registrations_by_year.get(year, 0) + 1
        
        # Collect gender_by_location to get all users
        loc = user.location.strip()
        gender = user.gender.strip().capitalize()
        # Check if location is empty then assign it equal to zero for male and female
        if loc not in gender_by_location:
            gender_by_location[loc] = {'Male': 0, 'Female': 0}
        # Count the number of gender of each location
        gender_by_location[loc][gender] = gender_by_location[loc].get(gender, 0) + 1
        
    # Create a figure with two subplots (in on figure will have two charts)
    fig, axes =plt.subplots(1, 2, figsize=(16, 8))
    
    # Subplot 1: Registration trend
    years = sorted(registrations_by_year.keys())
    counts = [registrations_by_year[y] for y in years]
    # Set left side is line chart
    # Set attribute for charts
    axis_line = axes[0]
    axis_line.plot(years, counts, marker='o')
    axis_line.set_title("Trend Of User Registrations Over The Years")
    axis_line.set_xlabel("Year")
    axis_line.set_ylabel("Number Of User")
    axis_line.grid(True, linestyle='--', alpha=0.6)
    
    # Subplot 2: Male and Female users per location
    locations = sorted(gender_by_location.keys())
    genders = ['Male', 'Female']    
    gender_count = {g: [gender_by_location[loc].get(g, 0) for loc in locations] for g in genders}
    
    # Split into two 
    axis_bar = axes[1]
    bottom = [0] * len(locations)
    
    # Calculate maximum total user per location for setting y-axis limit
    max_users_per_location = max(sum(gender_by_location[loc].get(g, 0) for g in genders) for loc in locations)
    
    # Set y-axis limit to slightly higher than the maximum
    axis_bar.set_ylim(0, max_users_per_location * 1.2)
    
    # For gender
    for gender in genders:
        axis_bar.bar(locations, gender_count[gender], label=gender, bottom=bottom)
        bottom = [b + c for b, c in zip(bottom, gender_count[gender])]

    axis_bar.set_title("Gender Distribution By Location")
    axis_bar.set_xlabel("Location")
    axis_bar.set_ylabel("Users")
    axis_bar.set_xticks(range(len(locations)))
    axis_bar.set_xticklabels(locations, rotation=45, ha='right')
    axis_bar.legend(title='Gender')
    # Calculate maximum total users
    plt.tight_layout()
    plt.show()
# Task 2:
    """
    The challenges of handling data inconsistencies in visualizations:
    1. Missing values: can lead to incomplete or inaccurate charts.
    2. Incorrect data type: strings instead of numbers/dates can break plots.
    3. Inconsistent formatting/categorization: causes incorrect grouping or labeling.
    4. Outliers: skew the scale and distort the visual interpretation.
    5. Conflicting information: duplication information can lead to unreliable results.
    """

# Question 3:
def store_user_data_in_database(data):
# Task 1:
    if not data:
        print("Not found data to store into database!")
        return
    try:
        # Create database and connect database
        with sqlite3.connect('UserData.db') as conn:
            # Create cursor to execute sql queri
            cursor = conn.cursor()
            
            # Create table Users
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users
                (
                    ID INTEGER PRIMARY KEY,
                    Name TEXT NOT NULL,
                    Email TEXT NOT NULL UNIQUE,
                    Location TEXT NOT NULL,
                    Gender TEXT NOT NULL,
                    DateOfBirth DATETIME NOT NULL,
                    RegisteredDate DATETIME NOT NULL
                )
            ''')
            
            # Insert users data
            for user in data:
                cursor.execute('''
                    INSERT OR IGNORE INTO Users (ID, Name, Email, Location, Gender, DateOfBirth, RegisteredDate)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (user.id, user.name, user.email, user.location, user.gender, user.date_of_birth.strftime('%Y-%m-%d'), user.registered_date.strftime('%Y-%m-%d')))
            
            # Commit
            conn.commit()
            
            # Task 2:
            # Top 5 location with highest number of registered users
            cursor.execute('''
                SELECT Location, COUNT(*) as UserCount
                FROM Users
                GROUP BY Location
                ORDER BY UserCount DESC
                LIMIT 5                      
            ''')
            top_locations = cursor.fetchall()
            print("\nLocation with the highest number of registered users:")
            for location, count in top_locations:
                print(f"Location {location} - Count {count} Users")
                
            # The number of user per gender who registered after 2015
            cursor.execute('''
                SELECT Gender, COUNT(*) AS UserCount
                FROM Users
                WHERE RegisteredDate >= '2016-01-01'
                GROUP BY Gender
            ''')
            user_per_gender = cursor.fetchall()
            print("\nThe number of user per gender who registered after 2015:")
            for gender, count in user_per_gender:
                print(f"Gender: {gender}, Count: {count} users")
            
    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")
    print("\nAll User stored into database successfully!")
    
# Question 4:
def fetch_and_update_user_data(data):
    try:
        with sqlite3.connect('UserData.db') as conn:
            cursor = conn.cursor()

            cursor.execute('''PRAGMA table_info(Users)''')
            existing_columns = [row[1] for row in cursor.fetchall()]
    
            columns_need_add = {
                'Username': 'TEXT',
                'PictureURL': 'TEXT',
                'Timezone': 'TEXT'
            }
            
            for column, data_type in columns_need_add.items():
                if column not in existing_columns:
                    cursor.execute(f'ALTER TABLE Users ADD COLUMN {column} {data_type}')
        
            cursor.execute('''SELECT ID FROM Users''')
            existing_ids = [row[0] for row in cursor.fetchall()]
            
            if not existing_ids:
                print("Not found user's ID to update!")
                return
        
            # Fetch data from https://randomuser.me/api/
            print("Loading data from: https://randomuser.me/api/ .....")
            number_of_users = len(existing_ids)
            response = requests.get(f'https://randomuser.me/api/?results={number_of_users}')
            
            data = response.json().get('results', [])
            print(data)
            update_user_count = 0
            
            for index, user_id in enumerate(existing_ids):
                if index >= len(data):
                    break
                
                user = data[index]
                
                # Extract data from URL
                user_name = user.get('login', {}).get('username', '')
                print(user_name)
                picture_url = user.get('picture', {}).get('large', '')
                print(picture_url)
                time_zone = user.get('location', {}).get('timezone', {}).get('description', '')
                print(time_zone)
                
                cursor.execute('''
                    UPDATE Users
                    SET Username = ?, PictureURL = ?, Timezone = ?       
                    WHERE ID = ?
                ''', (user_name, picture_url, time_zone, user_id))
                
                update_user_count += 1
            conn.commit()
            print(f"Update User Account {update_user_count} Users.")
             
    except requests.exceptions.RequestException as e:
        print(f"Error while handling fetch data from API!: {e}")
    except sqlite3.Error as ex:
        print(f"Error while handling sql!: {ex}")
    except Exception as es:
        print(f"Error!: {es}")
# Task 2:
    """
    Challenges of working with live API and json:
    - API available and reliability: APIs may be down or stable. Use error handling and retries.
    - Rate limiting: request limits can block access.
    - API changes and versioning: update may break code.
    - Data inconsistency and quality: missing or invalid data.
    - Json structure complexity: nested structure cause errors.
    - Error handling: catch all possible exceptions.
    - Security: Authentication needs protection.
    """

# Question 5 Function:
def gender_percentage():
    current_year = datetime.now().year
    cut_off_year = current_year - 5
    try:
        with sqlite3.connect('UserData.db') as conn:
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT Gender, strftime('%Y', RegisteredDate) AS Year
                FROM Users
                WHERE CAST(strftime('%Y', RegisteredDate) AS INTEGER) >= ?
            """, (cut_off_year,))
            rows = cursor.fetchall()
            
            if not rows:
                print(f"No users found who registered from {cut_off_year} to {current_year}")
                return
            
            gender_counts = {'Male': 0, 'Female': 0}
            total_count = 0
            
            for gender, year in rows:
                gender = gender.capitalize()
                if gender in gender_counts:
                    gender_counts[gender] += 1
                    total_count += 1
                    
            print(f"\nGender Distribution for Users Registered from {cut_off_year} to {current_year}:")
            print(f"Total Users: {total_count}")
            
            for gender, count in gender_counts.items():
                percentage = (count / total_count) * 100 if total_count > 0 else 0
                print(f"Gender: {gender}, Count: {count}, Percentage: {percentage:.2f}%")
            
    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")
    except Exception as ex:
        print(f"Exception Error: {ex}")
    
# Question 5:
def main():
    # Question 1:
    filename = "D:/Study-AI/Python/Practical/1_PRP201c_FA24_PE1_492118/PRP201c_FA24_PE1_492118/PRP201c_FA24_PE1_492118/PaperNo_2/All/user_data.csv"
    data = load_user_data(filename)
    
    # Question 2:
    # visualize_user_data(data)
    
    # Question 3:
    store_user_data_in_database(data)
    
    # Question 4:
    fetch_and_update_user_data(data)
    
    # Question 5:
    gender_percentage()
    
# Main
if __name__ == "__main__":
    main()
import re
from datetime import datetime
import csv
import sqlite3
import requests
import matplotlib.pyplot as plt

# Q1: User Class and Data Validation
class User:
    def __init__(self, ID, Name, Email, Location, Gender, DateOfBirth, RegisteredDate):
        self.ID = ID
        self.Name = Name
        self.Email = Email
        self.Location = Location
        self.Gender = Gender
        self.DateOfBirth = DateOfBirth
        self.RegisteredDate = RegisteredDate

    def __repr__(self):
        """Return a string representation of the User object."""
        dob_str = self.DateOfBirth.strftime('%Y-%m-%d') if isinstance(self.DateOfBirth, datetime) else str(self.DateOfBirth)
        reg_str = self.RegisteredDate.strftime('%Y-%m-%d') if isinstance(self.RegisteredDate, datetime) else str(self.RegisteredDate)
        
        return (f"User(ID={self.ID}, Name='{self.Name}', Email='{self.Email}', "
                f"Location='{self.Location}', Gender='{self.Gender}', "
                f"DateOfBirth='{dob_str}', RegisteredDate='{reg_str}')")


def validate_data(id_str, name, email):
    """
    Validates user data fields.
    
    Args:
        id_str (str): User ID string to validate
        name (str): User name to validate
        email (str): User email to validate
        
    Returns:
        bool: True if all validations pass, False otherwise
    """
    # Validate ID (must be numeric)
    if not id_str.isdigit():
        print(f"Validation Error: ID '{id_str}' must contain only digits.")
        return False
    
    # Validate Name (must contain only letters and spaces, and not be empty)
    if not name.strip():
        print(f"Validation Error: Name cannot be empty or just whitespace.")
        return False
    
    if not all(char.isalpha() or char.isspace() for char in name):
        print(f"Validation Error: Name '{name}' should only contain letters and spaces.")
        return False
    
    # Validate Email (must match email format)
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        print(f"Validation Error: Email '{email}' is not valid.")
        return False
    
    return True


def convert_to_datetime(date_str):
    """
    Converts a date string to a datetime object.
    
    Args:
        date_str (str): Date string in 'YYYY-MM-DD' format
        
    Returns:
        datetime: Parsed datetime object or None if parsing fails
    """
    input_date_format = "%Y-%m-%d"
    try:
        return datetime.strptime(date_str.strip(), input_date_format)
    except ValueError as e:
        print(f"Date Conversion Error: Could not parse date '{date_str}' using format '{input_date_format}'. Reason: {e}")
        return None


def load_user_data(filename):
    """
    Loads user data from a CSV file and returns a list of User objects.
    
    Args:
        filename (str): Path to the CSV file
        
    Returns:
        list: List of valid User objects
    """
    users = []
    line_number = 0

    try:
        with open(filename, "r", newline='') as file:
            csv_reader = csv.reader(file)
            
            try:
                header = next(csv_reader)
                line_number += 1
                print(f"CSV Header found: {header}")
                
                if header[0].strip().upper() != 'ID':
                    print(f"Warning: Header does not start with 'ID'. Processing might be incorrect.")
            except StopIteration:
                print("Error: CSV file is empty.")
                return users
            except Exception as e:
                print(f"Error reading header: {e}")
                return users

            for row in csv_reader:
                line_number += 1
                
                # Check if row has expected number of fields
                if len(row) != 7:
                    print(f"Skipping row {line_number}: Expected 7 fields, found {len(row)}. Row content: {row}")
                    continue
                
                # Extract and strip values from row
                id_str, name, email, location, gender, dob_str, reg_date_str = map(str.strip, row)
                
                # Validate basic fields
                if not validate_data(id_str, name, email):
                    print(f"Skipping row {line_number} due to validation error.")
                    continue
                
                # Convert date strings to datetime objects
                dob_obj = convert_to_datetime(dob_str)
                reg_obj = convert_to_datetime(reg_date_str)
                
                if not dob_obj or not reg_obj:
                    print(f"Skipping row {line_number} due to date conversion error.")
                    continue
                
                # Create User object and add to list
                try:
                    user_id = int(id_str)
                    user = User(user_id, name, email, location, gender, dob_obj, reg_obj)
                    users.append(user)
                except ValueError:
                    print(f"Data Error on line {line_number}: ID '{id_str}' could not be converted to integer. Skipping row.")
                    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred while reading file '{filename}' on/near line {line_number}: {e}")

    return users


# --- Discussion: Advantages and Disadvantages of using a List ---

# Advantages of using a list to store User objects:
# 1. Simplicity: Lists are a fundamental Python data structure, easy to understand and use.
# 2. Built-in: No need to import special libraries just for storing the data in memory.
# 3. Ordered: Maintains the order in which users were added (usually the order from the CSV file).
# 4. Mutable: Easy to add or remove users from the list after loading.
# 5. Iteration: Simple to loop through all users (e.g., for processing or display).

# Disadvantages of using a list:
# 1. Search Performance: Finding a specific user by ID or email requires iterating through potentially the entire list (O(n) complexity), which is slow for very large datasets. Dictionaries (using user_id as key) would be much faster (O(1) average complexity) for lookups.
# 2. Memory Usage: For extremely large datasets, storing all User objects in a list in memory might consume a lot of RAM. Databases or generators might be more memory-efficient alternatives in such cases.
# 3. Data Analysis Features: Lists lack the built-in analytical capabilities of structures like Pandas DataFrames (e.g., easy filtering, grouping, aggregation). You'd have to implement these manually.


# Q2: Data Visualization
def visualize_user_data(data):
    """
    Creates visualizations of user data.
    
    Args:
        data (list): List of User objects
    """
    if not data:
        print("No data provided for visualization.")
        return

    # Collect data for visualization
    registrations_by_year = {}
    gender_by_location = {}
    
    for user in data:
        # Collect registration years
        year = user.RegisteredDate.year
        registrations_by_year[year] = registrations_by_year.get(year, 0) + 1

        # Collect gender distribution by location
        loc = user.Location.strip()
        gender = user.Gender.capitalize()
        
        if loc not in gender_by_location:
            gender_by_location[loc] = {'Male': 0, 'Female': 0}
        
        gender_by_location[loc][gender] = gender_by_location[loc].get(gender, 0) + 1

    # Create figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(18, 7))

    # Subplot 1: Registration Trend
    years = sorted(registrations_by_year.keys())
    counts = [registrations_by_year[y] for y in years]
    
    ax1 = axes[0]
    ax1.plot(years, counts, marker='o')
    ax1.set_title('User Registration Trend Over Years')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Registrations')
    ax1.grid(True, linestyle='--', alpha=0.6)

    # Subplot 2: Gender Distribution by Location
    locations = sorted(gender_by_location.keys())
    genders = ['Male', 'Female']
    gender_counts = {g: [gender_by_location[loc].get(g, 0) for loc in locations] for g in genders}
    
    ax2 = axes[1]
    bottom = [0] * len(locations)
    
    # Calculate maximum total users per location for setting y-axis limit
    max_users_per_location = max(
        sum(gender_by_location[loc].get(g, 0) for g in genders)
        for loc in locations
    )
    
    # Set y-axis limit to slightly higher than the maximum
    ax2.set_ylim(0, max_users_per_location * 1.2)  # Add 20% padding
    
    for gender in genders:
        ax2.bar(locations, gender_counts[gender], label=gender, bottom=bottom)
        bottom = [b + c for b, c in zip(bottom, gender_counts[gender])]
    
    ax2.set_title('Gender Distribution by Location')
    ax2.set_xlabel('Location')
    ax2.set_ylabel('Users')
    ax2.set_xticks(range(len(locations)))
    ax2.set_xticklabels(locations, rotation=45, ha='right')
    ax2.legend(title='Gender')

    plt.tight_layout()
    plt.show()
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


# Q3: Database Integration
def store_user_data(data):
    """
    Stores user data in a SQLite database and performs basic analytics.
    
    Args:
        data (list): List of User objects
    """
    if not data:
        print("No data provided to store.")
        return
        
    try:
        with sqlite3.connect("UserData.db") as conn:
            cursor = conn.cursor()
            
            # Create table if it doesn't exist
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Users (
                    ID INTEGER PRIMARY KEY,
                    Name TEXT NOT NULL,
                    Email TEXT NOT NULL UNIQUE,
                    Location TEXT NOT NULL,
                    Gender TEXT NOT NULL,
                    DateOfBirth TEXT NOT NULL,
                    RegisteredDate TEXT NOT NULL
                )
            ''')

            # Insert user data
            for user in data:
                cursor.execute('''
                    INSERT OR IGNORE INTO Users 
                    (ID, Name, Email, Location, Gender, DateOfBirth, RegisteredDate) 
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (
                    user.ID, 
                    user.Name, 
                    user.Email,
                    user.Location, 
                    user.Gender, 
                    user.DateOfBirth.strftime('%Y-%m-%d'),
                    user.RegisteredDate.strftime('%Y-%m-%d')
                ))
            
            conn.commit()

            # Analytics: Top 5 locations with highest number of registered users 
            cursor.execute('''
                SELECT Location, COUNT(*) as UserCount 
                FROM Users 
                GROUP BY Location 
                ORDER BY UserCount DESC 
                LIMIT 5
            ''')
            
            top_locations = cursor.fetchall()
            print("\nTop 5 Locations with Highest Number of Registered Users : ")
            for location, count in top_locations:
                print(f"{location}: {count} users")
        
            # Analytics: Number of users by gender who registered after 2015
            cursor.execute('''
                SELECT Gender, COUNT(*) as UserCount 
                FROM Users 
                WHERE RegisteredDate >= '2016-01-01' 
                GROUP BY Gender
            ''')
            
            gender_counts = cursor.fetchall()
            print("\nNumber of users by gender who registered since 2015:")
            for gender, count in gender_counts:
                print(f"{gender}: {count} users")
            
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    
    print("\nUser data stored in the database and analytics completed successfully.")


# Q4: Fetch and Update User Information
def fetch_and_update_user_info():
    """
    Fetches random user data from an API and updates the database with additional user information.
    """
    try:
        # Connect to database
        with sqlite3.connect("UserData.db") as conn:
            cursor = conn.cursor()
            
            # Check and add new columns if needed
            cursor.execute('PRAGMA table_info(Users)')
            existing_columns = [row[1] for row in cursor.fetchall()]
            
            columns_to_add = {
                "Username": "TEXT",
                "PictureURL": "TEXT",
                "Timezone": "TEXT"
            }
            
            for column, data_type in columns_to_add.items():
                if column not in existing_columns:
                    cursor.execute(f'ALTER TABLE Users ADD COLUMN {column} {data_type}')
                    print(f"Added new column: {column}")

            # Get existing user IDs
            cursor.execute("SELECT ID FROM Users")
            existing_ids = [row[0] for row in cursor.fetchall()]

            if not existing_ids:
                print("No user records found in the database to update.")
                return

            # Fetch data from API
            print("Fetching data from randomuser.me API...")
            response = requests.get("https://randomuser.me/api/?results=10")
            
            if response.status_code != 200:
                print(f"Failed to fetch data from the API. Status code: {response.status_code}")
                return
            
            # Process and update user data
            data = response.json().get("results", [])
            update_count = 0
            
            for i, user_id in enumerate(existing_ids):
                if i >= len(data):
                    break
                    
                user = data[i]
                
                # Extract data from API response
                username = user.get("login", {}).get("username", "")
                picture_url = user.get("picture", {}).get("large", "")
                timezone = user.get("location", {}).get("timezone", {}).get("description", "")
                
                # Update database
                cursor.execute('''
                    UPDATE Users
                    SET Username = ?, PictureURL = ?, Timezone = ?
                    WHERE ID = ?
                ''', (username, picture_url, timezone, user_id))
                
                update_count += 1
            
            conn.commit()
            print(f"Successfully updated {update_count} user records with API data.")
            
    except requests.exceptions.RequestException as e:
        print(f"API connection error: {e}")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


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


# Q5: Gender Percentage by Registration Year
def calculate_gender_percentages():
    """
    Calculates and displays the gender percentages of users registered in the last 5 years.
    """
    current_year = datetime.now().year
    cutoff_year = current_year - 5
    
    print(f"\nCalculating gender percentages for users registered from {cutoff_year} to {current_year}...")
    
    try:
        with sqlite3.connect("UserData.db") as conn:
            cursor = conn.cursor()
            
            # Query users registered in the last 5 years
            cursor.execute("""
                SELECT Gender, strftime('%Y', RegisteredDate) AS Year 
                FROM Users 
                WHERE CAST(Year AS INTEGER) >= ?
            """, (cutoff_year,))

            rows = cursor.fetchall()
            
            if not rows:
                print(f"No users found who registered in the last 5 years (since {cutoff_year}).")
                return
            
            # Count users by gender
            gender_counts = {'Male': 0, 'Female': 0}
            total_count = 0

            for gender, year in rows:
                gender = gender.capitalize()
                if gender in gender_counts:
                    gender_counts[gender] += 1
                    total_count += 1

            # Calculate and display percentages
            print(f"\nGender Distribution for Users Registered Since {cutoff_year}:")
            print(f"Total Users: {total_count}")
            
            for gender, count in gender_counts.items():
                percentage = (count / total_count) * 100 if total_count > 0 else 0
                print(f"{gender}: {count} users ({percentage:.2f}%)")
                
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Main Function
def main():
    """Main program execution flow."""
    print("=" * 80)
    print("USER DATA PROCESSING AND ANALYSIS")
    print("=" * 80)
    
    # Step 1: Load user data from CSV
    print("\nSTEP 1: Loading User Data")
    print("-" * 40)
    user_data_file = "D:/Study-AI/Python/PRP201c/2034/de 1PRP201c_FA24_PE1_492118 tự làm để luyện tập/PRP201c_FA24_PE1_492118/PaperNo_2/All/user_data.csv"
    users = load_user_data(user_data_file)
    
    if users:
        print(f"Successfully loaded {len(users)} user(s).")
    else:
        print("No user data was loaded successfully.")
        return

    # Step 2: Visualize user data
    print("\nSTEP 2: Visualizing User Data")
    print("-" * 40)
    visualize_user_data(users)

    # Step 3: Store user data in database
    print("\nSTEP 3: Storing User Data in Database")
    print("-" * 40)
    store_user_data(users)

    # Step 4: Fetch and update user information
    print("\nSTEP 4: Fetching and Updating User Information")
    print("-" * 40)
    fetch_and_update_user_info()

    # Step 5: Calculate gender percentage by registration year
    print("\nSTEP 5: Calculating Gender Percentage by Registration Year")
    print("-" * 40)
    calculate_gender_percentages()
    
    print("\n" + "=" * 80)
    print("DATA PROCESSING COMPLETE")
    print("=" * 80)


if __name__ == "__main__":
    main()
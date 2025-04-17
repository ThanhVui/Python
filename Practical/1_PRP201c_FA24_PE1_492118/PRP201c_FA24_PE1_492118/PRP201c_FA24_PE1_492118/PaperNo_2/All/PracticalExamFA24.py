import csv
import datetime
from collections import Counter, defaultdict
import sqlite3
import matplotlib.pyplot as plt
import requests


# Question 1:
# Task 1:
class User:  # Define a class to represent a user
    def __init__(self, ID, name, email, location, gender, DateOfBirth, RegisteredDate):
        self.ID = ID
        self.name = name
        self.email = email
        self.location = location
        self.gender = gender
        self.DateOfBirth = DateOfBirth
        self.RegisteredDate = RegisteredDate


# Task 2:
def load_user_data(filename):  # Define a function to load user data from a CSV file
    list_of_users = []  # Initialize an empty list to store user objects
    with open(filename, "r", encoding='utf-8') as csvfile:  # Open the CSV file for reading
        reader = csv.DictReader(
            csvfile
        )  # Read the CSV file into a dictionary reader object
        for row in reader:  # Iterate through each row in the CSV file
            try:
                # Create a User object for each row and append it to the list
                ID = int(row["ID"])
                name = str(row["Name"])
                email = str(row["Email"])
                location = str(row["Location"])
                gender = str(row["Gender"])
                DateOfBirth = datetime.datetime.strptime(row["DateOfBirth"], "%Y-%m-%d")
                RegisteredDate = datetime.datetime.strptime(
                    row["RegisteredDate"], "%Y-%m-%d"
                )
                # Convert the date strings to datetime.date objects
                # If the date strings are empty, set them to None
                user = User(
                    ID, name, email, location, gender, DateOfBirth, RegisteredDate
                )  # Create a User object
                list_of_users.append(user)  # Append the User object to the list
            except (
                Exception
            ) as e:  # Handle any exceptions that occur during data conversion
                continue  # Skip rows with invalid data
    return list_of_users  # Return the list of User objects


# Task 3:
""""
Advantages: Easy to implement, easy to read, and easy to maintain and iterate through list of user objects.
Disadvantages: Searching and updating specific user data can be slow, especially for large datasets. 
                It requires more memory to store the list of user objects compared to a database or other 
                data structures and can be slow (O(n)).
"""


# Question 2:
def visualize_user_date(data):
    # Task 1:
    # Line chart user registration over the years
    years = [
        user.RegisteredDate.year for user in data
    ]  # Extract the years from the RegisteredDate of each user
    year_counts = Counter(years)  # Count the number of users registered each year
    sorted_years = sorted(year_counts.items())  # Sort the years and their counts
    x, y = zip(*sorted_years)  # Unzip the sorted years and counts
    plt.plot(
        x, y, marker="o", linestyle="-", color="b"
    )  # Plot the data with markers and lines
    plt.title("User Registration Over the Years")  # Set the title of the plot
    plt.xlabel("Year")
    plt.ylabel("Number Of Users")
    plt.grid(True)
    plt.show()  # Display the plot

    # Stacked bar chart for the number of male and female users per location
    gender_location = defaultdict(
        lambda: {"Male": 0, "Female": 0}
    )  # Initialize a default dictionary
    for user in data:
        gender_location[user.location][user.gender] += 1  # Count per each location
    locations = list(gender_location.keys())  # Get the list of locations
    males = [
        gender_location[loc]["Male"] for loc in locations
    ]  # Get the males of each location
    females = [
        gender_location[loc]["Female"] for loc in locations
    ]  # Get the females of each location

    x = range(len(locations))
    plt.figure(figsize=(12, 6))  # Set the figure size
    plt.bar(x, females, label="Female")
    plt.bar(x, males, label="Male", bottom=females)  # Stack
    plt.xticks(
        x, locations, rotation=45, ha="right"
    )  # Set the x-ticks to the locations
    plt.title("Gender Distribution Per Location")  # Set the title of the plot
    plt.xlabel("Location")
    plt.ylabel("Number Of Users")
    plt.legend()  # Show the legend
    plt.tight_layout()  # Adjust the layout to fit the figure
    plt.show()  # Display the plot

    # Task 2:
    """
    Challenges of handing data inconsistencies in visualization
    1. Missing or incomplete data: If some users have missing or incomplete data, it can lead to inaccurate visualizations.
    2. Data format inconsistencies: If the data is not in a consistent format, it can lead to errors in parsing and visualizing the data.
    3. Duplicate data: If there are duplicate entries in the data, it can lead to misleading visualizations.
    4. Data type mismatches: If the data types are not consistent, it can lead to errors in calculations and visualizations.
    5. Outliers: If there are outliers in the data, it can skew the visualizations and make them less meaningful.
    """

# Question 3:
# Task 1:
def store_user_data_in_database(data):
    conn = sqlite3.connect("UserData.db")
    cursor = conn.cursor()

    # Create a table to store Users data
    cursor.execute("DROP TABLE IF EXISTS Users")
    cursor.execute(
        """
        CREATE TABLE Users (
            ID INTEGER PRIMARY KEY,
            Name TEXT,
            Email TEXT,
            Location TEXT,
            Gender TEXT,
            DateOfBirth DATETIME,
            RegisteredDate DATETIME
        )
    """
    )
    for user in data:
        cursor.execute(
            """
            INSERT INTO Users (ID, Name, Email, Location, Gender, DateOfBirth, RegisteredDate)
            VALUES (?, ?, ?, ?, ?, ?, ?)           
            """,
            (
                user.ID,
                user.name,
                user.email,
                user.location,
                user.gender,
                user.DateOfBirth,
                user.RegisteredDate,
            ),
        )
    conn.commit()  # Commit the changes to the database

    # Task 2:
    # Top 5 locations with the highest number of registered users.
    print("Top 5 locations with the highest number of registered users:")
    cursor.execute(
        """
        SELECT Location, COUNT(*) as Total 
        FROM Users
        GROUP BY Location
        ORDER BY Total DESC
        LIMIT 5
    """
    )
    for row in cursor.fetchall():
        print(row)

    # The number of users per gender who registered after 2015
    print("The number of users per gender who registered after 2015")
    cursor.execute(
        """
        SELECT Gender, COUNT(*) as Total
        FROM Users
        WHERE RegisteredDate > '2015-01-01 00:00:00'
        GROUP BY Gender
        ORDER BY Total DESC
    """
    )
    for row in cursor.fetchall():
        print(row)
    conn.close()  # Close the database connection


# Question 4:
def fetch_and_update_user_info():
    conn = sqlite3.connect("UserData.db")
    cursor = conn.cursor()

    try:
        cursor.execute("""ALTER TABLE Users ADD COLUMN Username TEXT""")
        cursor.execute("""ALTER TABLE Users ADD COLUMN PictureURL TEXT""")
        cursor.execute("""ALTER TABLE Users ADD COLUMN Timezone TEXT""")
    except sqlite3.OperationalError:
        pass  # Handle the case where the table does not exist

    for user_id in range(1, 21):
        try:
            r = requests.get(f"https://randomuser.me/api/").json()["results"][0]
            username = r["login"]["username"]
            picture_url = r["picture"]["large"]
            timezone = r["location"]["timezone"]["description"]
            cursor.execute(
                """
                UPDATE Users
                SET Username = ?,
                PictureURL = ?,
                Timezone = ?
                WHERE ID = ?
            """,
                (username, picture_url, timezone, user_id)
            )
        except Exception as e:
            continue  # Skip rows with invalid data
    conn.commit()
    conn.close()

# CHALLENGES: Live APIs may fail, return unexpected/missing fields, need try-except
# blocks to handle errors, and may have rate limits.
# Also, the API may not return data in the expected format, so we need to handle that as well.

# Question 5:
def main():
    # Question 1:
    # Load user data from the CSV file
    filename = "D:/Study-AI/Python/Practical/1_PRP201c_FA24_PE1_492118/PRP201c_FA24_PE1_492118/PRP201c_FA24_PE1_492118/PaperNo_2/All/user_data.csv"
    data = load_user_data(filename)
    # Print the loaded user data
    for user in data:
        print(f"ID: {user.ID}, Name: {user.name}, Email: {user.email}, Location: {user.location}, Gender: {user.gender}, DateOfBirth: {user.DateOfBirth}, RegisteredDate: {user.RegisteredDate}")

    # Question 2:
    visualize_user_date(data)

    # Question 3:
    store_user_data_in_database(data)
    
    # Question 4:
    fetch_and_update_user_info()

    # Question 5:
    # Percentage of users by gender who registered in the last 5 years
    print("Percentage of users by gender who registered in the last 5 years:")
    five_years_ago = datetime.datetime(datetime.datetime.now().year - 5, 1, 1)
    recent_users = [user for user in data if user.RegisteredDate >= five_years_ago]
    gender_counts = Counter([user.gender for user in recent_users])
    total_recent_users = sum(gender_counts.values())
    for gender in gender_counts:
        percent = (gender_counts[gender] / total_recent_users) * 100
        print(f"{gender}: {percent:.2f}%")
    
# Main function to execute the program
if __name__ == "__main__":
    main()  # Call the main function to execute the program

import csv
import datetime
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
    fig, axes =plt.subplot(1, 2, figsize=(16, 8))
    
    # Subplot 1: Registration trend
    years = sorted(registrations_by_year.keys())
    counts = [registrations_by_year[y] for y in years]
    # Set left side is line chart
    # Set attribute for charts
    axis_line = axes[0]
    axis_line.plot(years, counts, makers='o')
    axis_line.title("Trend Of User Registrations Over The Years")
    axis_line.xlable("Year")
    axis_line.ylable("Number Of User")
    axis_line.grid(True, linestyle='--', alpha=0.6)
    
    # Subplot 2: Male and Female users per location
    location = sorted(gender_by_location.keys())
    genders = ['Male', 'Female']
    gender_count = {g: [gender_by_location[loc].get(g, 0) for loc in location] for g in genders}
    
    axis_bar = axes[1]
    bottom = [0] * len(location)
    
    # Calculate maximum total users    
    plt.show()
    
# Question 3:

# Question 4:

# Question 5:
def main():
    # Question 1:
    # filename = "D:/Study-AI/Python/PRP201c/2034/de 1PRP201c_FA24_PE1_492118 tự làm để luyện tập/PRP201c_FA24_PE1_492118/PaperNo_2/All/user_data.csv"
    filename = "D:/Study-AI/Python/Practical/1_PRP201c_FA24_PE1_492118/PRP201c_FA24_PE1_492118/PRP201c_FA24_PE1_492118/PaperNo_2/All/user_data.csv"
    data = load_user_data(filename)
    for user in data:
        print(user.id, user.name)
        
    # Question 2:
    visualize_user_data(data)
    
    # Question 3:

    # Question 4:

if __name__ == "__main__":
    main()
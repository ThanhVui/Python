import csv
import datetime

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
            reader_file = csv.reader(file)
            headers = next(reader_file)
            
            for row in reader_file:
                row_dict = dict(zip(headers, [col.strip() for col in row]))
                print(headers)
                # Validate User information
                if not row_dict['ID'] or not row_dict['Name'] or not row_dict['Email']:
                    print('Row contain empty attribute in user information!')
                    continue
                try:
                    ID = int(row_dict['ID'])       
                    Name = str(row_dict['Name'])
                    Email = str(row_dict['Email'])
                    Location = str(row_dict['Location'])
                    Gender = str(row_dict['Gender'])
                    DateOfBirth = datetime.datetime.strptime(row_dict['DateOfBirth'], "%Y-%m-%d")
                    RegisteredDate = datetime.datetime.strptime(row_dict['RegisteredDate'], "%Y-%m-%d")
                    user = User(ID, Name, Email, Location, Gender, DateOfBirth, RegisteredDate)
                    list_user_data.append(user)
                except Exception as ex:
                    print(f"Error while parsing row: {row_dict} => {ex}")
            return list_user_data
    except FileNotFoundError:
        print(f"File not found '{filename}'")
    except Exception as e:
        print(f"Error while handling read file: {e}")
    return []
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

# Question 3:

# Question 4:

# Question 5:
def main():
    # Question 1:
    # filename = "D:/Study-AI/Python/PRP201c/2034/de 1PRP201c_FA24_PE1_492118 tự làm để luyện tập/PRP201c_FA24_PE1_492118/PaperNo_2/All/user_data.csv"
    filename = "D:/Study-AI/Python/Practical/1_PRP201c_FA24_PE1_492118/PRP201c_FA24_PE1_492118/PRP201c_FA24_PE1_492118/PaperNo_2/All/user_data.csv"
    list_users = load_user_data(filename)
    for user in list_users:
        print(user.id, user.name)
    # Question 2:

    # Question 3:

    # Question 4:

if __name__ == "__main__":
    main()
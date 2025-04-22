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
        with open(filename, 'r') as file:
            csv_file = csv.DictReader(file)
            for user in csv_file:
                try:
                    ID = int(user['ID'])
                except:
                    print("Error while processing ID")
                    
                Name = str(user['Name'])
                Email = str(user['Email'])
                Location = str(user['Location'])
                Gender = str(user['Gender'])
                DateOfBirth = datetime.datetime.strptime(user['DateOfBirth'], "%Y-%m-%d")
                RegisteredDate = datetime.datetime.strptime(user['RegisteredDate'], "%Y-%m-%d")
                user = User(ID, Name, Email, Location, Gender, DateOfBirth, RegisteredDate)
                list_user_data.append(user)
        return list_user_data
    except FileNotFoundError:
        print(f"File not found '{filename}'")
    except Exception as e:
        print(f"Error while handling read file: {e}")
        
# Question 2:

# Question 3:

# Question 4:

# Question 5:
def main():
    # filename = "D:/Study-AI/Python/PRP201c/2034/de 1PRP201c_FA24_PE1_492118 tự làm để luyện tập/PRP201c_FA24_PE1_492118/PaperNo_2/All/user_data.csv"
    filename = "D:/Study-AI/Python/Practical/1_PRP201c_FA24_PE1_492118/PRP201c_FA24_PE1_492118/PRP201c_FA24_PE1_492118/PaperNo_2/All/user_data.csv"
    list_users = load_user_data(filename)
    for user in list_users:
        print(user.id, user.name)
        
if __name__ == "__main__":
    main()
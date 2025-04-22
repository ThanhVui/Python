import sqlite3
import csv

def readFromFile(fileName):
    """
    Reads data from a CSV file, skipping the header row.
    Returns a list of lists.
    """
    data = []
    try:
        # Add newline='' and encoding='utf-8'
        with open(fileName, mode="r", newline='', encoding='utf-8') as fileObject:
            csvReader = csv.reader(fileObject)
            try:
                next(csvReader)  # Skip the header row
            except StopIteration:
                print(f"Warning: File '{fileName}' is empty or contains only a header.")
                return [] # Return empty list if file is empty

            # Append each row (which is a list) to the data list
            for row in csvReader:
                if row: # Ensure row is not empty
                    data.append(row)
    except FileNotFoundError:
        print(f"Error: File '{fileName}' not found.")
        return None # Return None if file doesn't exist
    except Exception as e:
        print(f"Error reading file '{fileName}': {e}")
        return None
    return data

def createDataBase(cursor):
    """Creates the tables if they do not already exist."""
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
            EmployeeID TEXT PRIMARY KEY,
            EmployeeName TEXT NOT NULL
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS projects (
            ProjectID TEXT PRIMARY KEY,
            ProjectName TEXT NOT NULL
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employee_project (
            EmployeeID TEXT NOT NULL,
            ProjectID TEXT NOT NULL,
            FOREIGN KEY (EmployeeID) REFERENCES employees(EmployeeID) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (ProjectID) REFERENCES projects(ProjectID) ON DELETE CASCADE ON UPDATE CASCADE,
            PRIMARY KEY (EmployeeID, ProjectID) -- Add PK to ensure pair uniqueness
    );
    ''')
 
def insertDataToDb(cursor, employeeData, projectData, employeeProjectData):
    """Inserts data into tables, ensuring no duplicates are allowed."""
    if employeeData:
        try:
            # Use INSERT OR IGNORE to skip duplicates
            cursor.executemany("INSERT OR IGNORE INTO employees (EmployeeID, EmployeeName) VALUES (?, ?)", employeeData)
        except sqlite3.Error as e:
            print(f"Error inserting into employees: {e}")

    if projectData:
        try:
            cursor.executemany("INSERT OR IGNORE INTO projects (ProjectID, ProjectName) VALUES (?, ?)", projectData)
        except sqlite3.Error as e:
            print(f"Error inserting into projects: {e}")

    if employeeProjectData:
        try:
            cursor.executemany("INSERT OR IGNORE INTO employee_project (EmployeeID, ProjectID) VALUES (?, ?)", employeeProjectData)
        except sqlite3.Error as e:
            print(f"Error inserting into employee_project: {e}")

    # Commit should be handled after all insert operations in main

def retrieveData(cursor, nameE):
    """Queries and prints the projects for a given employee name."""
    query = '''
    SELECT p.ProjectID, p.ProjectName
    FROM employees e
    JOIN employee_project ep ON e.EmployeeID = ep.EmployeeID
    JOIN projects p ON ep.ProjectID = p.ProjectID
    WHERE e.EmployeeName = ?;
    '''
    try:
        cursor.execute(query, (nameE,)) # Parameterized query
        data = cursor.fetchall()
        if not data:
            print(f"No projects found for employee '{nameE}'.")
        else:
            print(f"\nProjects for employee '{nameE}':")
            for row in data:
                print(f"  {row[0]:<5}{'-':<5}{row[1]:<10}")
    except sqlite3.Error as e:
        print(f"Error retrieving data: {e}")

def main():
    dbName = "company_project.sqlite"
    employee_csv = "employees.csv"
    project_csv = "projects.csv"
    employee_project_csv = "employee_projects.csv" # Consistent file name

    conn = None # Initialize conn
    try:
        # Use 'with' for better connection management
        with sqlite3.connect(dbName) as conn:
            cursor = conn.cursor()
            print("Connected to the database.")

            # Enable foreign key support (recommended)
            cursor.execute("PRAGMA foreign_keys = ON;")

            # Create tables
            createDataBase(cursor)
            print("Checked/Created tables successfully.")

            # Read data from CSV files
            employeeData = readFromFile(employee_csv)
            projectData = readFromFile(project_csv)
            employeeProjectData = readFromFile(employee_project_csv)

            # Check if files were read successfully before inserting
            if employeeData is not None and projectData is not None and employeeProjectData is not None:
                # Insert data
                insertDataToDb(cursor, employeeData, projectData, employeeProjectData)
                # conn.commit() is called automatically by 'with' on successful block exit
                print("Inserted data (or ignored duplicates) successfully.")

                # Get employee name and query
                nameE = input("Enter the employee name to find their projects: ").strip()
                if nameE:
                    retrieveData(cursor, nameE)
                else:
                    print("Employee name cannot be empty.")
            else:
                print("Could not insert data due to file reading errors.")

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred in main: {e}")


if __name__ == "__main__":
    main()
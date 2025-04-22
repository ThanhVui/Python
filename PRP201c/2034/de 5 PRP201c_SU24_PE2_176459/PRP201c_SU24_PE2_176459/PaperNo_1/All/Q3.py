import csv
import sqlite3

def readCsvFile(filePath):
    """
    Reads a CSV file and returns a list of rows, skipping the header.
    """
    data = []
    with open(filePath, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header line
        for row in reader:
            if row:  # Skip empty rows
                data.append(row)
    return data

def createDataBase(): 
    dbName = "library_borrowing.sqlite"
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Books (
            BookID TEXT PRIMARY KEY,
            BookTitle TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Members (
            MemberID TEXT PRIMARY KEY,
            NemberName TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Borrowing (
            MemberID TEXT,
            BookID TEXT,
            BorrowDate TEXT,
            PRIMARY KEY (MemberID, BookID)
        )
    ''')
    return conn, cursor

def insertDataToDb(cursor, bookData, memberData, borrowingData):
    for row in bookData:
        cursor.execute("INSERT OR IGNORE INTO Books (BookID, BookTitle) VALUES (?, ?)", row)
    
    for row in memberData:
        cursor.execute("INSERT OR IGNORE INTO Members (MemberID, NemberName) VALUES (?, ?)", row)
    
    for row in borrowingData:
        cursor.execute("INSERT OR IGNORE INTO Borrowing (MemberID, BookID, BorrowDate) VALUES (?, ?, ?)", row)

    cursor.connection.commit()
    
def retriveDataFromDb(cursor):
    name = input("Enter the member's name to find their borrow book : ")
    cursor.execute('''
        SELECT Books.BookID, Books.BookTitle , Borrowing.BorrowDate
        FROM Borrowing 
        JOIN Members ON Borrowing.MemberID = Members.MemberID 
        JOIN Books ON Borrowing.BookID = Books.BookID 
        WHERE Members.NemberName = ?
    ''', (name,))
    rows = cursor.fetchall()
    if rows:
        print(f"Books borrowed by {name}:")
        for row in rows:
            print(f"{row[0]:<5}{'-' :<5}{row[1]}{' (Borrow on ':<5}{row[2]})")
    else:
        print(f"No books found for member: {name}")
  

def main(): 
    conn, cursor = createDataBase()
    bookData = readCsvFile(r'books.csv')
    memberData = readCsvFile(r'members.csv')
    borrowingData = readCsvFile(r'borrowings.csv')
    insertDataToDb(cursor, bookData, memberData, borrowingData)
    retriveDataFromDb(cursor)
    conn.close()

if __name__ == "__main__":
    main()



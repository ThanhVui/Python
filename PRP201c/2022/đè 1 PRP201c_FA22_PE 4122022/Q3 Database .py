import sqlite3

DB_FILE = r"PRODUCT.sqlite"
CATEGORY_FILE = r"category.txt"
PRODUCT_FILE = r"product.txt"

def create_tables(cursor):
    try:
        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS CATEGORY (
                CatID TEXT PRIMARY KEY, 
                CatName TEXT NOT NULL
            ) 
        ''')
        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS PRODUCT (
                PID TEXT PRIMARY KEY, 
                Pname TEXT NOT NULL, 
                CatID TEXT, 
                FOREIGN KEY (CatID) REFERENCES CATEGORY(CatID)
            ) 
        ''')
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")
        exit(1)

def read_file(file_path):
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: {file_path} file not found.")
        exit(1)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        exit(1)

def insert_category_data(cursor, data):
    try:
        for item in data:
            fields = item.split(",")
            if len(fields) == 2:
                cursor.execute(''' 
                    INSERT OR IGNORE INTO CATEGORY (CatID, CatName) 
                    VALUES (?, ?) 
                ''', (fields[0], fields[1]))
    except sqlite3.Error as e:
        print(f"Error inserting into CATEGORY table: {e}")

def insert_product_data(cursor, data):
    try:
        for item in data:
            fields = item.split(",")
            if len(fields) == 3:
                cursor.execute(''' 
                    INSERT OR IGNORE INTO PRODUCT (PID, Pname, CatID) 
                    VALUES (?, ?, ?) 
                ''', (fields[0], fields[1], fields[2]))
    except sqlite3.Error as e:
        print(f"Error inserting into PRODUCT table: {e}")

def display_products(cursor):
    print("\nPRODUCT LIST:")
    print(f"{'ID':<10}{'Product Name':<20}{'Category':<10}")
    print("-" * 40)
    try:
        cursor.execute(''' 
            SELECT P.PID, P.Pname, C.CatName
            FROM PRODUCT P
            INNER JOIN CATEGORY C ON P.CatID = C.CatID
            WHERE C.CatName IN ('Tivi', 'Phone')
            ORDER BY P.Pname DESC
        ''')
        results = cursor.fetchall()
        if results:
            for pid, pname, catname in results:
                print(f"{pid:<10}{pname:<20}{catname:<10}")
        else:
            print("No products found.")
    except sqlite3.Error as e:
        print(f"Error querying data: {e}")

def main():
    try:
        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            create_tables(cursor)

            category_data = read_file(CATEGORY_FILE)
            insert_category_data(cursor, category_data)

            product_data = read_file(PRODUCT_FILE)
            insert_product_data(cursor, product_data)

            display_products(cursor)

    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        exit(1)

if __name__ == "__main__":
    main()
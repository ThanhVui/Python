import sqlite3
import csv


def create_tables(cursor):
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS authors (
                        author_id INTEGER PRIMARY KEY,
                        author_name TEXT UNIQUE)"""
    )

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS books (
                        book_id INTEGER PRIMARY KEY,
                        title TEXT,
                        author_id INTEGER,
                        FOREIGN KEY(author_id) REFERENCES authors(author_id))"""
    )


def insert_data(connection, cursor, data):
    for row in data:
        author_id = cursor.execute(
            "SELECT author_id FROM authors WHERE author_name = ?", (row[2],)
        ).fetchone()
        if author_id:
            author_id = author_id[0]
        else:
            cursor.execute("INSERT INTO authors (author_name) VALUES (?)", (row[2],))
            author_id = cursor.lastrowid
        cursor.execute(
            "INSERT INTO books (title, author_id) VALUES (?, ?)", (row[1], author_id)
        )
    connection.commit()


def find_books_by_author(cursor):
    author_name = input("Enter an author's name to find their books: ")
    cursor.execute(
        """SELECT books.title 
                      FROM books 
                      JOIN authors ON books.author_id = authors.author_id 
                      WHERE authors.author_name = ?""",
        (author_name,),
    )
    books = cursor.fetchall()
    if books:
        print(f"Books by {author_name}:")
        for book in books:
            print(book[0])
    else:
        print("No books found for the author.")


def main():
    connection = sqlite3.connect("library.sqlite")
    cursor = connection.cursor()

    create_tables(cursor)

    with open("book_data.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip the header
        data = list(reader)

    insert_data(connection, cursor, data)

    find_books_by_author(cursor)

    connection.close()


if __name__ == "__main__":
    main()

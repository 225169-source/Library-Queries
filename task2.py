import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("library.db")
cur = conn.cursor()

# Create books table
cur.execute("DROP TABLE IF EXISTS books;")
cur.execute("""
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY,
    title TEXT,
    genre TEXT,
    price INTEGER,
    stock INTEGER
);
""")

# Insert 8 sample books
books = [
    (1, 'Data Science Basics', 'Tech', 1450, 10),
    (2, 'Clean Code', 'Tech', 1200, 8),
    (3, 'The Silent Patient', 'Fiction', 1350, 2),
    (4, 'Python Crash Course', 'Tech', 950, 15),
    (5, 'Dune', 'Fiction', 1100, 4),
    (6, 'Atomic Habits', 'Self-Help', 800, 12),
    (7, '1984', 'Fiction', 600, 7),
    (8, 'Intro to Algorithms', 'Tech', 2200, 3)
]
cur.executemany("INSERT INTO books VALUES (?, ?, ?, ?, ?);", books)
conn.commit()

# Query (a): Books with price > 1000 sorted DESC
print("--- Books above Rs. 1000 (sorted) ---")
cur.execute("SELECT title, price FROM books WHERE price > 1000 ORDER BY price DESC;")
for row in cur.fetchall():
    print(row)

# Query (b): Renaming title as book_title using AS
print("\n--- Renamed Title Column ---")
cur.execute("SELECT title AS book_title, price FROM books;")
for row in cur.fetchall():
    print(row)

# Query (c): Low-stock Fiction books (stock < 5)
print("\n--- Low-stock Fiction books ---")
cur.execute("SELECT title, genre, price, stock FROM books WHERE genre = 'Fiction' AND stock < 5;")
for row in cur.fetchall():
    print(row)

conn.close()

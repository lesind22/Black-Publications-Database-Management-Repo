# Import_Volume_Issue

import sqlite3
import csv

# Connect to the database (creates Publications.db if it doesn't exist)
print("=== Creating Publications.db and Importing Data ===")
conn = sqlite3.connect('Publications.db')
cursor = conn.cursor()

# Drop the existing table (if needed) and recreate it with the correct schema
cursor.execute("DROP TABLE IF EXISTS publications")
cursor.execute('''
CREATE TABLE publications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    publication_title TEXT NOT NULL,
    advertisement_type TEXT NOT NULL,
    volume TEXT,
    issue TEXT
)
''')
print("Table `publications` created successfully!")

# Open and read the CSV file
with open('Ad_Type_BP.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row

    # Prepare data for insertion
    data = [
        ("The Anglo-African Magazine", "Sponsored Content", "2", "3"),
        ("Ringwood's Afro American Journal of Fashion", "Sponsored Content", "2", "5"),
        ("The Voice of the Negro", "Public Service Announcement", "4", "46"),
        ("The Crisis", "Sponsored Content", "68", "13,000"),
        ("The Negro Yearbook: An Encyclopedia of the Negro", "Sponsored Content", "1", "1"),
        ("The Negro Yearbook: An Encyclopedia of the Negro", "Sponsored Content", "1", "2"),
        ("The Half-Century Magazine", "Sponsored Content", "18", "77"),
        ("Black History Bulletin", "Sponsored Content", "88", "176"),
        ("The Black Panther Newspaper", "Public Service Announcement", "15", "30"),
        ("Black World (Negro Digest)", "Public Service Announcement", "25", "53"),
        ("Ebony", "Sponsored Content", "80", "60"),
        ("Jet", "Sponsored Content", "60", "31,000"),
        ("Essence", "Sponsored Content", "55", "440"),
        ("Ebony Jr!", "Public Service Announcement", "7", "71"),
        ("Muhammad Speaks", "Public Service Announcement", "15", "780")
    ]

# Insert data into the `publications` table
cursor.executemany('''
    INSERT INTO publications (publication_title, advertisement_type, volume, issue)
    VALUES (?, ?, ?, ?)
''', data)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Data with volume and issue imported successfully into Publications.db!")
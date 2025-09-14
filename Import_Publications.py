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
    advertisement_type TEXT NOT NULL
)
''')
print("Table `publications` created successfully!")

# Open and read the CSV file
with open('Ad_Type_BP.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip the header row

    # Prepare data for insertion
    data = []
    for row in csv_reader:
        publication_title = row[0].strip()  # First column: Publication_Title
        advertisement_type = row[5].strip()  # Last column: Advertisement_Type_On_Back_Matter
        data.append((publication_title, advertisement_type))

# Prepare data for insertion (including volume and issue)
data = [
    ("The Anglo-African Magazine", "Sponsored Content", "2", "3"),
    ("Ringwood's Afro American Journal of Fashion", "Sponsored Content", "2", "5"),
    ("The Voice of the Negro", "Public Service Announcement", "4", "46"),
    ("The Crisis", "Sponsored Content", "", ""),
    ("Negro Yearbook: An Encyclopedia of the Negro", "Sponsored Content", "", ""),
    ("The Half-Century Magazine", "Sponsored Content", "", ""),

] 
# Insert data into the `publications` table
cursor.executemany('''
    INSERT INTO publications (publication_title, advertisement_type)
    VALUES (?, ?)
''', data)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Data imported successfully into Publications.db!")
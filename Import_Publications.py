# Import_Volume_Issue

import sqlite3
import csv

# Connect to the database (creates Publications.db if it doesn't exist)
print("=== Creating Publications.db and Importing Data ===")
conn = sqlite3.connect('Publications.db')
cursor = conn.cursor()

# Adding in 'time_period' column
cursor.execute("DROP TABLE IF EXISTS publications")
cursor.execute('''
CREATE TABLE publications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    publication_title TEXT NOT NULL,
    advertisement_type TEXT NOT NULL,
    volume TEXT,
    issue TEXT,
    time_period TEXT
)
''')
print("Table `publications` recreated successfully!")


# Open and read the CSV file
with open('Ad_Type_BP.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  

    # Prepare data for insertion
    data = [
    ("Freedom Journal", )
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
    ("Muhammad Speaks", "Public Service Announcement", "15", "780"),
    ("The BAD Times (Black Americans for Democracy)", "Sponsored Content", "20", ""), 
    ("Black Enterprise", "Sponsored Content", "40", "480"),
    ("Black Dialogue", "Sponsored Content", "4", "5"),
    ("The Grassroot Struggle: The Official Organ of the Black Citizens Task Force", "Sponsored Content", "2", "12"),  
    ("Freedomways", "Sponsored Content", "24", "28"),  
    ("Soulbook: Quarterly Journal of Revolutionary Afroamerica", "Sponsored Content", "3", "8"),  
]

# Insert data into the `publications` table
cursor.executemany('''
    INSERT INTO publications (publication_title, advertisement_type, volume, issue, time_period)
    VALUES (?, ?, ?, ?)
''', data)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Data with volume, issue, and time_period imported successfully into Publications.db!")
# Import_Publications

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
    ("Freedom Journal", "Sponsored Content", "2", "103", "1827-1829"),
    ("The North Star Newspaper", "Sponsored Content", "", "187", "1847-1851"),
    ("The Provincial Freeman Newspaper", "Sponsored Content", "", "49", "1853-1857"),
    ("The Christian Recorder Newspaper", "Sponsored Content", "24", "473", "1854-1888"),
    ("The New South Newspaper", "Editorial", "", "67", "1862-1966"),
    ("The California Eagle Newspaper", "Sponsored Content", "80", "", "1879-1964"),
    ("The Woman's Era Newspaper", "Sponsored Content", "3", "22", "1894-1897"),
    ("Ringwood's Afro American Journal of Fashion", "Sponsored Content", "2", "5", "1891-1894"),
    ("The Voice of the Negro", "Public Service Announcement", "4", "46", "1904-1907"),
    ("The Crisis", "Sponsored Content", "68", "13,000", "1910-current"),
    ("The West End News Newspaper", "Sponsored Content", "", "1,305", "1912-1973"),
    ("Opportunity: A Journal of Negro Life", "Sponsored Content", "27", "14", "1923-1949"),
    ("The Negro Yearbook: An Encyclopedia of the Negro", "Sponsored Content", "1", "1", "1951"),
    ("The Negro Yearbook: An Encyclopedia of the Negro", "Sponsored Content", "1", "2", "1952"),
    ("The Half-Century Magazine", "Sponsored Content", "18", "77", "1916-1925"),
    ("Black History Bulletin", "Sponsored Content", "88", "176", "1937-current"),
    ("The Black Panther Newspaper", "Public Service Announcement", "15", "30", "1967-1980"),
    ("Black World (Negro Digest)", "Public Service Announcement", "25", "53", "1942-1976"),
    ("Ebony", "Sponsored Content", "80", "60", "1945-current"),
    ("Jet", "Sponsored Content", "60", "31,000", "1951-2014"),
    ("Essence", "Sponsored Content", "55", "440", "1970-current"),
    ("Ebony Jr!", "Public Service Announcement", "7", "71", "1973-1985"),
    ("Muhammad Speaks", "Public Service Announcement", "15", "780", "1961-1975"),
    ("The BAD Times (Black Americans for Democracy)", "Sponsored Content", "20", "", "1968-1975"),
    ("Black Enterprise", "Sponsored Content", "40", "480", "1970-current"),
    ("Black Dialogue", "Sponsored Content", "4", "5", "1965-1968"),
    ("The Grassroot Struggle: The Official Organ of the Black Citizens Task Force", "Sponsored Content", "2", "12", "1982-1984"),
    ("Freedomways", "Sponsored Content", "24", "28", "1961-1985"),
    ("Soulbook: Quarterly Journal of Revolutionary Afroamerica", "Sponsored Content", "3", "8", "1964-1970"),
    ("The Root Magazine", "Sponsored Content", "29", "", "2008-current")
]
# Insert data into the `publications` table
cursor.executemany('''
    INSERT INTO publications (publication_title, advertisement_type, volume, issue, time_period)
    VALUES (?, ?, ?, ?, ?)
''', data)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Data with volume, issue, and time_period imported successfully into Publications.db!")
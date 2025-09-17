# Import_Publishing_Companies 

import sqlite3

# Connect to the database (creates PublishingCompanies.db if it doesn't exist)
print("=== Creating PublishingCompanies.db and Adding Data ===")
conn = sqlite3.connect('PublishingCompanies.db')
cursor = conn.cursor()

# Create the `publishing_companies` table
cursor.execute('''
CREATE TABLE IF NOT EXISTS publishing_companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL,
    location_city TEXT,
    location_state TEXT,
    founded_year INTEGER,
    description TEXT
)
''')
print("Table `publishing_companies` created successfully!")

# Sample data for publishing companies
data = [
    ("Johnson Publishing Company", "Chicago", "Illinois", 1942, "Publisher of Ebony and Jet magazines."),
    ("The Crisis Publishing Company", "New York City", "New York", 1910, "Publisher of The Crisis magazine."),
    ("Freedomways Associates", "New York City", "New York", 1961, "Publisher of Freedomways journal."),
    ("The Black Panther Party", "Oakland", "California", 1966, "Publisher of The Black Panther Newspaper."),
    ("The Half-Century Magazine Company", "Chicago", "Illinois", 1916, "Publisher of The Half-Century Magazine."),
    ("Essence Communications Inc.", "New York City", "New York", 1968, "Publisher of Essence magazine."),
    ("Black Enterprise Publishing", "New York City", "New York", 1970, "Publisher of Black Enterprise magazine."),
    ("Thomas and Robert Hamiltion", "New York City", "New York", 1858-1860, "Publishers of The Anglo African magazine"), 
    
]

# Insert data into the `publishing_companies` table
cursor.executemany('''
    INSERT INTO publishing_companies (company_name, location_city, location_state, founded_year, description)
    VALUES (?, ?, ?, ?, ?)
''', data)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Data imported successfully into PublishingCompanies.db!")
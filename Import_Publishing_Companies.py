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
    ("Samuel Cornish and John Russwurm", "New York City", "New York", "1827", "Publishers of Freedom's Journal"),
    ("Frederick Douglass", "Rochester", "New York", "1847", "Publisher of The North Star Newspaper"),
    ("Mary Ann Shadd Cary", "Windor, Toronto, and Chatham", "Canada", "1853", "Publisher of The Provincial Freeman Newspaper"),
    ("African Methodist Episcopal Church", "Philadelphia", "Pennsylvania", "1854" "Publisher of The Christian Recorder Newspaper"),
    ("Sears", "Beaufort", "South Carolina", "1862", "Publisher of The New South Newspaper"),
    ("Publisher of The California Eagle Newspaper"),
    ("The Publisher of The Woman's Era Newspaper"),
    ("Opportunity: A Journal of Negro Life"),
    ("Johnson Publishing Company", "Chicago", "Illinois", "1942", "Publisher of Ebony and Jet magazines"),
    ("The Crisis Publishing Company", "New York City", "New York", "1910", "Publisher of The Crisis magazine"),
    ("Freedomways Associates", "New York City", "New York", "1961", "Publisher of Freedomways journal"),
    ("The Black Panther Party", "Oakland", "California", "1966", "Publisher of The Black Panther Newspaper"),
    ("The Half-Century Magazine Company", "Chicago", "Illinois", "1916", "Publisher of The Half-Century Magazine"),
    ("Essence Communications Inc.", "New York City", "New York", "1968", "Publisher of Essence magazine"),
    ("Black Enterprise Publishing", "New York City", "New York", "1970", "Publisher of Black Enterprise magazine"),
    ("J.L. Nichols Publishing Company", "New York City", "New York", "1858-1860", "Publishers of The Anglo African magazine"), 
    ("Publisher of The Root Magazine")
    
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
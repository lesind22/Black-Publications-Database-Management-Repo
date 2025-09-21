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
    founded_year TEXT,
    description TEXT
)
''')
print("Table `publishing_companies` created successfully!")

# Sample data for publishing companies
publishing_companies_data = [
    ("Samuel Cornish and John Russwurm", "New York City", "New York", "1827", "Publishers of Freedom's Journal"),
    ("Frederick Douglass", "Rochester", "New York", "1847", "Publisher of The North Star Newspaper"),
    ("Mary Ann Shadd Cary", "Windsor", "Canada", "1853", "Publisher of The Provincial Freeman Newspaper"),
    ("African Methodist Episcopal Church", "Philadelphia", "Pennsylvania", "1854", "Publisher of The Christian Recorder Newspaper"),
    ("Julia Ringwood Coston", "Cleveland", "Ohio", "1891", "Publisher of Ringwood's Afro-American Journal of Fashion"),
    ("Sears", "Beaufort", "South Carolina", "1862", "Publisher of The New South Newspaper"),
    ("The Voice Publishing Company", "Chicago", "Illinois", "1906", "Publisher's of The Voice of a Negro"),
    ("The West End Publishing Company", "Frederiksted", "St. Croix", "1912", "Publisher's of The West End News Newspaper"),
    ("Headwaiters and Sidewaiters Society of Greater New York", "New York City", "New York", "1917", "Publisher's of The Messenger Magazine"),
    ("Charlotta A. Bass", "Los Angeles", "California", "1912", "Publisher of The California Eagle Newspaper"),
    ("Josephine St. Pierre Ruffin", "Boston", "Massachusetts", "1894", "Publisher of The Woman's Era Newspaper"),
    ("National Urban League", "New York City", "New York", "1923", "Publisher of Opportunity: A Journal of Negro Life"),
    ("Association for the Study of African American Life and History", "Washington", "D.C", "1937", "Publisher's of Black History Bulletin Magazine"),
    ("Moore Publishing and Printing Company", "New York City", "New York", "1904", "Publisher of The Colored American Magazine"),
    ("Johnson Publishing Company", "Chicago", "Illinois", "1942", "Publisher of Ebony and Jet magazines"),
    ("The Crisis Publishing Company", "New York City", "New York", "1910", "Publisher of The Crisis magazine"),
    ("Johnson Publishing Company", "New York City", "New York", "1942", "Publisher of Black World (Negro Digest) Magazine"),
    ("Freedomways Associates", "New York City", "New York", "1961", "Publisher of Freedomways Journal"),
    ("Nation of Islam", "Chicago", "Illinois", "1961", "Publisher's of Muhammad Speaks"),
    ("The Black Panther Party", "Oakland", "California", "1966", "Publisher of The Black Panther Newspaper"),
    ("Black Americans for Democracy Student Organization", "Fayetteville", "Arkansas", "1968", "Publisher's of The BAD Times Newspaper"),
    ("The Half-Century Magazine Company", "Chicago", "Illinois", "1916", "Publisher of The Half-Century Magazine"),
    ("The Negro Year Book Publishing Company", "Tuskegee", "Alabama", "1951", "Publisher's of The Negro Yearbook: Encyclopedia of the Negro"),
    ("The Negro Year Book Publishing Company", "Tuskegee", "Alabama", "1952", "Publisher's of The Negro Yearbook: Encyclopedia of the Negro"),
    ("Ari Publications", "San Francisco", "California", "1965", "Publisher's of Black Dialogue Magazine"),
    ("Essence Communications Inc.", "New York City", "New York", "1968", "Publisher of Essence Magazine"),
    ("Black Enterprise Publishing", "New York City", "New York", "1970", "Publisher of Black Enterprise Magazine"),
    ("Earl G. Graves Publishing Company", "New York City", "New York", "1970", "Publisher's of Black Enterprise Magazine"),
    ("Johnson Publishing Company", "New York City", "New York", "1973", "Publisher's of Ebony Jr!"),
    ("Black Citizens Task Force", "Austin", "Texas", "1982", "Publisher's of The Grassroot Struggle: The Official Organ of the Black Citizens Task Force"),
    ("Revolutionary Action Movement of Berkeley", "Berkeley", "California", "1964", "Publisher's of Soulbook: Quarterly Journal of Revolutionary Afroamerica"),
    ("J.L. Nichols Publishing Company", "New York City", "New York", "1858", "Publishers of The Voice of Negro"), 
    ("GO Media Group", "New York City", "New York", "2019", "Publisher of The Root Magazine")
]

# Debugging: Print each tuple and its length (creation of loop checking each element)
for i, row in enumerate(publishing_companies_data):
    if len(row) != 5:
        print(f"Error in row {i}: {row} (Length: {len(row)})")

# Insert data into the `publishing_companies` table
cursor.executemany('''
    INSERT INTO publishing_companies (company_name, location_city, location_state, founded_year, description)
    VALUES (?, ?, ?, ?, ?)
''', publishing_companies_data)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Data imported successfully into PublishingCompanies.db!")



















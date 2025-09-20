# Import_BP_Data

import sqlite3

# Connect to the database
print("=== Importing Sample Data into Black Publications Database ===")
conn = sqlite3.connect('publications.db')
cursor = conn.cursor()

# Ensure the `publications` table exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS publications (
    publication_id INTEGER PRIMARY KEY AUTOINCREMENT,
    publication_title TEXT NOT NULL,
    audience TEXT,
    frequency TEXT,
    time_period TEXT,
    city TEXT,
    state TEXT
)
''') 

# Sample data to insert
data = [
    ("The Anglo-African Magazine", "Black men and women", "Monthly", "1859-1860", "New York City", "New York"),
    ("Ringwood's Afro American Journal of Fashion", "Black women", "Monthly", "1891-1894", "Cleveland", "Ohio"),
    ("The Voice of the Negro", "Black women and men", "Monthly", "1904-1917", "Atlanta", "Georgia"),
    ("The Colored American", "Black women and men", "Monthly", "1900-1909", "Boston", "Massachusetts"),
    ("The Crisis", "Educated Black men and women", "Monthly/Quarterly", "1910-2021", "New York City", "New York"),
    ("Negro Yearbook: An Encyclopedia of the Negro", "Black women, men, and academics", "Yearly", "1961", "Tuskegee", "Alabama"),
    ("Negro Yearbook: An Encyclopedia of the Negro", "Black women, men, and academics", "Yearly", "1962", "Tuskegee", "Alabama"),
    ("The Half-Century Magazine", "Black women and men", "Monthly", "1916-2025", "Chicago", "Illinois"),
    ("Black History Bulletin", "Black educators and students", "Annually", "1937-current", "Washington", "D.C."),
    ("The Black Panther Party Newspaper", "Black women, students, men, and activists", "Weekly", "1967-1980", "San Francisco", "California"),
    ("Black World (Negro Digest)", "Black women and men", "Monthly", "1942-1970", "Chicago", "Illinois"),
    ("Ebony", "Black women and men", "Monthly", "1945-current", "Chicago", "Illinois"),
    ("Jet", "Black women and men", "Monthly", "1951-2014", "Chicago", "Illinois"),
    ("Essence", "Black women", "Bi-Monthly", "1970-current", "New York City", "New York"),
    ("Ebony Jr.!", "Black children", "Monthly", "1960-1975", "Chicago", "Illinois"),
    ("Black Enterprise", "Black entrepreneurs and small business owners", "Monthly", "1970-current", "New York City", "New York"),
    ("Muhammad Speaks", "Black women, men, members of The Nation of Islam", "Weekly", "1971-1977", "Chicago", "Illinois"),
    ("The BAD Times (Black Americans for Democracy)", "Black students at The University of Arkansas and community", "Weekly", "1950-1975", "Fayetteville", "Arkansas"),
    ("Black Dialogue", "Black students, artists, and writers", "Sporadic", "1965-1970", "San Francisco", "California"),
    ("The Grassroot Struggle: The Official Organ of The Black Citizens Task Force", "Black students, grassroots activists, and militants", "Monthly", "1982-1984", "Austin", "Texas"),
    ("Freedomways", "Black artists, activists, educators, and intellectuals", "Monthly", "1961-1985", "New York City", "New York"),
    ("Soulbook: Quarterly Journal of Revolutionary Afroamerica", "Black students, artists, and writers", "Quarterly", "1964-1980", "Berkeley", "California")
]

# Insert data into the publications table
cursor.executemany('''
    INSERT INTO publications (publication_title, audience, frequency, time_period, publishing_company_city, publishing_company_state)
    VALUES (?, ?, ?, ?, ?, ?)
''', data)

# Commit changes and close the connection
conn.commit()
conn.close()

print("✓ Sample data inserted into the `publications` table.")



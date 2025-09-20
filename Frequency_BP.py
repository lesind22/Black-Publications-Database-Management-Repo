
 
# === Section 1: Importing Sample Data into Black Publications Database ===

import sqlite3 

print("=== Importing Sample Data into Black Publications Database ===")
conn = sqlite3.connect('pub_freq.db')
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

# Data to insert into publications table 
frequency_data = [
    ("Freedom's Journal", "Free Blacks in Northern states", "Weekly", "1827-1829", "New York City", "New York"), 
    ("The North Star Newspaper", "Black and White Abolitionists", "Weekly", "1847-1851", "Rochester", "New York"),
    ("The Provincial Freeman Newspaper", "Blacks fleeing enslavement", "Weekly", "1853-1857", "Windsor, Toronto, Chatham", "Canada"),
    ("The Christian Recorder Newspaper", "Black church communities", "Monthly", "1854-1888", "Philadelphia", "Pennsylvania"),
    ("The New South Newspaper", "White middle class and business owners", "Weekly", "1862-1866", "Beaufort", "South Carolina"),
    ("The California Eagle Newspaper", "Black Los Angeles community-members", "Weekly", "1879-1964", "Los Angeles", "California"),
    ("The Woman's Era Newspaper", "Black elite women", "Monthly", "1894-1897", "Boston", "Massachusetts"),
    ("Opportunity: A Journal of Negro Life", "Black community, scholars, activists, and artists", "Monthly and Quarterly", "1923-1949", "New York City", "New York"),
    ("The Anglo-African Magazine", "Black men and women", "Monthly", "1859-1860", "New York City", "New York"),
    ("Ringwood's Afro American Journal of Fashion", "Black women", "Monthly", "1891-1894", "Cleveland", "Ohio"),
    ("The Voice of the Negro", "Black women and men", "Monthly", "1904-1917", "Atlanta", "Georgia"),
    ("The Colored American", "Black women and men", "Monthly", "1900-1909", "Boston", "Massachusetts"),
    ("The Crisis", "Educated Black men and women", "Monthly/Quarterly", "1910-2021", "New York City", "New York"),
    ("The West End Newspaper", "Islanders of St. Croix",  "Daily and Weekly", "1912-1973", "Frederiksted", "St. Croix"),
    ("Negro Yearbook: An Encyclopedia of the Negro", "Black women, men, and academics", "Yearly", "1951", "Tuskegee", "Alabama"),
    ("Negro Yearbook: An Encyclopedia of the Negro", "Black women, men, and academics", "Yearly", "1952", "Tuskegee", "Alabama"),
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
    ("Soulbook: Quarterly Journal of Revolutionary Afroamerica", "Black students, artists, and writers", "Quarterly", "1964-1980", "Berkeley", "California"),
    ("The Root Magazine", "Black community and scholars", "Monthly", "2008-current", "New York City", "New York")   
] 

# Insert data into the publications table
cursor.executemany('''
    INSERT INTO publications (publication_title, audience, frequency, time_period, city, state)
    VALUES (?, ?, ?, ?, ?, ?)
''', frequency_data) 

# Commit changes and close the connection for publications.db
conn.commit()
conn.close()

# === Section 2: Importing Sample Data into Ad_Type_BP Database ===
print("=== Importing Sample Data into Ad_Type_BP Database ===")
conn = sqlite3.connect('Ad_Type_BP.db')
cursor = conn.cursor()

# Ensure the `ad_types` table exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS ad_types (
    ad_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad_type_name TEXT NOT NULL,
    description TEXT
)
''')

# Sample data to insert into ad_types table
ad_data = [
    ("Sponsored Content", "Advertisements that promote products or services in a way that blends with editorial content."),
    ("Leisure", "Advertisements related to entertainment, travel, and recreational activities."),
    ("Public Service Announcement", "Non-commercial messages intended to inform or educate the public."),
    ("Editorial", "Content that reflects the opinions or perspectives of the publication.")
]

# Insert data into the ad_types table
cursor.executemany('''
    INSERT INTO ad_types (ad_type_name, description)
    VALUES (?, ?)
''', ad_data)

# Commit changes and close the connection for pub_freq.db
conn.commit()
conn.close()

print("Data imported successfully into both databases!")
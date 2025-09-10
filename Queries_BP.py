

# Simple Analysis of Black Publications Dataset 18th-21st centuries
# Century 


# The first question I want to ask from what I've been working with
# so far is "What city and state did these publications thrive
# in from the years 1869-1969".

import sqlite3

# Connect to the database
conn = sqlite3.connect('publications.db')
cursor = conn.cursor()

# Ensure the `publications` table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='publications';")
table_exists = cursor.fetchone()

if not table_exists:
    print("Error: The `publications` table does not exist in the database.")
    conn.close()
    exit()

# Query to find cities and states where publications thrived between 1969-1980
query = '''
SELECT DISTINCT publishing_company_city, publishing_company_state
FROM publications
WHERE time_period LIKE '%1969%' OR time_period LIKE '%1980%'
   OR (CAST(SUBSTR(time_period, 1, 4) AS INTEGER) >= 1969 AND CAST(SUBSTR(time_period, -4) AS INTEGER) <= 1980);
'''

# Execute the query
cursor.execute(query)
results = cursor.fetchall()

# Print the results
print("\nCities and states where publications thrived between 1969-1980:")
for row in results:
    print(f"City: {row[0]}, State: {row[1]}")

# Close the connection
conn.close()
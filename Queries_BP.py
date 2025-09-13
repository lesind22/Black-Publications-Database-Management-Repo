

# Simple Analysis of Black Publications Dataset 18th-21st centuries
# Century 

# What is the time period with the most publications?
# Answer "The time period with the most publications is 1970-Current with 2 publications"


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

# Query to find the time period with the most publications
query = '''
SELECT time_period, COUNT(*) AS publication_count
FROM publications
GROUP BY time_period
ORDER BY publication_count DESC
LIMIT 1;
'''

# Execute the query
cursor.execute(query)
result = cursor.fetchone()

# Print the result
if result:
    print(f"\nThe time period with the most publications is {result[0]} with {result[1]} publications.")
else:
    print("\nNo publications found in the database.")

# Close the connection
conn.close()


# Simple Analysis of Black Publications Dataset 18th-21st centuries
# Century 


# The first question I want to ask from what I've been working with
# so far is "What city and state did these publications thrive
# in from the years 1869-1969".

import sqlite3

# Connect to the database
conn = sqlite3.connect('publications.db')
cursor = conn.cursor()

# Query to find cities and states where publications thrived between 1869-1969
query = '''
SELECT DISTINCT publishing_company_city, publishing_company_state
FROM publications
WHERE time_period LIKE '%1869%' OR time_period LIKE '%1969%'
   OR (CAST(SUBSTR(time_period, 1, 4) AS INTEGER) >= 1869 AND CAST(SUBSTR(time_period, -4) AS INTEGER) <= 1969);
'''

# Execute the query
cursor.execute(query)
results = cursor.fetchall()

# Print the results
print("\nCities and states where publications thrived between 1869-1969:")
for row in results:
    print("City: {row[0]}, State: {row[1]}")

# Close the connection
conn.close()















#  I chose those years because historically 
# what was happening throughout the US and abroad. 
# "What publishing company did the most publishing between 1900-1919"
# It's a working question that is subject to change but that's where my thinking is right now







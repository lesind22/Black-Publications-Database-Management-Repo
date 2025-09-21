# Simple Analysis of Black Publications Dataset 18th-21st centuries


import sqlite3

# Connect to the pub_freq.db database
db_path = "pub_freq.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Query: Retrieve publication titles with an audience of Black women or Black elite women
print("=== Query: Publication Titles with Audience Black Women or Black Elite Women ===")
query_black_women_audience = '''
SELECT publication_title
FROM publications
WHERE audience LIKE '%Black women%'
   OR audience LIKE '%Black elite women%';
'''
cursor.execute(query_black_women_audience)
results = cursor.fetchall()

# Display the results
if results:
    print("Publications with Audience Black Women or Black Elite Women:")
    for row in results:
        print(f"- {row[0]}")
else:
    print("No publications found with Black women or Black elite women as their audience.")

# Close the database connection
conn.close()








# BREAK FOR QUERY 2 #











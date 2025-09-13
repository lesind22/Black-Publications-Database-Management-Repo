# Import_BP_Data (Advertisements)

import sqlite3

# Connect to the database
print("=== Updating Black Publications Database ===")
conn = sqlite3.connect('publications.db')
cursor = conn.cursor()

# Add `volume` and `issue` columns to the `publications` table if they don't already exist
try:
    cursor.execute("ALTER TABLE publications ADD COLUMN volume TEXT")
    cursor.execute("ALTER TABLE publications ADD COLUMN issue TEXT")
    print("Columns `volume` and `issue` added successfully!")
except sqlite3.OperationalError as e:
    print(f"An error occurred (likely columns already exist): {e}")

# Ensure the `publications` table exists (for reference)
cursor.execute('''
CREATE TABLE IF NOT EXISTS publications (
    publication_id INTEGER PRIMARY KEY AUTOINCREMENT,
    publication_title TEXT NOT NULL,
    audience TEXT,
    frequency TEXT,
    time_period TEXT,
    city TEXT,
    state TEXT,
    volume TEXT,
    issue TEXT
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()
print("Database update complete!")
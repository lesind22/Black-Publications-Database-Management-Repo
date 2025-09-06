# Black Publications Database Structure Management 
# HIST 8510 Fall 2025
# Unit 1: Data Infrastructure and Management

import sqlite3

# Connect to the database (creates the file if it doesn't exist)
print("=== Creating Database Structure ===")
conn = sqlite3.connect('publications.db')
cursor = conn.cursor()
print("✓ Connected to publications.db")

# Create the publications table
print("\nCreating `publications` table...")
cursor.execute('''
CREATE TABLE IF NOT EXISTS publications (
    publication_id INTEGER PRIMARY KEY AUTOINCREMENT,
    publication_title TEXT NOT NULL,
    audience TEXT,
    frequency TEXT,
    time_period TEXT
)
''')
print("✓ Created `publications` table.")

# Create the issues table
print("\nCreating `issues` table...")
cursor.execute('''
CREATE TABLE IF NOT EXISTS issues (
    issue_id INTEGER PRIMARY KEY AUTOINCREMENT,
    publication_id INTEGER NOT NULL,
    volume TEXT,
    issue_number TEXT,
    release_date TEXT,
    FOREIGN KEY (publication_id) REFERENCES publications (publication_id)
)
''')
print("✓ Created `issues` table.")

# Create the editors table
print("\nCreating `editors` table...")
cursor.execute('''
CREATE TABLE IF NOT EXISTS editors (
    editor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    editor_name TEXT NOT NULL,
    editor_email TEXT
)
''')
print("✓ Created `editors` table.")

# Commit changes and close the connection
conn.commit()
conn.close()
print("\n✓ Database structure created successfully!")
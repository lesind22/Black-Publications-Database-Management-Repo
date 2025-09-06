# Script to Import Data into the Black Publications Database

import sqlite3
import csv

# Connect to the database
print("=== Importing Data into Black Publications Database ===")
conn = sqlite3.connect('publications.db')
cursor = conn.cursor()
print("✓ Connected to publications.db")

# Function to import data into the publications table
def import_publications(Black_Publications_CSV):
    print("\nImporting data into `publications` table...")
    with open(Black_Publications_CSV, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute('''
                INSERT INTO publications (publication_title, audience, frequency, time_period)
                VALUES (?, ?, ?, ?)
            ''', (row['publication_title'], row['audience'], row['frequency'], row['time_period']))
    print(f"✓ Data imported into `publications` table from {Black_Publications_CSV}")

# Function to import data into the issues table
def import_issues(Black_Publications_CSV):
    print("\nImporting data into `issues` table...")
    with open(Black_Publications_CSV, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute('''
                INSERT INTO issues (publication_id, volume, issue_number, release_date)
                VALUES (?, ?, ?, ?)
            ''', (row['publication_id'], row['volume'], row['issue_number'], row['release_date']))
    print(f"✓ Data imported into `issues` table from {Black_Publications_CSV}")

# Paths to the CSV files
Black_Publications_CSV = '/path/to/Black_Publications_CSV.csv'  # Replace with the actual path to your publications CSV file
Black_Publications_CSV = '/path/to/issues.csv'  # Replace with the actual path to your issues CSV file

# Import data
import_publications(Black_Publications_CSV)
import_issues(Black_Publications_CSV)

# Commit changes and close the connection
conn.commit()
conn.close()
print("\n✓ Data import completed successfully!")
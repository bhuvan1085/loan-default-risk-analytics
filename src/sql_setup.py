# src/sql_setup.py
"""
SQL Database Setup - Load cleaned data into SQLite
"""

import pandas as pd
import sqlite3
import os

print("="*70)
print("🗄️ SQL DATABASE SETUP")
print("="*70)

# Load cleaned data
print("\n📂 Loading cleaned data...")
df = pd.read_csv('data/processed/loan_default_cleaned.csv')
print(f"✅ Loaded {len(df):,} records")

# Create SQLite database
db_path = 'loan_default.db'
print(f"\n📁 Creating database: {db_path}")

# Connect to database (creates if doesn't exist)
conn = sqlite3.connect(db_path)

# Write data to SQL table
print("\n📝 Writing data to SQL table...")
df.to_sql('loan_data', conn, if_exists='replace', index=False)
print(f"✅ Table 'loan_data' created with {len(df):,} rows")

# Verify
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM loan_data")
count = cursor.fetchone()[0]
print(f"\n🔍 Verification: {count:,} rows in table")

# Show table schema
cursor.execute("PRAGMA table_info(loan_data)")
columns = cursor.fetchall()
print("\n📊 Table Schema:")
for col in columns:
    print(f"   {col[1]}: {col[2]}")

# Close connection
conn.close()
print("\n✅ Database setup complete!")
# src/sql_analysis.py
"""
SQL Analysis - Run queries from SQL file
"""

import sqlite3
import pandas as pd
import os

print("="*70)
print("🗄️ SQL ANALYSIS - LOAN DEFAULT DATASET")
print("="*70)

# Connect to database
conn = sqlite3.connect('loan_default.db')

print("\n📊 RUNNING BUSINESS QUERIES")
print("="*70)

# Query 1: Overall Default Rate
print("\n1️⃣ OVERALL DEFAULT RATE:")
query = '''
SELECT 
    COUNT(*) as total_loans,
    SUM("Default") as total_defaults,
    ROUND(CAST(SUM("Default") AS FLOAT) / COUNT(*) * 100, 2) as default_rate_pct
FROM loan_data
'''
df_result = pd.read_sql_query(query, conn)
print(df_result.to_string(index=False))

# Query 2: Default Rate by Education
print("\n2️⃣ DEFAULT RATE BY EDUCATION:")
query = '''
SELECT 
    Education,
    COUNT(*) as total_loans,
    SUM("Default") as defaults,
    ROUND(CAST(SUM("Default") AS FLOAT) / COUNT(*) * 100, 2) as default_rate
FROM loan_data
GROUP BY Education
ORDER BY default_rate DESC
'''
df_result = pd.read_sql_query(query, conn)
print(df_result.to_string(index=False))

# Query 3: Default Rate by Employment Type
print("\n3️⃣ DEFAULT RATE BY EMPLOYMENT TYPE:")
query = '''
SELECT 
    EmploymentType,
    COUNT(*) as total_loans,
    SUM("Default") as defaults,
    ROUND(CAST(SUM("Default") AS FLOAT) / COUNT(*) * 100, 2) as default_rate
FROM loan_data
GROUP BY EmploymentType
ORDER BY default_rate DESC
'''
df_result = pd.read_sql_query(query, conn)
print(df_result.to_string(index=False))

# Query 4: Default Rate by Credit Category
print("\n4️⃣ DEFAULT RATE BY CREDIT CATEGORY:")
query = '''
SELECT 
    CASE 
        WHEN CreditScore >= 800 THEN 'Excellent'
        WHEN CreditScore >= 740 THEN 'Very Good'
        WHEN CreditScore >= 670 THEN 'Good'
        WHEN CreditScore >= 580 THEN 'Fair'
        ELSE 'Poor'
    END as credit_category,
    COUNT(*) as total_loans,
    SUM("Default") as defaults,
    ROUND(CAST(SUM("Default") AS FLOAT) / COUNT(*) * 100, 2) as default_rate
FROM loan_data
GROUP BY credit_category
ORDER BY default_rate DESC
'''
df_result = pd.read_sql_query(query, conn)
print(df_result.to_string(index=False))

# Query 5: Highest Risk Profiles
print("\n5️⃣ TOP 5 HIGHEST RISK PROFILES:")
query = '''
SELECT 
    Education,
    EmploymentType,
    LoanPurpose,
    COUNT(*) as loan_count,
    SUM("Default") as defaults,
    ROUND(CAST(SUM("Default") AS FLOAT) / COUNT(*) * 100, 2) as default_rate
FROM loan_data
GROUP BY Education, EmploymentType, LoanPurpose
HAVING COUNT(*) > 50
ORDER BY default_rate DESC
LIMIT 5
'''
df_result = pd.read_sql_query(query, conn)
print(df_result.to_string(index=False))

# Query 6: Co-Signer Impact
print("\n6️⃣ CO-SIGNER IMPACT ANALYSIS:")
query = '''
SELECT 
    HasCoSigner,
    COUNT(*) as total_loans,
    SUM("Default") as defaults,
    ROUND(CAST(SUM("Default") AS FLOAT) / COUNT(*) * 100, 2) as default_rate,
    ROUND(AVG(LoanAmount), 0) as avg_loan_amount
FROM loan_data
GROUP BY HasCoSigner
'''
df_result = pd.read_sql_query(query, conn)
print(df_result.to_string(index=False))

# Query 7: Age Group Risk
print("\n7️⃣ DEFAULT RATE BY AGE GROUP:")
query = '''
SELECT 
    CASE 
        WHEN Age BETWEEN 18 AND 29 THEN '18-29'
        WHEN Age BETWEEN 30 AND 39 THEN '30-39'
        WHEN Age BETWEEN 40 AND 49 THEN '40-49'
        WHEN Age BETWEEN 50 AND 59 THEN '50-59'
        WHEN Age BETWEEN 60 AND 69 THEN '60-69'
    END as age_group,
    COUNT(*) as total_loans,
    SUM("Default") as defaults,
    ROUND(CAST(SUM("Default") AS FLOAT) / COUNT(*) * 100, 2) as default_rate
FROM loan_data
GROUP BY age_group
ORDER BY default_rate DESC
'''
df_result = pd.read_sql_query(query, conn)
print(df_result.to_string(index=False))

# Query 8: Default Rate by DTI Risk Level
print("\n8️⃣ DEFAULT RATE BY DTI RISK LEVEL:")
query = '''
SELECT 
    CASE 
        WHEN DTIRatio <= 0.3 THEN 'Low'
        WHEN DTIRatio <= 0.5 THEN 'Medium'
        WHEN DTIRatio <= 0.7 THEN 'High'
        ELSE 'Very High'
    END as dti_risk,
    COUNT(*) as total_loans,
    SUM("Default") as defaults,
    ROUND(CAST(SUM("Default") AS FLOAT) / COUNT(*) * 100, 2) as default_rate
FROM loan_data
GROUP BY dti_risk
ORDER BY default_rate DESC
'''
df_result = pd.read_sql_query(query, conn)
print(df_result.to_string(index=False))

# Query 9: Loan Amount Distribution by Default
print("\n9️⃣ LOAN AMOUNT DISTRIBUTION BY DEFAULT:")
query = '''
SELECT 
    CASE 
        WHEN LoanAmount < 50000 THEN 'Under 50K'
        WHEN LoanAmount < 100000 THEN '50K-100K'
        WHEN LoanAmount < 200000 THEN '100K-200K'
        ELSE 'Over 200K'
    END as loan_size,
    COUNT(*) as total_loans,
    SUM("Default") as defaults,
    ROUND(CAST(SUM("Default") AS FLOAT) / COUNT(*) * 100, 2) as default_rate
FROM loan_data
GROUP BY loan_size
ORDER BY default_rate DESC
'''
df_result = pd.read_sql_query(query, conn)
print(df_result.to_string(index=False))

# Save all results to CSV
print("\n📁 Saving query results to CSV...")
os.makedirs('sql_results', exist_ok=True)

queries = {
    'overall_default_rate': 'SELECT COUNT(*) as total_loans, SUM("Default") as total_defaults, ROUND(CAST(SUM("Default") AS FLOAT) / COUNT(*) * 100, 2) as default_rate_pct FROM loan_data',
    'education_default': 'SELECT Education, COUNT(*) as total_loans, SUM("Default") as defaults, ROUND(CAST(SUM("Default") AS FLOAT) / COUNT(*) * 100, 2) as default_rate FROM loan_data GROUP BY Education ORDER BY default_rate DESC',
    'employment_default': 'SELECT EmploymentType, COUNT(*) as total_loans, SUM("Default") as defaults, ROUND(CAST(SUM("Default") AS FLOAT) / COUNT(*) * 100, 2) as default_rate FROM loan_data GROUP BY EmploymentType ORDER BY default_rate DESC',
    'loan_purpose_default': 'SELECT LoanPurpose, COUNT(*) as total_loans, SUM("Default") as defaults, ROUND(CAST(SUM("Default") AS FLOAT) / COUNT(*) * 100, 2) as default_rate FROM loan_data GROUP BY LoanPurpose ORDER BY default_rate DESC',
    'age_group_default': "SELECT CASE WHEN Age BETWEEN 18 AND 29 THEN '18-29' WHEN Age BETWEEN 30 AND 39 THEN '30-39' WHEN Age BETWEEN 40 AND 49 THEN '40-49' WHEN Age BETWEEN 50 AND 59 THEN '50-59' WHEN Age BETWEEN 60 AND 69 THEN '60-69' END as age_group, COUNT(*) as total_loans, SUM(\"Default\") as defaults, ROUND(CAST(SUM(\"Default\") AS FLOAT) / COUNT(*) * 100, 2) as default_rate FROM loan_data GROUP BY age_group ORDER BY default_rate DESC"
}

for name, query in queries.items():
    df = pd.read_sql_query(query, conn)
    df.to_csv(f'sql_results/{name}.csv', index=False)
    print(f"✅ Saved: sql_results/{name}.csv")

conn.close()
print("\n✅ SQL Analysis Complete!")
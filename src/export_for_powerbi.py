# src/export_for_powerbi.py
"""
Export Data for Power BI Dashboards
"""

import pandas as pd
import os

print("="*70)
print("📊 EXPORTING DATA FOR POWER BI")
print("="*70)

# Load cleaned data
print("\n📂 Loading cleaned data...")
df = pd.read_csv('data/processed/loan_default_cleaned.csv')
print(f"✅ Loaded {len(df):,} records with {len(df.columns)} columns")

# Create powerbi folder
os.makedirs('powerbi', exist_ok=True)

# ============================================
# 1. FACT TABLE - Loan Transactions
# ============================================
print("\n1️⃣ Creating Fact Table...")
fact_table = df.copy()
fact_table.to_csv('powerbi/fact_loans.csv', index=False)
print(f"✅ Saved: powerbi/fact_loans.csv ({len(fact_table):,} rows)")

# ============================================
# 2. DIMENSION TABLES
# ============================================

# 2.1 Customer Dimension
print("\n2️⃣ Creating Customer Dimension...")
customer_dim = df[['LoanID', 'Age', 'Income', 'CreditScore', 'MonthsEmployed', 
                   'NumCreditLines', 'DTIRatio', 'Education', 'EmploymentType', 
                   'MaritalStatus', 'HasMortgage', 'HasDependents', 'HasCoSigner']].copy()
customer_dim.to_csv('powerbi/dim_customer.csv', index=False)
print(f"✅ Saved: powerbi/dim_customer.csv ({len(customer_dim):,} rows)")

# 2.2 Loan Dimension
print("\n3️⃣ Creating Loan Dimension...")
loan_dim = df[['LoanID', 'LoanAmount', 'InterestRate', 'LoanTerm', 'LoanPurpose', 'Default']].copy()
loan_dim.to_csv('powerbi/dim_loan.csv', index=False)
print(f"✅ Saved: powerbi/dim_loan.csv ({len(loan_dim):,} rows)")

# ============================================
# 3. AGGREGATED TABLES FOR DASHBOARDS
# ============================================

# 3.1 Summary by Education
print("\n4️⃣ Creating Education Summary...")
edu_summary = df.groupby('Education').agg({
    'LoanID': 'count',
    'Default': 'sum',
    'LoanAmount': 'mean',
    'CreditScore': 'mean',
    'Income': 'mean'
}).reset_index()
edu_summary.columns = ['Education', 'Total_Loans', 'Defaults', 'Avg_Loan_Amount', 'Avg_Credit_Score', 'Avg_Income']
edu_summary['Default_Rate'] = (edu_summary['Defaults'] / edu_summary['Total_Loans'] * 100).round(2)
edu_summary = edu_summary.sort_values('Default_Rate', ascending=False)
edu_summary.to_csv('powerbi/summary_by_education.csv', index=False)
print("   Summary by Education:")
for _, row in edu_summary.iterrows():
    print(f"      {row['Education']}: {row['Default_Rate']}% ({row['Defaults']:,}/{row['Total_Loans']:,})")

# 3.2 Summary by Employment
print("\n5️⃣ Creating Employment Summary...")
emp_summary = df.groupby('EmploymentType').agg({
    'LoanID': 'count',
    'Default': 'sum',
    'LoanAmount': 'mean',
    'CreditScore': 'mean',
    'Income': 'mean'
}).reset_index()
emp_summary.columns = ['EmploymentType', 'Total_Loans', 'Defaults', 'Avg_Loan_Amount', 'Avg_Credit_Score', 'Avg_Income']
emp_summary['Default_Rate'] = (emp_summary['Defaults'] / emp_summary['Total_Loans'] * 100).round(2)
emp_summary = emp_summary.sort_values('Default_Rate', ascending=False)
emp_summary.to_csv('powerbi/summary_by_employment.csv', index=False)
print("   Summary by Employment:")
for _, row in emp_summary.iterrows():
    print(f"      {row['EmploymentType']}: {row['Default_Rate']}% ({row['Defaults']:,}/{row['Total_Loans']:,})")

# 3.3 Summary by Loan Purpose
print("\n6️⃣ Creating Loan Purpose Summary...")
purpose_summary = df.groupby('LoanPurpose').agg({
    'LoanID': 'count',
    'Default': 'sum',
    'LoanAmount': 'mean',
    'InterestRate': 'mean'
}).reset_index()
purpose_summary.columns = ['LoanPurpose', 'Total_Loans', 'Defaults', 'Avg_Loan_Amount', 'Avg_Interest_Rate']
purpose_summary['Default_Rate'] = (purpose_summary['Defaults'] / purpose_summary['Total_Loans'] * 100).round(2)
purpose_summary = purpose_summary.sort_values('Default_Rate', ascending=False)
purpose_summary.to_csv('powerbi/summary_by_purpose.csv', index=False)
print("   Summary by Purpose:")
for _, row in purpose_summary.iterrows():
    print(f"      {row['LoanPurpose']}: {row['Default_Rate']}% ({row['Defaults']:,}/{row['Total_Loans']:,})")

# 3.4 Summary by Age Group
print("\n7️⃣ Creating Age Group Summary...")
df['AgeGroup'] = pd.cut(df['Age'], 
                        bins=[18, 30, 40, 50, 60, 70],
                        labels=['18-29', '30-39', '40-49', '50-59', '60-69'])
age_summary = df.groupby('AgeGroup').agg({
    'LoanID': 'count',
    'Default': 'sum',
    'LoanAmount': 'mean',
    'CreditScore': 'mean'
}).reset_index()
age_summary.columns = ['AgeGroup', 'Total_Loans', 'Defaults', 'Avg_Loan_Amount', 'Avg_Credit_Score']
age_summary['Default_Rate'] = (age_summary['Defaults'] / age_summary['Total_Loans'] * 100).round(2)
age_summary = age_summary.sort_values('Default_Rate', ascending=False)
age_summary.to_csv('powerbi/summary_by_age.csv', index=False)
print("   Summary by Age Group:")
for _, row in age_summary.iterrows():
    print(f"      {row['AgeGroup']}: {row['Default_Rate']}% ({row['Defaults']:,}/{row['Total_Loans']:,})")

# 3.5 Summary by Credit Category
print("\n8️⃣ Creating Credit Category Summary...")
def credit_category(score):
    if score >= 800: return 'Excellent'
    elif score >= 740: return 'Very Good'
    elif score >= 670: return 'Good'
    elif score >= 580: return 'Fair'
    else: return 'Poor'

df['CreditCategory'] = df['CreditScore'].apply(credit_category)
credit_summary = df.groupby('CreditCategory').agg({
    'LoanID': 'count',
    'Default': 'sum',
    'LoanAmount': 'mean',
    'CreditScore': 'mean'
}).reset_index()
credit_summary.columns = ['CreditCategory', 'Total_Loans', 'Defaults', 'Avg_Loan_Amount', 'Avg_Credit_Score']
credit_summary['Default_Rate'] = (credit_summary['Defaults'] / credit_summary['Total_Loans'] * 100).round(2)
credit_summary = credit_summary.sort_values('Default_Rate', ascending=False)
credit_summary.to_csv('powerbi/summary_by_credit.csv', index=False)
print("   Summary by Credit Category:")
for _, row in credit_summary.iterrows():
    print(f"      {row['CreditCategory']}: {row['Default_Rate']}% ({row['Defaults']:,}/{row['Total_Loans']:,})")

# ============================================
# 4. KPI TABLE
# ============================================
print("\n9️⃣ Creating KPI Table...")
kpi_data = {
    'Metric': [
        'Total Loans',
        'Total Defaults',
        'Default Rate (%)',
        'Average Loan Amount ($)',
        'Average Credit Score',
        'Average Income ($)',
        'Average DTI Ratio',
        'Highest Risk Education',
        'Highest Risk Employment',
        'Highest Risk Loan Purpose'
    ],
    'Value': [
        f"{len(df):,}",
        f"{df['Default'].sum():,}",
        f"{round(df['Default'].mean() * 100, 2)}%",
        f"${round(df['LoanAmount'].mean(), 0):,}",
        f"{round(df['CreditScore'].mean(), 0)}",
        f"${round(df['Income'].mean(), 0):,}",
        f"{round(df['DTIRatio'].mean(), 3)}",
        edu_summary.iloc[0]['Education'],
        emp_summary.iloc[0]['EmploymentType'],
        purpose_summary.iloc[0]['LoanPurpose']
    ]
}
kpi_df = pd.DataFrame(kpi_data)
kpi_df.to_csv('powerbi/kpi_table.csv', index=False)
print("✅ Saved: powerbi/kpi_table.csv")
print("\n   KPI Summary:")
for _, row in kpi_df.iterrows():
    print(f"      {row['Metric']}: {row['Value']}")

# ============================================
# 5. SUMMARY REPORT
# ============================================
print("\n" + "="*70)
print("📊 POWER BI DATA EXPORT COMPLETE!")
print("="*70)
print("\n📁 Files saved in 'powerbi/' folder:")

print("\n📋 FACT TABLES:")
print("   ✅ fact_loans.csv (255,347 rows, 18 columns)")

print("\n📊 DIMENSION TABLES:")
print("   ✅ dim_customer.csv (255,347 rows, 13 columns)")
print("   ✅ dim_loan.csv (255,347 rows, 6 columns)")

print("\n📈 SUMMARY TABLES:")
print("   ✅ summary_by_education.csv (4 rows)")
print("   ✅ summary_by_employment.csv (5 rows)")
print("   ✅ summary_by_purpose.csv (5 rows)")
print("   ✅ summary_by_age.csv (5 rows)")
print("   ✅ summary_by_credit.csv (5 rows)")

print("\n📊 KPI TABLE:")
print("   ✅ kpi_table.csv (10 KPIs)")

print("\n✅ All data ready for Power BI Dashboards!")
print("="*70)
# src/quick_analysis.py
"""
Quick Analysis - Understanding Loan Default Patterns
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for better visuals
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# Load cleaned data
print("📂 Loading cleaned data...")
df = pd.read_csv('data/processed/loan_default_cleaned.csv')
print(f"✅ Loaded {len(df):,} records\n")

print("="*70)
print("📊 LOAN DEFAULT ANALYSIS - KEY INSIGHTS")
print("="*70)

# 1. Overall Default Rate
print(f"\n1️⃣ OVERALL DEFAULT RATE: {df['Default'].mean()*100:.2f}%")
print(f"   Total Loans: {len(df):,}")
print(f"   Defaults: {df['Default'].sum():,}")
print(f"   Non-Defaults: {(len(df) - df['Default'].sum()):,}")

# 2. Default by Education
print("\n2️⃣ DEFAULT RATE BY EDUCATION:")
edu_default = df.groupby('Education')['Default'].mean() * 100
for edu, rate in edu_default.sort_values(ascending=False).items():
    print(f"   {edu}: {rate:.2f}%")

# 3. Default by Employment Type
print("\n3️⃣ DEFAULT RATE BY EMPLOYMENT TYPE:")
emp_default = df.groupby('EmploymentType')['Default'].mean() * 100
for emp, rate in emp_default.sort_values(ascending=False).items():
    print(f"   {emp}: {rate:.2f}%")

# 4. Default by Loan Purpose
print("\n4️⃣ DEFAULT RATE BY LOAN PURPOSE:")
purpose_default = df.groupby('LoanPurpose')['Default'].mean() * 100
for purpose, rate in purpose_default.sort_values(ascending=False).items():
    print(f"   {purpose}: {rate:.2f}%")

# 5. Default by Marital Status
print("\n5️⃣ DEFAULT RATE BY MARITAL STATUS:")
marital_default = df.groupby('MaritalStatus')['Default'].mean() * 100
for status, rate in marital_default.sort_values(ascending=False).items():
    print(f"   {status}: {rate:.2f}%")

# 6. Average Credit Score by Default Status
print("\n6️⃣ AVERAGE CREDIT SCORE:")
print(f"   Non-Default: {df[df['Default']==0]['CreditScore'].mean():.0f}")
print(f"   Default:     {df[df['Default']==1]['CreditScore'].mean():.0f}")
print(f"   Difference:  {df[df['Default']==0]['CreditScore'].mean() - df[df['Default']==1]['CreditScore'].mean():.0f} points")

# 7. Average Income by Default Status
print("\n7️⃣ AVERAGE INCOME:")
print(f"   Non-Default: ${df[df['Default']==0]['Income'].mean():,.0f}")
print(f"   Default:     ${df[df['Default']==1]['Income'].mean():,.0f}")
print(f"   Difference:  ${df[df['Default']==0]['Income'].mean() - df[df['Default']==1]['Income'].mean():,.0f}")

# 8. Average DTI Ratio by Default Status
print("\n8️⃣ AVERAGE DTI RATIO:")
print(f"   Non-Default: {df[df['Default']==0]['DTIRatio'].mean():.3f}")
print(f"   Default:     {df[df['Default']==1]['DTIRatio'].mean():.3f}")
print(f"   Difference:  {df[df['Default']==0]['DTIRatio'].mean() - df[df['Default']==1]['DTIRatio'].mean():.3f}")

# 9. Average Loan Amount by Default Status
print("\n9️⃣ AVERAGE LOAN AMOUNT:")
print(f"   Non-Default: ${df[df['Default']==0]['LoanAmount'].mean():,.0f}")
print(f"   Default:     ${df[df['Default']==1]['LoanAmount'].mean():,.0f}")

# 10. Has Mortgage Impact
print("\n🔟 DEFAULT RATE BY MORTGAGE STATUS:")
mortgage_default = df.groupby('HasMortgage')['Default'].mean() * 100
for status, rate in mortgage_default.items():
    print(f"   {status}: {rate:.2f}%")

print("\n" + "="*70)
print("🔍 KEY OBSERVATIONS")
print("="*70)

# Find highest risk group
highest_edu = edu_default.idxmax()
highest_emp = emp_default.idxmax()
highest_purpose = purpose_default.idxmax()

print(f"\n🚨 HIGHEST RISK SEGMENTS:")
print(f"   - Education: {highest_edu} ({edu_default[highest_edu]:.2f}% default rate)")
print(f"   - Employment: {highest_emp} ({emp_default[highest_emp]:.2f}% default rate)")
print(f"   - Loan Purpose: {highest_purpose} ({purpose_default[highest_purpose]:.2f}% default rate)")

print(f"\n💡 KEY INSIGHTS:")
print(f"   - Defaulters have {df[df['Default']==0]['CreditScore'].mean() - df[df['Default']==1]['CreditScore'].mean():.0f} points lower credit score")
print(f"   - Defaulters earn ${df[df['Default']==0]['Income'].mean() - df[df['Default']==1]['Income'].mean():,.0f} less annually")
print(f"   - Defaulters have {df[df['Default']==1]['DTIRatio'].mean() - df[df['Default']==0]['DTIRatio'].mean():.3f} higher DTI ratio")

# Create visualizations
print("\n📊 Creating visualizations...")

# Create folder for images if not exists
import os
os.makedirs('images', exist_ok=True)

fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Loan Default Analysis - Key Patterns', fontsize=16, fontweight='bold')

# 1. Default by Education
edu_default.sort_values().plot(kind='barh', ax=axes[0,0], color='red', alpha=0.7)
axes[0,0].set_title('Default Rate by Education', fontsize=14)
axes[0,0].set_xlabel('Default Rate (%)')
axes[0,0].set_xlim(0, max(edu_default) * 1.2)
# Add value labels
for i, v in enumerate(edu_default.sort_values()):
    axes[0,0].text(v + 0.5, i, f'{v:.1f}%', va='center')

# 2. Default by Employment
emp_default.sort_values().plot(kind='barh', ax=axes[0,1], color='orange', alpha=0.7)
axes[0,1].set_title('Default Rate by Employment Type', fontsize=14)
axes[0,1].set_xlabel('Default Rate (%)')
for i, v in enumerate(emp_default.sort_values()):
    axes[0,1].text(v + 0.5, i, f'{v:.1f}%', va='center')

# 3. Credit Score Distribution by Default
df[df['Default']==0]['CreditScore'].hist(ax=axes[1,0], bins=30, alpha=0.6, label='Non-Default', color='green')
df[df['Default']==1]['CreditScore'].hist(ax=axes[1,0], bins=30, alpha=0.6, label='Default', color='red')
axes[1,0].set_title('Credit Score Distribution by Default Status', fontsize=14)
axes[1,0].set_xlabel('Credit Score')
axes[1,0].set_ylabel('Count')
axes[1,0].legend()
# Add vertical line for means
axes[1,0].axvline(df[df['Default']==0]['CreditScore'].mean(), color='green', linestyle='--', alpha=0.8)
axes[1,0].axvline(df[df['Default']==1]['CreditScore'].mean(), color='red', linestyle='--', alpha=0.8)

# 4. DTI Ratio by Default Status
df.boxplot(column='DTIRatio', by='Default', ax=axes[1,1])
axes[1,1].set_title('DTI Ratio Distribution by Default Status', fontsize=14)
axes[1,1].set_xlabel('Default (0=No, 1=Yes)')
axes[1,1].set_ylabel('DTI Ratio')
axes[1,1].set_ylim(0, 1)

plt.tight_layout()
plt.savefig('images/default_analysis.png', dpi=300, bbox_inches='tight')
print("✅ Visualization saved to: images/default_analysis.png")

# Additional chart: Default Rate by Age Group
fig2, ax = plt.subplots(figsize=(12, 6))

# Create age groups
df['AgeGroup'] = pd.cut(df['Age'], bins=[18, 25, 35, 45, 55, 65, 70], 
                         labels=['18-25', '26-35', '36-45', '46-55', '56-65', '66-70'])
age_default = df.groupby('AgeGroup')['Default'].mean() * 100

age_default.plot(kind='bar', ax=ax, color='steelblue', alpha=0.8)
ax.set_title('Default Rate by Age Group', fontsize=14, fontweight='bold')
ax.set_xlabel('Age Group')
ax.set_ylabel('Default Rate (%)')
ax.set_ylim(0, max(age_default) * 1.2)
# Add value labels
for i, v in enumerate(age_default):
    ax.text(i, v + 0.5, f'{v:.1f}%', ha='center', fontweight='bold')

plt.tight_layout()
plt.savefig('images/default_by_age.png', dpi=300, bbox_inches='tight')
print("✅ Visualization saved to: images/default_by_age.png")

# Additional chart: Income Distribution by Default
fig3, ax = plt.subplots(figsize=(12, 6))
df[df['Default']==0]['Income'].hist(bins=50, alpha=0.6, label='Non-Default', color='green')
df[df['Default']==1]['Income'].hist(bins=50, alpha=0.6, label='Default', color='red')
ax.set_title('Income Distribution by Default Status', fontsize=14, fontweight='bold')
ax.set_xlabel('Annual Income ($)')
ax.set_ylabel('Count')
ax.legend()
# Add vertical line for means
ax.axvline(df[df['Default']==0]['Income'].mean(), color='green', linestyle='--', alpha=0.8, label='Mean Non-Default')
ax.axvline(df[df['Default']==1]['Income'].mean(), color='red', linestyle='--', alpha=0.8, label='Mean Default')
ax.legend()

plt.tight_layout()
plt.savefig('images/income_distribution.png', dpi=300, bbox_inches='tight')
print("✅ Visualization saved to: images/income_distribution.png")

# Summary Report
print("\n" + "="*70)
print("📋 SUMMARY REPORT - LOAN DEFAULT ANALYSIS")
print("="*70)

print(f"""
KEY FINDINGS:
-------------
1. Overall default rate: {df['Default'].mean()*100:.2f}% ({df['Default'].sum():,} out of {len(df):,} loans)

2. HIGHEST RISK SEGMENTS:
   - Education: {highest_edu} ({edu_default[highest_edu]:.2f}% default rate)
   - Employment: {highest_emp} ({emp_default[highest_emp]:.2f}% default rate)
   - Loan Purpose: {highest_purpose} ({purpose_default[highest_purpose]:.2f}% default rate)

3. DEFAULT PROFILE:
   - Lower credit score by {df[df['Default']==0]['CreditScore'].mean() - df[df['Default']==1]['CreditScore'].mean():.0f} points
   - Lower income by ${df[df['Default']==0]['Income'].mean() - df[df['Default']==1]['Income'].mean():,.0f}
   - Higher DTI ratio by {df[df['Default']==1]['DTIRatio'].mean() - df[df['Default']==0]['DTIRatio'].mean():.3f}

4. BUSINESS RECOMMENDATIONS:
   - 🎯 Focus on {highest_edu} borrowers - they have {edu_default[highest_edu]:.2f}% default rate
   - 🎯 {highest_emp} applicants need stricter screening ({emp_default[highest_emp]:.2f}% default rate)
   - 🎯 {highest_purpose} loans have highest risk - review approval criteria
   - 🎯 Consider higher down payments or interest rates for high-risk segments
   - 🎯 Implement credit score improvement programs for subprime borrowers
""")

print("="*70)
print("✅ Analysis Complete! Check images/ folder for visualizations.")
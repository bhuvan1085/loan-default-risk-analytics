# src/eda.py
"""
Exploratory Data Analysis - Deep Dive into Loan Default Patterns
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

print("="*70)
print("🔍 EXPLORATORY DATA ANALYSIS - LOAN DEFAULT DATASET")
print("="*70)

# Load cleaned data
print("\n📂 Loading cleaned data...")
df = pd.read_csv('data/processed/loan_default_cleaned.csv')
print(f"✅ Loaded {len(df):,} records with {len(df.columns)} features")

# Create images folder
import os
os.makedirs('images', exist_ok=True)

# ============================================
# PART 1: Correlation Analysis
# ============================================
print("\n" + "="*70)
print("📊 PART 1: CORRELATION ANALYSIS")
print("="*70)

# Select numeric columns for correlation
numeric_cols = ['Age', 'Income', 'LoanAmount', 'CreditScore', 'MonthsEmployed', 
                'NumCreditLines', 'InterestRate', 'LoanTerm', 'DTIRatio', 'Default']
df_numeric = df[numeric_cols]

# Calculate correlation matrix
correlation_matrix = df_numeric.corr()

print("\n🔗 CORRELATION WITH DEFAULT (Target Variable):")
default_corr = correlation_matrix['Default'].sort_values(ascending=False)
for col, corr in default_corr.items():
    if col != 'Default':
        print(f"   {col}: {corr:.3f}")

# Identify top predictors
print("\n📈 TOP 5 PREDICTORS OF DEFAULT:")
top_predictors = default_corr[default_corr.index != 'Default'].head(5)
for i, (col, corr) in enumerate(top_predictors.items(), 1):
    print(f"   {i}. {col}: {corr:.3f}")

# ============================================
# PART 2: Correlation Heatmap
# ============================================
print("\n📊 Creating correlation heatmap...")

fig, ax = plt.subplots(figsize=(14, 10))
mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
sns.heatmap(correlation_matrix, mask=mask, annot=True, fmt='.2f', 
            cmap='coolwarm', center=0, square=True, 
            linewidths=0.5, ax=ax, cbar_kws={"shrink": 0.8})
ax.set_title('Correlation Matrix - Loan Default Features', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('images/correlation_heatmap.png', dpi=300, bbox_inches='tight')
print("✅ Saved: images/correlation_heatmap.png")

# ============================================
# PART 3: Feature Engineering
# ============================================
print("\n" + "="*70)
print("⚙️ PART 3: FEATURE ENGINEERING")
print("="*70)

# Create new features
print("\n🔧 Creating new features...")

# 1. Credit Score Category
df['CreditCategory'] = pd.cut(df['CreditScore'], 
                               bins=[300, 580, 670, 740, 800, 850],
                               labels=['Poor', 'Fair', 'Good', 'Very Good', 'Excellent'])

# 2. Age Group
df['AgeGroup'] = pd.cut(df['Age'], 
                         bins=[18, 30, 40, 50, 60, 70],
                         labels=['18-29', '30-39', '40-49', '50-59', '60-69'])

# 3. Income Category
df['IncomeCategory'] = pd.cut(df['Income'], 
                               bins=[0, 50000, 75000, 100000, 150000],
                               labels=['Low', 'Lower-Mid', 'Upper-Mid', 'High'])

# 4. DTI Risk Level
df['DTIRisk'] = pd.cut(df['DTIRatio'],
                        bins=[0, 0.3, 0.5, 0.7, 1.0],
                        labels=['Low', 'Medium', 'High', 'Very High'])

# 5. Loan-to-Income Ratio
df['LoanToIncome'] = df['LoanAmount'] / df['Income']

# 6. Credit Score * Income (interaction feature)
df['CreditIncome'] = df['CreditScore'] * df['Income'] / 100000

print("\n📊 New Features Created:")
print(f"   - CreditCategory: {df['CreditCategory'].nunique()} categories")
print(f"   - AgeGroup: {df['AgeGroup'].nunique()} categories")
print(f"   - IncomeCategory: {df['IncomeCategory'].nunique()} categories")
print(f"   - DTIRisk: {df['DTIRisk'].nunique()} categories")
print(f"   - LoanToIncome: (continuous) range {df['LoanToIncome'].min():.2f} - {df['LoanToIncome'].max():.2f}")
print(f"   - CreditIncome: (continuous)")

# ============================================
# PART 4: Analyze New Features
# ============================================
print("\n" + "="*70)
print("📊 PART 4: NEW FEATURE ANALYSIS")
print("="*70)

# 1. Default by Credit Category
print("\n💳 DEFAULT RATE BY CREDIT CATEGORY:")
credit_default = df.groupby('CreditCategory')['Default'].mean() * 100
for cat, rate in credit_default.sort_values(ascending=False).items():
    print(f"   {cat}: {rate:.2f}%")

# 2. Default by Age Group
print("\n👤 DEFAULT RATE BY AGE GROUP:")
age_default = df.groupby('AgeGroup')['Default'].mean() * 100
for age, rate in age_default.sort_values(ascending=False).items():
    print(f"   {age}: {rate:.2f}%")

# 3. Default by Income Category
print("\n💰 DEFAULT RATE BY INCOME CATEGORY:")
income_default = df.groupby('IncomeCategory')['Default'].mean() * 100
for income, rate in income_default.sort_values(ascending=False).items():
    print(f"   {income}: {rate:.2f}%")

# 4. Default by DTI Risk
print("\n📈 DEFAULT RATE BY DTI RISK LEVEL:")
dti_default = df.groupby('DTIRisk')['Default'].mean() * 100
for dti, rate in dti_default.sort_values(ascending=False).items():
    print(f"   {dti}: {rate:.2f}%")

# 5. Average LoanToIncome by Default
print("\n📊 AVERAGE LOAN-TO-INCOME RATIO:")
print(f"   Non-Default: {df[df['Default']==0]['LoanToIncome'].mean():.2f}")
print(f"   Default:     {df[df['Default']==1]['LoanToIncome'].mean():.2f}")
print(f"   Difference:  {df[df['Default']==0]['LoanToIncome'].mean() - df[df['Default']==1]['LoanToIncome'].mean():.2f}")

# ============================================
# PART 5: Advanced Visualizations
# ============================================
print("\n" + "="*70)
print("📊 PART 5: ADVANCED VISUALIZATIONS")
print("="*70)

# 1. Pairplot of top features (sample to avoid slow performance)
print("\n📈 Creating pairplot (sampling 5000 records for performance)...")
df_sample = df.sample(n=min(5000, len(df)), random_state=42)
features_to_plot = ['CreditScore', 'Income', 'DTIRatio', 'LoanAmount', 'Default']
sns.pairplot(df_sample[features_to_plot], hue='Default', diag_kind='kde', 
             palette={0: 'green', 1: 'red'}, plot_kws={'alpha': 0.5})
plt.suptitle('Pairplot - Feature Relationships with Default', y=1.02, fontsize=14, fontweight='bold')
plt.savefig('images/pairplot_features.png', dpi=300, bbox_inches='tight')
print("✅ Saved: images/pairplot_features.png")
plt.close()

# 2. Default Rate by Credit Category (Bar Chart)
fig, ax = plt.subplots(figsize=(10, 6))
colors = ['darkred' if x == credit_default.idxmax() else 'steelblue' for x in credit_default.index]
bars = ax.bar(credit_default.index, credit_default.values, color=colors, alpha=0.8)
ax.set_title('Default Rate by Credit Score Category', fontsize=14, fontweight='bold')
ax.set_xlabel('Credit Category')
ax.set_ylabel('Default Rate (%)')
ax.set_ylim(0, max(credit_default) * 1.2)
for i, v in enumerate(credit_default.values):
    ax.text(i, v + 0.5, f'{v:.1f}%', ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('images/default_by_credit_category.png', dpi=300, bbox_inches='tight')
print("✅ Saved: images/default_by_credit_category.png")
plt.close()

# 3. LoanToIncome Distribution by Default
fig, ax = plt.subplots(figsize=(12, 6))
df[df['Default']==0]['LoanToIncome'].hist(bins=50, alpha=0.6, label='Non-Default', color='green')
df[df['Default']==1]['LoanToIncome'].hist(bins=50, alpha=0.6, label='Default', color='red')
ax.set_title('Loan-to-Income Ratio Distribution by Default Status', fontsize=14, fontweight='bold')
ax.set_xlabel('Loan-to-Income Ratio')
ax.set_ylabel('Count')
ax.legend()
plt.tight_layout()
plt.savefig('images/loan_to_income_distribution.png', dpi=300, bbox_inches='tight')
print("✅ Saved: images/loan_to_income_distribution.png")
plt.close()

# 4. Boxplot - Key Features by Default
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
features = ['CreditScore', 'Income', 'DTIRatio', 'LoanAmount', 'InterestRate', 'LoanTerm']
for i, feature in enumerate(features):
    row, col = i // 3, i % 3
    df.boxplot(column=feature, by='Default', ax=axes[row, col])
    axes[row, col].set_title(f'{feature} by Default Status', fontsize=12)
    axes[row, col].set_xlabel('Default (0=No, 1=Yes)')
plt.suptitle('Feature Distributions by Default Status', y=1.02, fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('images/feature_boxplots.png', dpi=300, bbox_inches='tight')
print("✅ Saved: images/feature_boxplots.png")
plt.close()

# 5. Relationship: Credit Score vs Income colored by Default
fig, ax = plt.subplots(figsize=(12, 8))
scatter = ax.scatter(df['CreditScore'], df['Income'], c=df['Default'], 
                     cmap='RdYlGn_r', alpha=0.4, s=10)
ax.set_title('Credit Score vs Income (Colored by Default)', fontsize=14, fontweight='bold')
ax.set_xlabel('Credit Score')
ax.set_ylabel('Annual Income ($)')
cbar = plt.colorbar(scatter)
cbar.set_label('Default (0=No, 1=Yes)')
# Add horizontal lines for mean income by default
ax.axhline(df[df['Default']==0]['Income'].mean(), color='green', linestyle='--', alpha=0.5, label='Mean Income (Non-Default)')
ax.axhline(df[df['Default']==1]['Income'].mean(), color='red', linestyle='--', alpha=0.5, label='Mean Income (Default)')
ax.legend()
plt.tight_layout()
plt.savefig('images/credit_score_vs_income.png', dpi=300, bbox_inches='tight')
print("✅ Saved: images/credit_score_vs_income.png")
plt.close()

# ============================================
# PART 6: Summary Report
# ============================================
print("\n" + "="*70)
print("📋 EDA SUMMARY REPORT")
print("="*70)

print("\n🔍 KEY FINDINGS FROM EDA:")
print("\n1. TOP PREDICTORS OF DEFAULT (Correlation):")
print(f"   - InterestRate: {default_corr['InterestRate']:.3f}")
print(f"   - LoanAmount: {default_corr['LoanAmount']:.3f}")
print(f"   - NumCreditLines: {default_corr['NumCreditLines']:.3f}")
print(f"   - DTIRatio: {default_corr['DTIRatio']:.3f}")
print(f"   - CreditScore: {default_corr['CreditScore']:.3f}")

print("\n2. HIGHEST RISK SEGMENTS:")
print(f"   - Credit Score: Poor - {credit_default['Poor']:.2f}% default rate")
print(f"   - Age Group: {age_default.idxmax()} - {age_default.max():.2f}% default rate")
print(f"   - Income: Low - {income_default['Low']:.2f}% default rate")
print(f"   - DTI Risk: Very High - {dti_default['Very High']:.2f}% default rate")

print("\n3. KEY INSIGHTS:")
print(f"   - Poor credit score borrowers default at {credit_default['Poor']:.2f}% rate")
print(f"   - Young adults (18-29) show {age_default['18-29']:.2f}% default rate")
print(f"   - Low income borrowers at {income_default['Low']:.2f}% risk")
print(f"   - Very high DTI ratio indicates {dti_default['Very High']:.2f}% default rate")
loan_to_income_ratio = df[df['Default']==1]['LoanToIncome'].mean() / df[df['Default']==0]['LoanToIncome'].mean()
print(f"   - Defaulters have {loan_to_income_ratio:.2f}x higher Loan-to-Income ratio")

print("\n4. RECOMMENDATIONS:")
print("   - 🎯 Implement stricter criteria for 'Poor' credit score applicants")
print("   - 🎯 Review approval process for low-income borrowers")
print("   - 🎯 Monitor DTI ratio closely - set maximum threshold")
print("   - 🎯 Consider age-based risk assessment (18-29 age group at 19.15% risk)")
print("   - 🎯 Reduce loan amounts for high-risk segments")

print("\n" + "="*70)
print("✅ EDA COMPLETE! Check images/ folder for all visualizations.")
print("📁 Visualizations saved:")
print("   - images/correlation_heatmap.png")
print("   - images/pairplot_features.png")
print("   - images/default_by_credit_category.png")
print("   - images/loan_to_income_distribution.png")
print("   - images/feature_boxplots.png")
print("   - images/credit_score_vs_income.png")
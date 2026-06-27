# 🏦 Loan Default Risk Analytics

An end-to-end Data Analytics project using Python, SQL, and Power BI to analyze loan default risk, uncover business insights, and build interactive dashboards for credit risk assessment.

---

## 📊 Project Overview

This project analyzes **255,000+ loan records** to identify patterns in loan defaults, understand customer risk profiles, and provide actionable business insights through interactive dashboards.

### 🎯 Business Problem
Banks and financial institutions lose billions annually due to loan defaults. This project helps:
- **Identify** high-risk customer segments
- **Understand** factors contributing to defaults
- **Enable** data-driven lending decisions
- **Reduce** financial losses through early intervention

---

## 🛠️ Tech Stack

| Category | Tools & Libraries |
|----------|------------------|
| **Data Processing** | Python, Pandas, NumPy |
| **Data Visualization** | Matplotlib, Seaborn |
| **Database** | SQL (SQLite/PostgreSQL) |
| **BI & Dashboard** | Power BI, DAX |
| **Version Control** | Git, GitHub |

---

## 📁 Project Structure
loan-default-risk-analytics/
│
├── data/
│ ├── raw/ # Original dataset (255K+ records)
│ │ └── loan_default.csv
│ └── processed/ # Cleaned and transformed data
│ └── loan_default_cleaned.csv
│
├── src/ # Python scripts
│ ├── data_loader.py # Load and explore data
│ ├── data_cleaner.py # Data cleaning functions
│ └── eda.py # Exploratory analysis
│
├── sql/ # SQL queries
│ └── analysis_queries.sql # Business analysis queries
│
├── powerbi/ # Power BI files
│ └── loan_default_dashboard.pbix
│
├── images/ # Dashboard screenshots
│ └── dashboard_preview.png
│
├── docs/ # Documentation
│ └── data_dictionary.md # Column descriptions
│
├── config.py # Configuration settings
├── main.py # Main execution pipeline
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore file
└── README.md # Project documentation

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Git (for version control)
- Power BI Desktop (for dashboards)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/bhuvan1085/loan-default-risk-analytics.git
cd loan-default-risk-analytics
# 🏦 Loan Default Risk Analytics

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-green.svg)](https://pandas.pydata.org/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Desktop-yellow.svg)](https://powerbi.microsoft.com/)
[![SQL](https://img.shields.io/badge/SQL-SQLite%2FPostgreSQL-orange.svg)](https://www.sqlite.org/)

An end-to-end Data Analytics project using **Python, SQL, and Power BI** to analyze loan default risk, uncover business insights, and build interactive dashboards for credit risk assessment.

---

## 📊 Project Overview

This project analyzes **255,000+ loan records** to identify patterns in loan defaults, understand customer risk profiles, and provide actionable business insights through interactive dashboards.

### 🎯 Business Problem
Banks and financial institutions lose billions annually due to loan defaults. This project helps:
- **Identify** high-risk customer segments
- **Understand** factors contributing to defaults
- **Enable** data-driven lending decisions
- **Reduce** financial losses through early intervention

### 📈 Key Metrics Tracked
| Metric | Description |
|--------|-------------|
| **Default Rate** | Percentage of loans that defaulted |
| **Average Loan Amount** | Mean loan value across all customers |
| **Average Credit Score** | Mean credit score of borrowers |
| **Recovery Rate** | Percentage of defaulted loans recovered |
| **Risk Segmentation** | Customer groups by risk level |

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
│ └── eda.py # Exploratory analysis (coming soon)
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
git clone https://github.com/yourusername/loan-default-risk-analytics.git
cd loan-default-risk-analytics
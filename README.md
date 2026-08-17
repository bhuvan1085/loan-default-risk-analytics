# 🏦 Loan Default Risk Analytics

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Desktop-yellow.svg)](https://powerbi.microsoft.com/)
[![SQL](https://img.shields.io/badge/SQL-SQLite-orange.svg)](https://www.sqlite.org/)
[![Git](https://img.shields.io/badge/Git-Version%20Control-red.svg)](https://git-scm.com/)

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
| **Database** | SQL (SQLite) |
| **BI & Dashboard** | Power BI, DAX |
| **Version Control** | Git, GitHub |

---

## 📁 Project Structure
loan-default-risk-analytics/
│
├── data/
│ ├── raw/ # Original dataset (255K+ records)
│ └── processed/ # Cleaned and transformed data
│
├── powerbi/ # Power BI data files
│ ├── fact_loans.csv # Main transaction data (255K rows)
│ ├── dim_customer.csv # Customer details
│ ├── dim_loan.csv # Loan details
│ ├── summary_by_*.csv # 5 summary tables
│ └── kpi_table.csv # Business KPIs
│
├── sql/ # SQL queries
│ └── analysis_queries.sql # 15+ business queries
│
├── src/ # Python scripts
│ ├── data_loader.py # Load and explore data
│ ├── data_cleaner.py # Data cleaning functions
│ ├── eda.py # Exploratory analysis
│ ├── sql_setup.py # SQL database setup
│ ├── sql_analysis.py # SQL analysis execution
│ └── export_for_powerbi.py # Power BI data export
│
├── images/ # Dashboard screenshots
│ ├── executive_dashboard.png
│ ├── risk_analysis.png
│ ├── loan_analytics.png
│ ├── customer_insights.png
│ └── whatif_analysis.png
│
├── docs/ # Documentation
│ └── data_dictionary.md # Column descriptions
│
├── config.py
├── main.py
├── loan_default.db # SQLite database
├── requirements.txt
├── README.md
└── .gitignore

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
2.Create and activate virtual environment
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
Install dependencies

pip install -r requirements.txt
Run the data pipeline


python main.py
Run SQL analysis

python src/sql_analysis.py
Open Power BI Dashboard
Open powerbi/loan_default_dashboard.pbix
Connect to your data source

📅 Project Timeline
Week 1: Data Pipeline & EDA
Day	Task	Status
Day 1	Project Setup & Data Pipeline	✅ COMPLETE
Day 2	Data Understanding & Quick Analysis	✅ COMPLETE
Day 3	Exploratory Data Analysis (EDA)	✅ COMPLETE
Deliverables: 255K records cleaned, 6+ visualizations, data dictionary

Week 2: SQL & Power BI Data Prep
Day	Task	Status
Day 4	SQL Database Setup & Analysis	✅ COMPLETE
Day 5	Power BI Data Preparation	✅ COMPLETE
Deliverables: SQL database with 15+ queries, fact and dimension tables exported

Week 3: Power BI Dashboards
Day	Task	Status
Day 6	Power BI Dashboards & Formatting	✅ COMPLETE
Deliverables: 5 interactive dashboards, 20+ DAX measures, What-If analysis

Week 4: Final Polish & Deployment
Day	Task	Status
Day 7	Documentation, Screenshots & GitHub	✅ COMPLETE
📊 Dashboard Previews
Executive Dashboard
https://images/executive_dashboard.png

Risk Analysis Dashboard
https://images/risk_analysis.png

Loan Analytics Dashboard
https://images/loan_analytics.png

Customer Insights Dashboard
https://images/customer_insights.png

What-If Analysis Dashboard
https://images/whatif_analysis.png

📈 Key Insights
Metric	Value
Overall Default Rate	11.61%
Highest Risk Education	High School (12.88%)
Highest Risk Employment	Unemployed (13.55%)
Highest Risk Loan Purpose	Business (12.33%)
Highest Risk Age Group	18-29 (19.15%)
Average Credit Score (Defaulters)	559
Average Credit Score (Non-Defaulters)	576
Average Income (Defaulters)	$71,845
Average Income (Non-Defaulters)	$83,899
🔍 Sample SQL Queries
sql
-- Overall Default Rate
SELECT 
    COUNT(*) as total_loans,
    SUM(Default) as total_defaults,
    ROUND(CAST(SUM(Default) AS FLOAT) / COUNT(*) * 100, 2) as default_rate
FROM loan_data;

-- Default Rate by Education
SELECT 
    Education,
    COUNT(*) as total_loans,
    SUM(Default) as defaults,
    ROUND(CAST(SUM(Default) AS FLOAT) / COUNT(*) * 100, 2) as default_rate
FROM loan_data
GROUP BY Education
ORDER BY default_rate DESC;
🎯 Future Improvements
□ Deploy dashboard to Power BI Service
□ Add machine learning model for default prediction
□ Build automated email reports
□ Connect to live database
□ Add more data sources (external economic indicators)

👤 Author-Bhuvan

🐙 GitHub: github.com/bhuvan1085
⭐ Support
If you found this project useful, please give it a ⭐ on GitHub!
📝 License
This project is for educational and portfolio purposes.



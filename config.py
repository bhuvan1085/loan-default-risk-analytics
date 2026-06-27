# config.py
import os
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent
DATA_RAW_DIR = BASE_DIR / "data" / "raw"
DATA_PROCESSED_DIR = BASE_DIR / "data" / "processed"
SRC_DIR = BASE_DIR / "src"
SQL_DIR = BASE_DIR / "sql"
POWERBI_DIR = BASE_DIR / "powerbi"
IMAGES_DIR = BASE_DIR / "images"

# File paths
RAW_DATA_PATH = DATA_RAW_DIR / "loan_default.csv"
PROCESSED_DATA_PATH = DATA_PROCESSED_DIR / "loan_default_cleaned.csv"

# Create directories if they don't exist
for dir_path in [DATA_RAW_DIR, DATA_PROCESSED_DIR, SRC_DIR, SQL_DIR, POWERBI_DIR, IMAGES_DIR]:
    dir_path.mkdir(parents=True, exist_ok=True)

# Column categories (we'll refine these)
TARGET_COLUMN = "Default"
NUMERIC_COLUMNS = ["Age", "Income", "LoanAmount", "CreditScore", "MonthsEmployed", 
                   "NumCreditLines", "InterestRate", "DTIRatio"]
CATEGORICAL_COLUMNS = ["Education", "EmploymentType", "MaritalStatus", "HasMortgage", 
                       "HasDependents", "LoanPurpose", "HasCoSigner"]
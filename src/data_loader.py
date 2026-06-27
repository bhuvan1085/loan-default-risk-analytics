# src/data_loader.py
import pandas as pd
import sys
from pathlib import Path

# Add parent directory to path to import config
sys.path.append(str(Path(__file__).resolve().parent.parent))
import config

def load_data():
    """Load the raw loan dataset"""
    try:
        df = pd.read_csv(config.RAW_DATA_PATH)
        print(f"✅ Data loaded successfully!")
        print(f"📊 Shape: {df.shape[0]:,} rows, {df.shape[1]} columns")
        return df
    except FileNotFoundError:
        print(f"❌ File not found at {config.RAW_DATA_PATH}")
        print("📌 Please place your CSV file in: data/raw/ folder")
        return None
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None

def get_data_info(df):
    """Print data information"""
    print("\n" + "="*50)
    print("📋 DATA INFO")
    print("="*50)
    
    print(f"\n📊 Shape: {df.shape[0]:,} rows, {df.shape[1]} columns")
    print(f"\n📝 Columns ({len(df.columns)} total):")
    for i, col in enumerate(df.columns, 1):
        print(f"   {i}. {col}")
    
    print(f"\n🔢 Data Types:")
    print(df.dtypes)
    
    print(f"\n📈 Missing Values:")
    missing = df.isnull().sum()
    if missing.sum() > 0:
        print(missing[missing > 0])
    else:
        print("✅ No missing values found!")
    
    print(f"\n📊 Basic Statistics:")
    print(df.describe())

def preview_data(df, n=5):
    """Preview first n rows"""
    print(f"\n📄 First {n} rows:")
    print("="*50)
    print(df.head(n).to_string())

def check_duplicates(df):
    """Check for duplicate rows"""
    duplicates = df.duplicated().sum()
    print(f"\n🔍 Duplicate rows: {duplicates:,}")
    return duplicates

if __name__ == "__main__":
    # Test the loader
    df = load_data()
    if df is not None:
        get_data_info(df)
        preview_data(df)
        check_duplicates(df)
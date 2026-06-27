# src/data_cleaner.py
import pandas as pd
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
import config

def clean_data(df):
    """
    Main cleaning function - builds step by step
    """
    print("\n🧹 STARTING DATA CLEANING")
    print("="*50)
    
    # Make a copy
    df_clean = df.copy()
    initial_shape = df_clean.shape
    
    # 1. Remove duplicates
    print("\n1️⃣ Removing duplicates...")
    duplicates = df_clean.duplicated().sum()
    df_clean = df_clean.drop_duplicates()
    print(f"   Removed {duplicates:,} duplicate rows")
    
    # 2. Check missing values
    print("\n2️⃣ Checking missing values...")
    missing = df_clean.isnull().sum()
    if missing.sum() > 0:
        print(f"   Missing values found in columns:")
        print(missing[missing > 0])
    else:
        print("   ✅ No missing values!")
    
    # 3. Check data types
    print("\n3️⃣ Checking data types...")
    print(f"   Object columns: {df_clean.select_dtypes(include=['object']).columns.tolist()}")
    
    final_shape = df_clean.shape
    print(f"\n📊 Shape change: {initial_shape[0]:,} → {final_shape[0]:,} rows")
    
    return df_clean

def save_cleaned_data(df):
    """Save cleaned data to processed folder"""
    output_path = config.PROCESSED_DATA_PATH
    df.to_csv(output_path, index=False)
    print(f"\n💾 Cleaned data saved to: {output_path}")
    print(f"📊 Final shape: {df.shape[0]:,} rows, {df.shape[1]} columns")

if __name__ == "__main__":
    # Test the cleaner
    print("📂 Loading raw data...")
    import data_loader
    df = data_loader.load_data()
    
    if df is not None:
        df_clean = clean_data(df)
        print("\n✅ Cleaning completed!")
        save_cleaned_data(df_clean)
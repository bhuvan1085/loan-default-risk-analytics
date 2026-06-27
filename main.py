# main.py
"""
Loan Default Risk Analytics Pipeline
Run this file to execute the entire analysis pipeline
"""

import sys
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).resolve().parent / "src"))

from data_loader import load_data, get_data_info, preview_data, check_duplicates
from data_cleaner import clean_data, save_cleaned_data

def main():
    print("🏦 LOAN DEFAULT RISK ANALYTICS PIPELINE")
    print("="*60)
    
    # Step 1: Load data
    print("\n📂 STEP 1: Loading Data")
    print("-"*40)
    df = load_data()
    
    if df is None:
        print("❌ Pipeline failed at Step 1")
        return
    
    # Step 2: Explore data
    print("\n🔍 STEP 2: Data Exploration")
    print("-"*40)
    get_data_info(df)
    preview_data(df)
    duplicates = check_duplicates(df)
    
    # Step 3: Clean data
    print("\n🧹 STEP 3: Data Cleaning")
    print("-"*40)
    df_clean = clean_data(df)
    
    # Step 4: Save cleaned data
    print("\n💾 STEP 4: Saving Processed Data")
    print("-"*40)
    save_cleaned_data(df_clean)
    
    print("\n✅ PIPELINE COMPLETED SUCCESSFULLY!")
    print("="*60)

if __name__ == "__main__":
    main()
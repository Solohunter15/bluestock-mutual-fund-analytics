import os
import pandas as pd
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.join(SCRIPT_DIR, "data", "raw")
PROCESSED_DIR = os.path.join(SCRIPT_DIR, "data", "processed")
os.makedirs(PROCESSED_DIR, exist_ok=True)

def clean_fund_master():
    print("Cleaning 01_fund_master.csv...")
    path = os.path.join(RAW_DIR, "01_fund_master.csv")
    df = pd.read_csv(path)
    
    # Check duplicates & drop
    df = df.drop_duplicates(subset=["amfi_code"])
    
    # Save
    out_path = os.path.join(PROCESSED_DIR, "01_fund_master.csv")
    df.to_csv(out_path, index=False)
    print(f"Saved cleaned Fund Master: {df.shape} to {out_path}\n")

def clean_nav_history():
    print("Cleaning 02_nav_history.csv...")
    path = os.path.join(RAW_DIR, "02_nav_history.csv")
    df = pd.read_csv(path)
    
    # Parse dates
    df["date"] = pd.to_datetime(df["date"])
    
    # Validate NAV > 0
    df = df[df["nav"] > 0]
    
    # Remove duplicate records
    df = df.drop_duplicates(subset=["amfi_code", "date"])
    
    # Forward-fill weekends/holidays per amfi_code
    cleaned_navs = []
    
    for code, group in df.groupby("amfi_code"):
        # Sort by date
        group = group.sort_values("date")
        
        # Set date index
        group = group.set_index("date")
        
        # Create complete date range from min to max date
        min_date = group.index.min()
        max_date = group.index.max()
        all_dates = pd.date_range(start=min_date, end=max_date, freq="D")
        
        # Reindex and forward-fill
        group = group.reindex(all_dates)
        group["amfi_code"] = code
        group["nav"] = group["nav"].ffill()
        
        # Reset index
        group = group.reset_index().rename(columns={"index": "date"})
        cleaned_navs.append(group)
        
    df_cleaned = pd.concat(cleaned_navs, ignore_index=True)
    
    # Format date back to string
    df_cleaned["date"] = df_cleaned["date"].dt.strftime("%Y-%m-%d")
    
    # Save
    out_path = os.path.join(PROCESSED_DIR, "02_nav_history.csv")
    df_cleaned.to_csv(out_path, index=False)
    print(f"Saved forward-filled NAV history: {df_cleaned.shape} to {out_path}\n")

def clean_investor_transactions():
    print("Cleaning 08_investor_transactions.csv...")
    path = os.path.join(RAW_DIR, "08_investor_transactions.csv")
    df = pd.read_csv(path)
    
    # Parse dates
    df["transaction_date"] = pd.to_datetime(df["transaction_date"]).dt.strftime("%Y-%m-%d")
    
    # Standardise transaction types
    type_map = {
        "sip": "SIP",
        "SIP": "SIP",
        "lumpsum": "Lumpsum",
        "Lumpsum": "Lumpsum",
        "redemption": "Redemption",
        "Redemption": "Redemption"
    }
    df["transaction_type"] = df["transaction_type"].map(type_map).fillna("SIP")
    
    # Validate amount > 0
    df = df[df["amount_inr"] > 0]
    
    # Standardise KYC status
    kyc_map = {
        "verified": "Verified",
        "Verified": "Verified",
        "pending": "Pending",
        "Pending": "Pending"
    }
    df["kyc_status"] = df["kyc_status"].map(kyc_map).fillna("Verified")
    
    # Save
    out_path = os.path.join(PROCESSED_DIR, "08_investor_transactions.csv")
    df.to_csv(out_path, index=False)
    print(f"Saved cleaned Transactions: {df.shape} to {out_path}\n")

def clean_scheme_performance():
    print("Cleaning 07_scheme_performance.csv...")
    path = os.path.join(RAW_DIR, "07_scheme_performance.csv")
    df = pd.read_csv(path)
    
    # Ensure numeric types
    for col in ["return_1yr_pct", "return_3yr_pct", "return_5yr_pct", "benchmark_3yr_pct", "alpha", "beta", "sharpe_ratio", "sortino_ratio", "expense_ratio_pct"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        
    # Check expense_ratio range (0.1% to 2.5%)
    invalid_expense = df[(df["expense_ratio_pct"] < 0.1) | (df["expense_ratio_pct"] > 2.5)]
    if len(invalid_expense) > 0:
        print(f"[WARNING] Found {len(invalid_expense)} records with expense ratio out of bounds (0.1% - 2.5%).")
        
    # Save
    out_path = os.path.join(PROCESSED_DIR, "07_scheme_performance.csv")
    df.to_csv(out_path, index=False)
    print(f"Saved cleaned Scheme Performance: {df.shape} to {out_path}\n")

def copy_clean_others():
    others = [
        "03_aum_by_fund_house.csv",
        "04_monthly_sip_inflows.csv",
        "05_category_inflows.csv",
        "06_industry_folio_count.csv",
        "09_portfolio_holdings.csv",
        "10_benchmark_indices.csv"
    ]
    
    for filename in others:
        print(f"Processing and copying {filename}...")
        path = os.path.join(RAW_DIR, filename)
        df = pd.read_csv(path)
        
        # Check nulls or other types
        if filename == "04_monthly_sip_inflows.csv":
            df["yoy_growth_pct"] = df["yoy_growth_pct"].fillna(0.0)
            
        out_path = os.path.join(PROCESSED_DIR, filename)
        df.to_csv(out_path, index=False)
        print(f"Saved {filename}: {df.shape} to {out_path}\n")

def main():
    print("=" * 60)
    print("STARTING DAY 2 DATA CLEANING & ETL PIPELINE")
    print("=" * 60)
    
    clean_fund_master()
    clean_nav_history()
    clean_investor_transactions()
    clean_scheme_performance()
    copy_clean_others()
    
    print("=" * 60)
    print("DATA CLEANING COMPLETE. All 10 cleaned CSVs saved in data/processed/.")
    print("=" * 60)

if __name__ == "__main__":
    main()

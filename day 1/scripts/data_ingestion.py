import os
import pandas as pd
from datetime import datetime

# Paths setup
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DAY_ROOT = os.path.dirname(SCRIPT_DIR)
RAW_DIR = os.path.join(DAY_ROOT, "data", "raw")
os.makedirs(RAW_DIR, exist_ok=True)

CSV_FILES = [
    "01_fund_master.csv", "02_nav_history.csv", "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv", "05_category_inflows.csv", "06_industry_folio_count.csv",
    "07_scheme_performance.csv", "08_investor_transactions.csv", "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

def load_and_inspect_datasets():
    print("LOADING AND INSPECTING DATASETS")
    anomalies = {}
    for filename in CSV_FILES:
        path = os.path.join(RAW_DIR, filename)
        if not os.path.exists(path):
            print(f"File missing: {filename}")
            continue
        try:
            df = pd.read_csv(path)
            print(f"FILE: {filename} - Shape: {df.shape}")
        except Exception as e:
            print(f"Error loading {filename}: {e}")
            
def main():
    load_and_inspect_datasets()

if __name__ == '__main__':
    main()

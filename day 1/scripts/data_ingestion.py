"""
Bluestock Mutual Fund Analytics Platform - Ingestion & Inspection
Loads all 10 raw CSV datasets, inspects shapes/dtypes, and audits anomalies.
"""
import os
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
RAW_DIR = os.path.join(PROJECT_ROOT, "data", "raw")

CSV_FILES = [
    "01_fund_master.csv", "02_nav_history.csv", "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv", "05_category_inflows.csv", "06_industry_folio_count.csv",
    "07_scheme_performance.csv", "08_investor_transactions.csv", "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

def load_and_inspect():
    print("=" * 60)
    print("DAY 1: LOADING AND INSPECTING DATASETS")
    print("=" * 60)
    for filename in CSV_FILES:
        path = os.path.join(RAW_DIR, filename)
        if not os.path.exists(path):
            print(f"File {filename} not found.")
            continue
        df = pd.read_csv(path)
        print(f"\nFILE: {filename}")
        print(f"Shape: {df.shape}")
        print("Dtypes:")
        print(df.dtypes)
        print("Head Preview:")
        print(df.head(2))

if __name__ == "__main__":
    load_and_inspect()

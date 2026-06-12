import os
import pandas as pd
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DAY_ROOT = os.path.dirname(SCRIPT_DIR)
RAW_DIR = os.path.join(DAY_ROOT, "data", "raw")
PROCESSED_DIR = os.path.join(DAY_ROOT, "data", "processed")
os.makedirs(PROCESSED_DIR, exist_ok=True)

def clean_fund_master():
    path = os.path.join(RAW_DIR, "01_fund_master.csv")
    if os.path.exists(path):
        df = pd.read_csv(path)
        df = df.drop_duplicates(subset=["amfi_code"])
        df.to_csv(os.path.join(PROCESSED_DIR, "01_fund_master.csv"), index=False)
        print("Cleaned Fund Master.")

def clean_nav_history():
    path = os.path.join(RAW_DIR, "02_nav_history.csv")
    if os.path.exists(path):
        df = pd.read_csv(path)
        df["date"] = pd.to_datetime(df["date"])
        df = df[df["nav"] > 0]
        df = df.drop_duplicates(subset=["amfi_code", "date"])
        cleaned_navs = []
        for code, group in df.groupby("amfi_code"):
            group = group.sort_values("date").set_index("date")
            all_dates = pd.date_range(start=group.index.min(), end=group.index.max(), freq="D")
            group = group.reindex(all_dates)
            group["amfi_code"] = code
            group["nav"] = group["nav"].ffill()
            cleaned_navs.append(group.reset_index().rename(columns={"index": "date"}))
        df_cleaned = pd.concat(cleaned_navs, ignore_index=True)
        df_cleaned["date"] = df_cleaned["date"].dt.strftime("%Y-%m-%d")
        df_cleaned.to_csv(os.path.join(PROCESSED_DIR, "02_nav_history.csv"), index=False)
        print("Cleaned NAV history.")

def main():
    clean_fund_master()
    clean_nav_history()

if __name__ == '__main__':
    main()

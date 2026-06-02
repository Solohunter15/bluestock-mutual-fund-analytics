import os
import sqlite3
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, "bluestock_mf.db")
SCHEMA_PATH = os.path.join(SCRIPT_DIR, "schema.sql")
PROCESSED_DIR = os.path.join(SCRIPT_DIR, "data", "processed")

def execute_ddl():
    print("Executing schema DDL script to create tables...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    with open(SCHEMA_PATH, "r") as f:
        sql_script = f.read()
        
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()
    print("Database tables and indexes created successfully.\n")

def populate_date_dimension():
    print("Generating and populating dim_date table...")
    # Generate dates from 2022-01-01 to 2026-12-31
    dates = pd.date_range(start="2022-01-01", end="2026-12-31", freq="D")
    df_date = pd.DataFrame({"date": dates})
    
    df_date["year"] = df_date["date"].dt.year
    df_date["month"] = df_date["date"].dt.month
    df_date["quarter"] = df_date["date"].dt.quarter
    # Dayofweek is 0-6 (Mon-Sun), weekdays are 0-4
    df_date["is_weekday"] = (df_date["date"].dt.dayofweek < 5).astype(int)
    
    # Format date as YYYY-MM-DD
    df_date["date"] = df_date["date"].dt.strftime("%Y-%m-%d")
    
    conn = sqlite3.connect(DB_PATH)
    df_date.to_sql("dim_date", conn, if_exists="append", index=False)
    conn.close()
    print(f"Generated and loaded {len(df_date)} rows into dim_date.\n")

def load_table(csv_name, table_name, mapping=None):
    csv_path = os.path.join(PROCESSED_DIR, csv_name)
    if not os.path.exists(csv_path):
        print(f"File {csv_name} not found, skipping.")
        return
        
    df = pd.read_csv(csv_path)
    
    if mapping:
        df = df.rename(columns=mapping)
        
    # Standardise column list based on schema
    conn = sqlite3.connect(DB_PATH)
    
    # Get columns from table
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name})")
    cols = [col[1] for col in cursor.fetchall()]
    
    # Keep only columns defined in the table (excluding AUTOINCREMENT tx_id)
    df_load = df[[c for c in df.columns if c in cols]]
    
    df_load.to_sql(table_name, conn, if_exists="append", index=False)
    
    # Fetch row count
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    db_count = cursor.fetchone()[0]
    conn.close()
    
    print(f"Loaded {csv_name} -> {table_name}: CSV rows={len(df)}, DB table rows={db_count}")

def main():
    print("=" * 60)
    print("STARTING DAY 2 DATABASE LOADING PIPELINE (SQLite)")
    print("=" * 60)
    
    # Delete old database if exists to ensure clean run
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print("Removed existing bluestock_mf.db to establish a clean instance.")
        
    execute_ddl()
    populate_date_dimension()
    
    # Load 1: dim_fund
    load_table("01_fund_master.csv", "dim_fund")
    
    # Load 2: fact_nav
    load_table("02_nav_history.csv", "fact_nav")
    
    # Load 3: fact_transactions
    load_table("08_investor_transactions.csv", "fact_transactions")
    
    # Load 4: fact_performance
    load_table("07_scheme_performance.csv", "fact_performance")
    
    # Load 5: fact_aum
    load_table("03_aum_by_fund_house.csv", "fact_aum")
    
    # Load 6: fact_portfolio
    load_table("09_portfolio_holdings.csv", "fact_portfolio")
    
    # Load 7: fact_sip_industry
    load_table("04_monthly_sip_inflows.csv", "fact_sip_industry")
    
    print("=" * 60)
    print("DATABASE LOADING COMPLETE. bluestock_mf.db loaded cleanly!")
    print("=" * 60)

if __name__ == "__main__":
    main()

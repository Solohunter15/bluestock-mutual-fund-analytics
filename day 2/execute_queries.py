import os
import sqlite3
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, "bluestock_mf.db")
QUERIES_PATH = os.path.join(SCRIPT_DIR, "queries.sql")

def run_queries():
    conn = sqlite3.connect(DB_PATH)
    
    with open(QUERIES_PATH, "r") as f:
        sql_content = f.read()
        
    # Split queries by semicolon
    queries = [q.strip() for q in sql_content.split(";") if q.strip()]
    
    # 10 Query Titles
    titles = [
        "1. Top 5 Funds by AUM",
        "2. Average NAV per Month for SBI Bluechip Fund (119551)",
        "3. Monthly SIP Inflow and YoY Growth (Industry Trend)",
        "4. Transactions Count and Total Amount in Rs. Grouped by State",
        "5. Funds with Expense Ratio < 1.0% in Direct Plan",
        "6. Unique Count of Investors by City Tier (T30 vs B30)",
        "7. Total Transaction Amount by Gender and Age Group",
        "8. Sector Allocation Summary Across All Portfolio Holdings",
        "9. Average Annualised 3yr Return and Sharpe Ratio by Fund Category",
        "10. Net Transaction Cash Flow (Total Inflows - Total Redemptions) per Fund Category"
    ]
    
    for idx, (title, query) in enumerate(zip(titles, queries)):
        print("\n" + "=" * 80)
        print(title)
        print("=" * 80)
        
        try:
            df = pd.read_sql_query(query, conn)
            # Formatting options for large tables
            pd.set_option('display.max_columns', None)
            pd.set_option('display.width', 1000)
            
            if df.empty:
                print("No results returned.")
            else:
                # Format numbers with commas where applicable
                for col in df.columns:
                    if "amount" in col.lower() or "inflows" in col.lower() or "outflows" in col.lower() or "cash_flow" in col.lower():
                        df[col] = df[col].apply(lambda x: f"{x:,.0f}" if isinstance(x, (int, float, np.integer)) else x)
                print(df.to_string(index=False))
        except Exception as e:
            print(f"Error executing query: {e}")
            
    conn.close()

if __name__ == "__main__":
    import numpy as np
    run_queries()

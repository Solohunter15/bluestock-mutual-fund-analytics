import os
import sqlite3
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DAY_ROOT = os.path.dirname(SCRIPT_DIR)
DB_PATH = os.path.join(DAY_ROOT, "data", "db", "bluestock_mf.db")
SCHEMA_PATH = os.path.join(DAY_ROOT, "sql", "schema.sql")
PROCESSED_DIR = os.path.join(DAY_ROOT, "data", "processed")

def execute_ddl():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    with open(SCHEMA_PATH, "r") as f:
        sql = f.read()
    cursor.executescript(sql)
    conn.commit()
    conn.close()
    print("Database tables created.")

def main():
    if os.path.exists(SCHEMA_PATH):
        execute_ddl()

if __name__ == '__main__':
    main()

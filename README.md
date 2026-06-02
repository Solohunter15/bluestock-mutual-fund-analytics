# Mutual Fund Analytics Platform 📈
### End-to-End Data Engineering & ETL Pipeline — Bluestock Capstone Project

Welcome to the **Mutual Fund Analytics Platform** Capstone Project repository, developed as part of the Bluestock Fintech Internship program. 

This repository leverages a clean **Monorepo Structure** to organize the end-to-end development of a financial analytics platform that ingests, cleans, stores, analyzes, and visualizes Indian Mutual Fund datasets.

---

## 📁 7-Day Monorepo Folder Structure

The repository is structured as a progressive daily monorepo. Each day's work is self-contained within its respective folder:

```text
bluestock-mutual-fund-analytics/
│
├── .git/
├── .gitignore
├── requirements.txt            # Unified project dependencies
├── README.md                   # Master repository documentation (You are here)
│
├── day 1/                      # Day 1: Project Setup + Data Ingestion (ETL)
│   ├── data_ingestion.py       # Local ETL bootstrapping, loading, & validation pipeline
│   ├── live_nav_fetch.py       # Live daily NAV fetcher from mfapi.in
│   ├── sql/                    # PostgreSQL DDL staging queries
│   ├── dashboard/              # Staging directory for dashboard assets
│   ├── notebooks/              # Jupyter research environment
│   ├── reports/                # Day 1 data quality reports & Word generator
│   └── README.md               # Day 1 documentation & workflows
│
└── day 2/                      # Day 2: Data Cleaning + SQLite Database Design
    ├── data/                   # Self-contained Day 2 data directory
    │   ├── raw/                # Raw source datasets (CSVs + Scraped JSONs)
    │   └── processed/          # Downstream validated & forward-filled CSVs
    ├── schema.sql              # Star Schema relational DDL (facts and dimensions)
    ├── queries.sql             # 10 comprehensive analytical SQL queries
    ├── db_loader.py            # SQLite database creation & insertion script
    ├── execute_queries.py      # Automated SQL execution harness
    ├── data_dictionary.md      # Database column reference and business definitions
    └── bluestock_mf.db         # Loaded SQLite database instance (~10.5 MB)
```

---

## 🚀 Progressive Project Roadmap

### 📅 [Day 1: Project Setup + Data Ingestion](file:///c:/Users/jibum/OneDrive/Desktop/Bluestock%20Internship/day%201/README.md)
*   **ETL Bootstrap Ingestion:** Completed local python pipeline in `day 1/data_ingestion.py` that auto-generates raw dataset structures and audits file metrics.
*   **Live NAV Fetcher:** Real-time JSON parser in `day 1/live_nav_fetch.py` scraping historical NAVs for 6 core mutual fund schemes directly from the public AMFI REST API (`mfapi.in`).
*   **Quality Reports:** Comprehensive data quality and referential integrity audit generated in `day 1/reports/day1_data_quality_summary.md`.

### 📅 [Day 2: Data Cleaning + SQLite DB Design](file:///c:/Users/jibum/OneDrive/Desktop/Bluestock%20Internship/day%202/data_dictionary.md)
*   **Robust Data Cleaning:** Implemented parsing, deduplication, anomaly boundaries, and daily continuous **forward-filling** for holiday/weekend NAV tracking in `day 2/data_cleaning.py`.
*   **Dimensional Star Schema:** Designed a normalized relational model in `day 2/schema.sql` spanning 2 dimension tables (`dim_fund`, `dim_date`) and 6 fact tables (`fact_nav`, `fact_transactions`, etc.).
*   **SQL Analytics:** Drafted 10 high-value business queries in `day 2/queries.sql` analyzing AUM trends, monthly average NAVs, YoY growth, and investor demographic cash flows.

---

## 🛠️ Technical Stack Details

*   **Language:** Python 3.10+ (Pandas, NumPy, Requests)
*   **Database Engine:** SQLite3
*   **SQL Interfaces:** standard SQLite SQL DDL
*   **ORM / Drivers:** Python-native SQLite3 connector
*   **Version Control:** Git + GitHub

# Bluestock Mutual Fund Analytics Platform 📈
### End-to-End Data Engineering, ETL Pipeline & Interactive Business Intelligence Dashboard
**Prepared by:** Intern / Data Analyst — Bluestock Fintech  
**Date:** June 2026  
**Version:** v1.0 (Production Release - Day-wise Restructure)  

Welcome to the **Mutual Fund Analytics Platform** repository. This project is structured into self-contained daily milestone folders (`day 1` through `day 7`), mapping to each phase of the capstone project. 

---

## 📁 Day-wise Repository Structure

The repository has been restructured into independent, daily milestone directories. Each folder contains its own self-contained sub-structure (`data/raw`, `data/processed`, `data/db`, `notebooks/`, `sql/`, `dashboard/`, `reports/charts/`, `scripts/`):

```text
bluestock-mutual-fund-analytics/
├── day 1/                    <- Project Setup + Data Ingestion (ETL)
│   ├── data/raw/             <- Live downloaded raw CSVs
│   ├── scripts/
│   │   ├── data_ingestion.py <- Inspects shapes, dtypes, and anomalies
│   │   └── live_nav_fetch.py <- Fetches live NAV from mfapi.in API
│   ├── requirements.txt
│   └── README.md
├── day 2/                    <- Relational DB Design & ETL Pipeline
│   ├── data/
│   │   ├── raw/
│   │   ├── processed/        <- Cleaned datasets
│   │   └── db/               <- SQLite database bluestock_mf.db
│   ├── sql/
│   │   ├── schema.sql        <- Star schema DDL tables and indexes
│   │   └── queries.sql       <- 10 core analytical business queries
│   ├── scripts/
│   │   ├── etl_pipeline.py   <- Preprocesses CSVs & loads relational database
│   │   └── execute_queries.py <- Runs and logs the 10 queries
│   ├── reports/
│   │   └── data_dictionary.md <- Database field documentation
│   └── README.md
├── day 3/                    <- Exploratory Data Analysis
│   ├── notebooks/
│   │   └── EDA_Analysis.ipynb <- Notebook containing 15+ EDA plots
│   ├── reports/charts/       <- 15+ exported interactive/static plots
│   └── README.md
├── day 4/                    <- Performance & Risk Analytics
│   ├── data/
│   │   ├── db/               <- Aligned relational database
│   │   └── processed/        <- fund_scorecard.csv & var_cvar_report.csv
│   ├── notebooks/
│   │   └── Performance_Analytics.ipynb <- CAGR, Sharpe, and Sortino calculations
│   ├── scripts/
│   │   └── compute_metrics.py <- Computes scorecards, benchmarks, and drawdowns
│   ├── reports/charts/       <- benchmark_comparison.png, rolling_sharpe_chart.png
│   └── README.md
├── day 5/                    <- BI Dashboard (Power BI)
│   ├── dashboard/
│   │   └── bluestock_mf_dashboard.pbip (and template directories)
│   ├── reports/
│   │   ├── Dashboard.pdf     <- Exported 4-page dashboard
│   │   └── charts/           <- page_1.png to page_4.png page captures
│   └── README.md
├── day 6/                    <- Advanced Analytics (Cohort & Recommender)
│   ├── data/
│   │   ├── db/
│   │   └── processed/        <- cohort_analysis.csv & sip_continuity.csv
│   ├── notebooks/
│   │   └── Advanced_Analytics.ipynb <- Cohort and HHI calculations
│   ├── scripts/
│   │   └── recommender.py    <- CLI-based mutual fund recommender
│   └── README.md
└── day 7/                    <- Final Reporting & Capstone Delivery
    ├── data/
    │   ├── raw/              <- Input raw CSV datasets
    │   ├── processed/        <- Processed CSV metrics outputs
    │   └── db/               <- Populated SQLite relational database
    ├── sql/
    │   ├── schema.sql
    │   └── queries.sql
    ├── scripts/
    │   ├── live_nav_fetch.py
    │   ├── etl_pipeline.py
    │   ├── compute_metrics.py
    │   ├── recommender.py
    │   ├── generate_report.py <- ReportLab PDF compiler
    │   └── generate_presentation.py <- python-pptx presentation deck compiler
    ├── reports/
    │   ├── Final_Report.pdf  <- Compiles the final 19-page wealth report
    │   ├── Bluestock_MF_Presentation.pptx <- Compiles the 12-slide presentation deck
    │   └── charts/           <- Extracted charts embedded in the PDF/PPTX
    ├── run_pipeline.py       <- Master orchestrator executing Day 7 from scratch
    ├── requirements.txt      <- Consolidated dependencies
    └── README.md
```

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Solohunter15/bluestock-mutual-fund-analytics.git
cd bluestock-mutual-fund-analytics
```

### 2. Install Project Dependencies
Ensure you have Python 3.10+ installed. Install the platform dependencies via pip:
```bash
pip install -r requirements.txt
pip install reportlab python-pptx
```

---

## 💻 Running the Platform (Self-Contained Day 7 Suite)

The final day (`day 7`) contains the fully integrated pipeline, databases, DDL scripts, and document compilers.

### 1. Execute the Master Pipeline
To run the entire data engineering and quantitative analytics suite from scratch inside the `day 7` workspace:
```bash
python "day 7/run_pipeline.py"
```
This single command runs the following stages:
1. **Live NAV Ingestion:** Fetches real-time NAV data for 6 major schemes from `mfapi.in` and saves raw responses in `day 7/data/raw/`.
2. **ETL Preprocessing:** Standardizes dates, cleans types, forward-fills weekend/holiday gaps, and loads the relational database in `day 7/data/db/bluestock_mf.db`.
3. **Performance Calculations:** Computes CAGR, risk ratios (Sharpe, Sortino), OLS regression (Alpha, Beta), downside risk (Value at Risk, CVaR), and sector portfolio HHI.
4. **Recommender CLI:** Executes a test recommendation for a Moderate risk appetite.

### 2. Launch the Interactive Recommender CLI
```bash
python "day 7/scripts/recommender.py" [low/moderate/high]
```
If no risk category is provided, it will launch an interactive command-line prompt.

### 3. Generate the Deliverables Manually
To recompile the final wealth report and slide deck:
- **19-Page PDF Report:** `python "day 7/scripts/generate_report.py"` (Generates `day 7/reports/Final_Report.pdf`)
- **12-Slide PowerPoint Deck:** `python "day 7/scripts/generate_presentation.py"` (Generates `day 7/reports/Bluestock_MF_Presentation.pptx`)

---

## 💡 Key Business & Financial Takeaways

1. **SIP Continuity & Churn Vulnerability:** SIP continuity analysis on investors with 6+ SIP transactions reveals that **97.80% (1,332 investors)** have average transaction gaps exceeding **35 days**. The global average gap stands at **64.89 days**, double the standard 30-day billing cycle. This points to irregular savings behavior, highlighting the need for automated mandate validation and notifications.
2. **Sector Concentration Risk (HHI):** Sector Herfindahl-Hirschman Index (HHI) rankings reveal that Large Cap portfolios exhibit higher sector concentration. **Axis Bluechip Fund (Regular)** is the most concentrated portfolio with a sector HHI of **2,967.69** across only 7 sectors. **UTI Mid Cap Fund (Regular)** represents the most diversified equity portfolio with an HHI of **1,240.20** across 10 sectors.
3. **Downside Risk Profiles (VaR/CVaR):** Small Cap funds exhibited the highest downside exposure. **SBI Small Cap Fund (Direct)** and **Axis Small Cap Fund (Regular)** show the highest daily Historical VaR (95%) of approximately **-2.52%** and **-2.43%** respectively. In the worst 5% of trading days, the average daily loss (CVaR) increases to **-3.23%**. Debt and Liquid funds remain stable with daily VaR of **-0.08%** and CVaR of **-0.10%**.
4. **Investor Cohort Expansion:** The **2024 cohort** comprises 4,803 investors contributing a gross investment of **Rs. 225.8 crore** (Net: Rs. 102.5 crore). The **2025 cohort** is smaller (197 investors) contributing **Rs. 1.90 crore** (Net: Rs. 0.75 crore). However, the average monthly SIP amount for the 2025 cohort is **Rs. 13,505.21**, which represents a **22.8% increase** compared to the 2024 cohort's average of **Rs. 10,996.89**, showing that newer cohorts commit larger ticket sizes.
5. **Scorecard Best Performers:**
   - **Large Cap Category:** HDFC Top 100 Fund (Regular) leads the moderate-risk category with a Sharpe ratio of **1.06** and a 3-Year CAGR of **14.84%**.
   - **Mid Cap Category:** Kotak Emerging Equity Fund (Regular) leads the high-risk category with a Sharpe ratio of **0.96** and a 3-Year CAGR of **18.23%**.
   - **Small Cap Category:** SBI Small Cap Fund (Direct) leads with a 3-Year CAGR of **23.14%** but exhibits higher volatility.

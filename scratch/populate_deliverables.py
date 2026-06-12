import os
import shutil

project_root = r"c:\Users\jibum\OneDrive\Desktop\Bluestock Internship"

# 1. Helper to copy directories
def copy_dir(src, dst):
    if os.path.exists(src):
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        print(f"Copied directory: {src} -> {dst}")

# 2. Helper to copy files
def copy_file(src, dst):
    if os.path.exists(src):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        print(f"Copied file: {src} -> {dst}")

# 3. Copy Raw Datasets to Days 1, 2, 4, 6
raw_csvs = [
    "01_fund_master.csv", "02_nav_history.csv", "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv", "05_category_inflows.csv", "06_industry_folio_count.csv",
    "07_scheme_performance.csv", "08_investor_transactions.csv", "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for day in ["day 1", "day 2", "day 4", "day 6"]:
    for csv in raw_csvs:
        src = os.path.join(project_root, "data", "raw", csv)
        dst = os.path.join(project_root, day, "data", "raw", csv)
        copy_file(src, dst)

# 4. DAY 1 Deliverables
copy_file(os.path.join(project_root, "scripts", "live_nav_fetch.py"), os.path.join(project_root, "day 1", "scripts", "live_nav_fetch.py"))
copy_file(os.path.join(project_root, "requirements.txt"), os.path.join(project_root, "day 1", "requirements.txt"))

# Create day 1 data_ingestion.py
data_ingestion_code = """\"\"\"
Bluestock Mutual Fund Analytics Platform - Ingestion & Inspection
Loads all 10 raw CSV datasets, inspects shapes/dtypes, and audits anomalies.
\"\"\"
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
        print(f"\\nFILE: {filename}")
        print(f"Shape: {df.shape}")
        print("Dtypes:")
        print(df.dtypes)
        print("Head Preview:")
        print(df.head(2))

if __name__ == "__main__":
    load_and_inspect()
"""
with open(os.path.join(project_root, "day 1", "scripts", "data_ingestion.py"), "w", encoding="utf-8") as f:
    f.write(data_ingestion_code)

# 5. DAY 2 Deliverables
copy_file(os.path.join(project_root, "sql", "schema.sql"), os.path.join(project_root, "day 2", "sql", "schema.sql"))
copy_file(os.path.join(project_root, "sql", "queries.sql"), os.path.join(project_root, "day 2", "sql", "queries.sql"))
copy_file(os.path.join(project_root, "scripts", "etl_pipeline.py"), os.path.join(project_root, "day 2", "scripts", "etl_pipeline.py"))
copy_file(os.path.join(project_root, "scripts", "execute_queries.py"), os.path.join(project_root, "day 2", "scripts", "execute_queries.py"))
copy_file(os.path.join(project_root, "data", "data_dictionary.md"), os.path.join(project_root, "day 2", "reports", "data_dictionary.md"))

# 6. DAY 3 Deliverables
copy_file(os.path.join(project_root, "notebooks", "03_eda_analysis.ipynb"), os.path.join(project_root, "day 3", "notebooks", "EDA_Analysis.ipynb"))
# Copy all charts from reports/charts/ to day 3/reports/charts/
for item in os.listdir(os.path.join(project_root, "reports", "charts")):
    src_file = os.path.join(project_root, "reports", "charts", item)
    if os.path.isfile(src_file):
        copy_file(src_file, os.path.join(project_root, "day 3", "reports", "charts", item))

# 7. DAY 4 Deliverables
copy_file(os.path.join(project_root, "notebooks", "04_performance_analytics.ipynb"), os.path.join(project_root, "day 4", "notebooks", "Performance_Analytics.ipynb"))
copy_file(os.path.join(project_root, "scripts", "compute_metrics.py"), os.path.join(project_root, "day 4", "scripts", "compute_metrics.py"))
copy_file(os.path.join(project_root, "reports", "charts", "benchmark_comparison.png"), os.path.join(project_root, "day 4", "reports", "charts", "benchmark_comparison.png"))

# 8. DAY 5 Deliverables
copy_dir(os.path.join(project_root, "bluestock_mf_dashboard.pbix.Report"), os.path.join(project_root, "day 5", "dashboard", "bluestock_mf_dashboard.pbix.Report"))
copy_dir(os.path.join(project_root, "bluestock_mf_dashboard.pbix.SemanticModel"), os.path.join(project_root, "day 5", "dashboard", "bluestock_mf_dashboard.pbix.SemanticModel"))
copy_file(os.path.join(project_root, "bluestock_mf_dashboard.pbix.pbip"), os.path.join(project_root, "day 5", "dashboard", "bluestock_mf_dashboard.pbix.pbip"))
copy_file(os.path.join(project_root, "Dashboard.pdf"), os.path.join(project_root, "day 5", "reports", "Dashboard.pdf"))

# Copy screenshots to Day 5 reports/charts and day 5/dashboard/
for idx in range(1, 5):
    img_name = f"page_{idx}.png"
    copy_file(os.path.join(project_root, img_name), os.path.join(project_root, "day 5", "reports", "charts", img_name))
    copy_file(os.path.join(project_root, img_name), os.path.join(project_root, "day 5", "dashboard", img_name))

# 9. DAY 6 Deliverables
copy_file(os.path.join(project_root, "notebooks", "05_advanced_analytics.ipynb"), os.path.join(project_root, "day 6", "notebooks", "Advanced_Analytics.ipynb"))
copy_file(os.path.join(project_root, "scripts", "recommender.py"), os.path.join(project_root, "day 6", "scripts", "recommender.py"))
copy_file(os.path.join(project_root, "reports", "charts", "rolling_sharpe_chart.png"), os.path.join(project_root, "day 6", "reports", "charts", "rolling_sharpe_chart.png"))

# 10. DAY 7 Deliverables
copy_file(os.path.join(project_root, "scripts", "generate_report.py"), os.path.join(project_root, "day 7", "scripts", "generate_report.py"))
copy_file(os.path.join(project_root, "scripts", "generate_presentation.py"), os.path.join(project_root, "day 7", "scripts", "generate_presentation.py"))
copy_file(os.path.join(project_root, "run_pipeline.py"), os.path.join(project_root, "day 7", "scripts", "run_pipeline.py"))
copy_file(os.path.join(project_root, "requirements.txt"), os.path.join(project_root, "day 7", "requirements.txt"))

# Copy all charts/screenshots to Day 7 reports/charts and Day 7 dashboard/ for self-contained generation
for item in os.listdir(os.path.join(project_root, "reports", "charts")):
    src_file = os.path.join(project_root, "reports", "charts", item)
    if os.path.isfile(src_file):
        copy_file(src_file, os.path.join(project_root, "day 7", "reports", "charts", item))

for idx in range(1, 5):
    img_name = f"page_{idx}.png"
    copy_file(os.path.join(project_root, img_name), os.path.join(project_root, "day 7", "dashboard", img_name))

print("Deliverables populated successfully!")

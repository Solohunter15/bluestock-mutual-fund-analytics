# Day 6: Advanced Analytics & Risk Metrics
### Quantitative Risk Management, Investor Cohorts, and Concentration Analysis

This directory contains the deliverables for **Day 6** of the Bluestock Mutual Fund Analytics Capstone Project. It covers Value at Risk (VaR), Conditional Value at Risk (CVaR), rolling Sharpe ratio tracking, investor cohort analysis, SIP continuity/churn risk, and sector concentration (HHI) for the portfolio holdings.

---

## 📁 Day 6 Deliverables & Folder Structure

All Day 6 code and reports are stored inside this folder:

```text
day 6/
├── Advanced_Analytics.ipynb   # Main Jupyter notebook with calculations, plots, and markdown insights
├── var_cvar_report.csv        # Computed VaR & CVaR (95%) for all 40 schemes (CSV format)
├── recommender.py             # Standalone command-line interactive fund recommendation script
├── rolling_sharpe_chart.png   # Time-series chart tracking rolling 90-day Sharpe ratio for 5 key funds
└── README.md                  # Day 6 documentation & execution guide (This file)
```

---

## 📊 Core Financial Methodologies & Formulas

### 1. Value at Risk (VaR 95%) & Conditional VaR (CVaR 95%)
Daily NAV return series were calculated after aligning data with the Nifty 100 benchmark index trading calendar:
$$R_t = \frac{NAV_t}{NAV_{t-1}} - 1$$
- **Historical VaR (95%)**: Represents the 5th percentile of the daily return distribution.
  $$VaR_{95} = P_5(R_t)$$
- **Conditional VaR (95%)**: Measures the average loss on days when the return is worse than or equal to the VaR threshold.
  $$CVaR_{95} = E[R_t \mid R_t \le VaR_{95}]$$

### 2. Rolling 90-Day Sharpe Ratio
Annualized rolling Sharpe ratio tracked over a 90-day window:
$$\text{Sharpe}_{\text{rolling}} = \frac{\text{rolling\_mean}(R_t)}{\text{rolling\_std}(R_t)} \times \sqrt{252}$$

### 3. Sector Herfindahl-Hirschman Index (HHI)
Computed sector concentration risk across all equity portfolios:
$$\text{HHI}_{\text{sector}} = \sum_{i=1}^{S} W_i^2$$
where $W_i$ represents the percentage allocation weight of sector $i$ in the fund portfolio ($W_i \in [0, 100]$).

---

## 🚀 Execution Instructions

### Running the Fund Recommender
The `recommender.py` script matches your risk appetite to the best-performing funds by Sharpe ratio. It can be run interactively or by passing an argument:

```bash
# Interactive mode (prompts you for input)
python recommender.py

# Direct command-line argument mode (Low / Moderate / High)
python recommender.py Low
python recommender.py Moderate
python recommender.py High
```

### Running the Notebook In-Place
To re-run the entire notebook programmatically and save outputs:
```bash
python -m jupyter nbconvert --to notebook --execute --inplace Advanced_Analytics.ipynb
```

---

## 🔍 Key Findings & Insights

1. **Small Cap Downside Risk**: Small Cap funds display the highest downside exposure, with **SBI Small Cap Fund (Direct)** and **Axis Small Cap Fund (Regular)** leading the daily VaR list (at **-2.69%** and **-2.62%** respectively).
2. **Inflow Expansion**: The **2025 cohort** signed up with a **22.8% larger average SIP size** (Rs. 13,505.21) compared to the **2024 cohort** (Rs. 10,996.89), showing ticket size expansion despite smaller volume.
3. **Severe Churn Risk**: **97.80%** of eligible investors with $\ge 6$ transactions exhibit average gaps $> 35$ days between dates (global average gap: **64.89 days**).
4. **Sector Concentration**: **Axis Bluechip Fund (Regular)** represents the most concentrated sector profile (HHI = **2,967.69** across 7 sectors), while **UTI Mid Cap Fund (Regular)** is the most diversified (HHI = **1,240.20** across 10 sectors).
5. **Sharpe Disparity**: Liquid funds exhibit Sharpe ratios above 5.00 due to near-zero standard deviation (denominator). Active equity funds exhibit healthy Sharpe profiles, led by **HDFC Top 100 Fund (Regular)** and **Mirae Asset Large Cap Fund (Regular)** (both at **1.06**).

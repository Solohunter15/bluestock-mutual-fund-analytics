# Day 4: Mutual Fund Performance Analytics & Scorecard
### End-to-End Quantitative Risk-Return Analysis & Benchmarking

This directory contains the deliverables for **Day 4** of the Bluestock Capstone Project. It focuses on evaluating the historical performance, market sensitivity, and risk-adjusted efficiency of **40 mutual fund schemes** over a 4.4-year period (January 2022 to May 2026), benchmarking them against the **Nifty 100** index.

---

## 📁 Day 4 Deliverables & Folder Structure

All calculations and outputs are self-contained in this folder:

```text
day 4/
├── Performance_Analytics.ipynb       # Jupyter notebook with SQL loading & financial math
├── reports/
│   ├── alpha_beta.csv                # Regression metrics (Alpha, Beta, R-squared, p-value)
│   ├── fund_scorecard.csv            # Scorecard metrics & overall composite score
│   └── charts/
│       └── benchmark_comparison.png  # Cumulative return comparison chart (Top 5 vs Benchmarks)
└── README.md                         # Day 4 documentation (This file)
```

---

## 📊 Core Financial Calculations & Formulas

1. **Daily Returns ($R_t$)**:
   Daily percentage change of Net Asset Value (NAV):
   $$R_t = \frac{NAV_t}{NAV_{t-1}} - 1$$
   *Note: NAV daily returns were aligned with Nifty 100 trading days to eliminate weekend forward-filling effects.*

2. **Compounded Annual Growth Rate (CAGR)**:
   Calculated across three horizons:
   - **1-Year**: Growth from May 29, 2025 to May 29, 2026.
   - **3-Year**: Annualized growth from May 29, 2023 to May 29, 2026.
   - **5-Year Proxy**: Inception-to-date CAGR (since the historical database covers 4.4 years).
   $$CAGR = \left( \frac{NAV_{\text{end}}}{NAV_{\text{start}}} \right)^{\frac{1}{\text{years}}} - 1$$

3. **Risk-Adjusted Performance (6.5% Annual Risk-Free Rate, $R_f$)**:
   - **Sharpe Ratio**: Annualized return per unit of total risk (volatility $\sigma_f$):
     $$\text{Sharpe} = \frac{\overline{R}_{\text{fund}} - R_{f,\text{daily}}}{\sigma_{\text{fund}}} \times \sqrt{252}$$
   - **Sortino Ratio**: Annualized return per unit of downside risk ($\sigma_{\text{downside}}$, computed using only negative returns):
     $$\text{Sortino} = \frac{\overline{R}_{\text{fund}} - R_{f,\text{daily}}}{\sigma_{\text{downside}}} \times \sqrt{252}$$

4. **OLS Regression (vs. Nifty 100)**:
   Ordinary Least Squares (OLS) regression on daily excess returns:
   - **Beta ($\beta$)**: Systematic market risk.
   - **Alpha ($\alpha$)**: Annualized risk-adjusted excess return (intercept $\times 252$).
   - **R-squared ($R^2$)**: Percentage of fund variance explained by Nifty 100 movements.
   - **p-value**: Statistical significance of the regression.

5. **Maximum Drawdown (MDD)**:
   The maximum peak-to-trough drop in NAV:
   $$\text{Drawdown} = \min \left( \frac{NAV_t}{\text{Running Max}(NAV_t)} - 1 \right)$$
   Peak and trough dates are identified for each scheme to locate historical distress periods.

6. **Composite Fund Scorecard (0-100 Score)**:
   Ranks were calculated across all 40 funds (0 to 100 scale) and weighted to compute a composite scorecard:
   - **30%**: 3-Year CAGR
   - **25%**: Annualized Sharpe Ratio
   - **20%**: Annualized Alpha
   - **15%**: Expense Ratio (lower expense = higher rank)
   - **10%**: Maximum Drawdown (smaller drawdown magnitude = higher rank)

---

## 🔍 Key Insights & Benchmark Analysis

### 🌟 Top 5 Scorecard Funds
Based on the multi-factor scorecard inside [fund_scorecard.csv](file:///c:/Users/jibum/OneDrive/Desktop/Bluestock%20Internship/day%204/reports/fund_scorecard.csv), the leading schemes are:

| AMFI Code | Scheme Name | Category | 3-Yr CAGR | Sharpe | Alpha | Expense Ratio | Max Drawdown | Fund Score |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **148567** | Mirae Asset Large Cap - Regular | Equity | 34.00% | 1.45 | 0.270 | 1.46% | -11.27% | **85.90** |
| **120505** | ICICI Pru Midcap - Regular | Equity | 31.78% | 1.18 | 0.293 | 1.36% | -18.19% | **81.79** |
| **120843** | Kotak Flexicap - Regular | Equity | 29.58% | 1.31 | 0.273 | 1.45% | -12.97% | **81.54** |
| **100033** | HDFC Mid-Cap Opportunities - Regular | Equity | 32.44% | 1.09 | 0.272 | 1.38% | -16.22% | **80.26** |
| **120504** | ICICI Pru Bluechip - Direct | Equity | 32.49% | 1.03 | 0.212 | 0.80% | -12.59% | **79.49** |

### 📈 3-Year Cumulative Returns vs. Benchmarks
The top 5 scorecard funds significantly outperformed both the Nifty 50 and Nifty 100 indices over the 3-year period starting May 29, 2023:

![Benchmark Comparison Chart](file:///c:/Users/jibum/OneDrive/Desktop/Bluestock%20Internship/day%204/reports/charts/benchmark_comparison.png)

### 📐 Tracking Error vs. Benchmarks
Annualized tracking error measures the active risk of outperforming the benchmark:
- **ICICI Pru Midcap Fund**: TE vs Nifty 50: **31.39%** | TE vs Nifty 100: **31.37%**
- **Mirae Asset Large Cap Fund**: TE vs Nifty 50: **31.42%** | TE vs Nifty 100: **31.40%**
- **Kotak Flexicap Fund**: TE vs Nifty 50: **31.43%** | TE vs Nifty 100: **31.41%**

*Full statistics are detailed in [alpha_beta.csv](file:///c:/Users/jibum/OneDrive/Desktop/Bluestock%20Internship/day%204/reports/alpha_beta.csv) and [fund_scorecard.csv](file:///c:/Users/jibum/OneDrive/Desktop/Bluestock%20Internship/day%204/reports/fund_scorecard.csv).*


# Task_03_Descriptive_Stats

This project is submitted as part of Syracuse University's Research Task 03 (Summer 2025). The objective is to analyze and summarize election-related social media datasets using three different approaches in Python: pure standard library, Pandas, and Polars.

---

## Datasets Analyzed

1. `facebook_ads.csv`  
2. `twitter_ads.csv`  
3. `advertiser_spend.csv`  

These datasets contain political ad and engagement data collected during the 2024 U.S. presidential election.

---

## Scripts Overview

### 1. Pure Python Scripts
These scripts use only standard Python libraries (`csv`, `statistics`, `math`, `collections`).

- `facebook_pure_python_stats.py`
- `twitter_pure_python_stats.py`
- `advertiser_pure_python_stats.py`

Each script includes:
- Basic descriptive statistics (count, mean, min, max, std)
- Unique values and most frequent values for categorical columns
- Group-level summaries (e.g., by `page_id`, `sponsor_name`)

### 2. Pandas-Based Scripts
These scripts leverage the `pandas` library for efficient data analysis.

- `pandas_facebook_ads.py`
- `pandas_twitter_ads.py`
- `pandas_advertiser_spend.py`

Each script performs:
- `describe()` for numeric columns
- `nunique()` for unique counts
- `value_counts()` for most common categories
- Grouped stats where relevant

### 3. Polars-Based Scripts
These scripts utilize the `polars` library for high-performance processing.

- `polars_facebook_ads.py`
- `polars_twitter_ads.py`
- `polars_advertiser_spend.py`

Each script outputs:
- Summary stats using `.describe()`
- Unique counts and value frequencies
- Fast performance, even on large files

---


## How to Run

1. Clone the repository:
   ```
   git clone https://github.com/kulveenkaur25/Task_03_Descriptive_Stats.git
   cd Task_03_Descriptive_Stats
   ```

2. Place the datasets into a folder named `datasets/`:
   ```
   /datasets/facebook_ads.csv
   /datasets/twitter_ads.csv
   /datasets/advertiser_spend.csv
   ```

3. Run any script with Python 3.8+:
   ```
   python facebook_pure_python_stats.py
   python pandas_twitter_ads.py
   python polars_advertiser_spend.py
   ```

Outputs will be generated in the corresponding folder.

---

## Summary of Insights

- A small number of Facebook pages were responsible for the majority of ad activity.
- "Love" and "Care" reactions were more frequent than "Angry" or "Sad" in advertiser content.
- Twitter ads showed high average view counts despite fewer interactions.
- Advocacy and call-to-action were the most common message types across platforms.
- Polars executed significantly faster than Pandas, especially for grouped operations.

---

## Author

Kulveen Kaur  
M.S. Applied Data Science  
Syracuse University  
Research OPT — Summer 2025

# Task_03_Descriptive_Stats

This project is part of Syracuse University's Research Task 03 for Summer 2025. The objective is to analyze and summarize election-related social media datasets using three different approaches in Python: pure standard library, Pandas, and Polars.

---

## Datasets Analyzed


1. `facebook_ads.csv`
2. `twitter_ads.csv`
3. `advertiser_spend.csv`

---

## Scripts Overview

### 1. Pure Python (No Pandas or Polars)
These scripts use only Python's built-in libraries like `csv`, `math`, `statistics`, and `collections`.

- `facebook_pure_python_stats.py`
- `twitter_pure_python_stats.py`
- `advertiser_pure_python_stats.py`

Each script calculates:
- Count, mean, min, max, std dev (for numeric columns)
- Unique values, most frequent values (for categorical columns)
- Grouped statistics (e.g., by `page_id` or `sponsor_name`)

---

### 2. Pandas-Based Analysis
Scripts use the `pandas` library to compute:
- Descriptive stats (`describe()`)
- Unique value counts (`nunique()`)
- Top value counts (`value_counts()`)

Files:
- `pandas_facebook_ads.py`
- `pandas_twitter_ads.py`
- `pandas_advertiser_spend.py`

Grouped stats (where applicable) are also included.

---

### 3. Polars-Based Analysis
Scripts use the high-performance `polars` library to mirror the Pandas analysis.

Files:
- `polars_facebook_ads.py`
- `polars_twitter_ads.py`
- `polars_advertiser_spend.py`

All results are saved as `.json` files under `output_pandas/` and `output_polars/`.

---

## Output Files

Each script saves the results in JSON format, containing:
- `describe`
- `nunique`
- `value_counts`
- grouped summaries

Directory examples:
- `output_pandas/facebook_ads_pandas_stats.json`
- `output_polars/twitter_ads_polars_stats.json`

---

## How to Run

1. Clone the repository.
2. Place datasets inside a folder named `datasets/` in the root directory.
3. Run each script using Python 3.8+:

```bash
python facebook_pure_python_stats.py
python pandas_twitter_ads.py
python polars_advertiser_spend.py

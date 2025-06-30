import pandas as pd
import json
import os

def analyze_twitter_ads():
    df = pd.read_csv("datasets/twitter_ads.csv", low_memory=False)
    
    describe = df.describe(include='all')
    nunique = df.nunique()
    value_counts = {col: df[col].value_counts(dropna=False).head(5).to_dict()
                    for col in df.columns if df[col].dtype == 'object'}

    print("=== Describe ===")
    print(describe)
    print("\n=== Number of Unique Values ===")
    print(nunique)
    print("\n=== Value Counts (Top 5) ===")
    for col, vc in value_counts.items():
        print(f"\nColumn: {col}")
        print(vc)

    os.makedirs("output_pandas", exist_ok=True)
    results = {
        "describe": describe.to_dict(),
        "nunique": nunique.to_dict(),
        "value_counts": value_counts
    }
    with open("output_pandas/twitter_ads_pandas_stats.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, default=str)

if __name__ == "__main__":
    analyze_twitter_ads()

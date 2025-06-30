import pandas as pd
import json
import os

print("Script started...")

try:
    # Load CSV
    df = pd.read_csv("datasets/facebook_ads.csv", low_memory=False)
    print("CSV loaded successfully.")

    # Generate describe
    describe = df.describe(include='all')
    print("Describe computed.")

    # Unique values
    nunique = df.nunique()
    print("Unique values computed.")

    # Top 5 value counts for object-type columns
    value_counts = {
        col: df[col].value_counts(dropna=False).head(5).to_dict()
        for col in df.select_dtypes(include='object').columns
    }
    print("Value counts computed.")

    # Create output directory
    os.makedirs("output_pandas", exist_ok=True)

    # Save to JSON
    with open("output_pandas/facebook_ads_pandas_stats.json", "w", encoding="utf-8") as f:
        json.dump({
            "describe": describe.to_dict(),
            "nunique": nunique.to_dict(),
            "value_counts": value_counts
        }, f, indent=2)

    # Print to terminal
    print("\n=== Describe ===")
    print(describe)

    print("\n=== Unique Value Counts ===")
    print(nunique)

    print("\n=== Top 5 Value Counts (Object Columns) ===")
    for col, vc in value_counts.items():
        print(f"\nColumn: {col}")
        print(vc)

    print("\nAll done. Output saved to: output_pandas/facebook_ads_pandas_stats.json")

except Exception as e:
    print("ERROR:", e)

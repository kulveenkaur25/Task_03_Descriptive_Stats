import polars as pl
import json
import os

def get_top_value_counts(df: pl.DataFrame, col: str, top_n: int = 5):
    try:
        result = (
            df.select(col)
              .drop_nulls()
              .group_by(col)
              .count()
              .sort("count", descending=True)
              .limit(top_n)
        )
        return result.to_dicts()
    except Exception as e:
        print(f"⚠️ Skipped column {col} due to error: {e}")
        return None

def analyze_facebook_ads():
    print("Starting Polars analysis...")

    df = pl.read_csv("datasets/facebook_ads.csv", infer_schema_length=10000)

    describe = df.describe().to_dict(as_series=False)
    nunique = {col: df[col].n_unique() for col in df.columns}

    value_counts = {}
    for col in df.columns:
        if df.schema[col] == pl.Utf8:
            result = get_top_value_counts(df, col)
            if result:
                value_counts[col] = result

    print("Describe and stats computed.")

    os.makedirs("output_polars", exist_ok=True)
    with open("output_polars/facebook_ads_polars_stats.json", "w") as f:
        json.dump({
            "describe": describe,
            "nunique": nunique,
            "value_counts": value_counts
        }, f, indent=2)

    print("=== Describe ===")
    print(df.describe())

    print("\n=== Unique Value Counts ===")
    print(nunique)

    print("\n=== Top 5 Value Counts ===")
    for col, values in value_counts.items():
        print(f"\nColumn: {col}")
        print(values)

    print("All done. Results saved to output_polars/facebook_ads_polars_stats.json")

if __name__ == "__main__":
    analyze_facebook_ads()

import csv
import math
import json
import os
from collections import defaultdict, Counter
from statistics import mean, stdev

# Load dataset
input_file = "datasets/advertiser_spend.csv"
with open(input_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Helper function to check if a value is numeric
def is_float(value):
    try:
        float(value)
        return True
    except:
        return False

# Analyze data for each column
def analyze_data(rows):
    col_data = defaultdict(list)
    for row in rows:
        for k, v in row.items():
            if v != '':
                col_data[k].append(v)

    result = {}
    for col, values in col_data.items():
        if all(is_float(v) for v in values):
            numeric_values = list(map(float, values))
            result[col] = {
                'count': len(numeric_values),
                'mean': mean(numeric_values),
                'min': min(numeric_values),
                'max': max(numeric_values),
                'std_dev': stdev(numeric_values) if len(numeric_values) > 1 else 0.0
            }
        else:
            counter = Counter(values)
            result[col] = {
                'count': len(values),
                'unique_values': len(set(values)),
                'most_frequent': counter.most_common(1)[0]
            }
    return result

# Grouping function
def group_by(rows, *cols):
    grouped = defaultdict(list)
    for row in rows:
        key = tuple(row[col] for col in cols)
        grouped[key].append(row)
    return grouped

# Ensure output folder exists
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Analyze full dataset
overall_stats = analyze_data(data)

# Group by 'Sponsor Name'
grouped_by_sponsor = group_by(data, 'Sponsor Name')
stats_by_sponsor = {k: analyze_data(v) for k, v in grouped_by_sponsor.items()}

# Group by 'Sponsor Name' and 'Sponsor Id'
grouped_by_sponsor_id = group_by(data, 'Sponsor Name', 'Sponsor Id')
stats_by_sponsor_id = {k: analyze_data(v) for k, v in grouped_by_sponsor_id.items()}

# Show sample outputs in console
print("=== Overall Stats Sample ===")
print(json.dumps(dict(list(overall_stats.items())[:5]), indent=2))

print("\n=== Grouped by 'Sponsor Name' Sample ===")
print(json.dumps({str(k): v for k, v in list(stats_by_sponsor.items())[:2]}, indent=2))

print("\n=== Grouped by 'Sponsor Name' and 'Sponsor Id' Sample ===")
print(json.dumps({str(k): v for k, v in list(stats_by_sponsor_id.items())[:2]}, indent=2))

# Save full outputs
with open(os.path.join(output_dir, "advertiser_overall_stats.json"), "w", encoding="utf-8") as f:
    json.dump(overall_stats, f, indent=2)

with open(os.path.join(output_dir, "advertiser_grouped_by_sponsor_stats.json"), "w", encoding="utf-8") as f:
    json.dump({str(k): v for k, v in stats_by_sponsor.items()}, f, indent=2)

with open(os.path.join(output_dir, "advertiser_grouped_by_sponsor_id_stats.json"), "w", encoding="utf-8") as f:
    json.dump({str(k): v for k, v in stats_by_sponsor_id.items()}, f, indent=2)

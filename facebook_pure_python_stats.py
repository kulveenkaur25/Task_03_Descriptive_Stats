import csv
import math
import json
import os
from collections import defaultdict, Counter
from statistics import mean, stdev

input_file = "datasets/facebook_ads.csv"  # update if needed
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Load data
with open(input_file, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)

def is_float(value):
    try:
        float(value)
        return True
    except:
        return False

def analyze_data(rows):
    col_data = defaultdict(list)
    for row in rows:
        for k, v in row.items():
            if v != '':
                col_data[k].append(v)

    result = {}
    for col, values in col_data.items():
        if all(is_float(v) for v in values):
            nums = list(map(float, values))
            result[col] = {
                'count': len(nums),
                'mean': mean(nums),
                'min': min(nums),
                'max': max(nums),
                'std_dev': stdev(nums) if len(nums) > 1 else 0.0
            }
        else:
            counter = Counter(values)
            result[col] = {
                'count': len(values),
                'unique_values': len(set(values)),
                'most_frequent': counter.most_common(1)[0]
            }
    return result

def group_by(rows, *cols):
    grouped = defaultdict(list)
    for row in rows:
        key = tuple(row.get(col, '') for col in cols)
        grouped[key].append(row)
    return grouped

# Compute stats
overall_stats = analyze_data(data)

# Grouped by 'page_id'
grouped_by_page = group_by(data, 'page_id')
stats_by_page = {k: analyze_data(v) for k, v in grouped_by_page.items()}

# Grouped by 'page_id' and 'ad_id'
grouped_by_page_ad = group_by(data, 'page_id', 'ad_id')
stats_by_page_ad = {k: analyze_data(v) for k, v in grouped_by_page_ad.items()}

# Output samples
print("=== Overall Stats Sample ===")
print(json.dumps(dict(list(overall_stats.items())[:5]), indent=2))

print("\n=== Grouped by 'page_id' Sample ===")
print(json.dumps({str(k): v for k, v in list(stats_by_page.items())[:2]}, indent=2))

print("\n=== Grouped by 'page_id' and 'ad_id' Sample ===")
print(json.dumps({str(k): v for k, v in list(stats_by_page_ad.items())[:2]}, indent=2))

# Save outputs
with open(os.path.join(output_dir, "facebook_overall_stats.json"), "w", encoding="utf-8") as f:
    json.dump(overall_stats, f, indent=2)

with open(os.path.join(output_dir, "facebook_grouped_by_page_stats.json"), "w", encoding="utf-8") as f:
    json.dump({str(k): v for k, v in stats_by_page.items()}, f, indent=2)

with open(os.path.join(output_dir, "facebook_grouped_by_page_and_ad_stats.json"), "w", encoding="utf-8") as f:
    json.dump({str(k): v for k, v in stats_by_page_ad.items()}, f, indent=2)

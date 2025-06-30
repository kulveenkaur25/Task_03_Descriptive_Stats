import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Choose which dataset to visualize
DATASET_PATH = "datasets/twitter_ads.csv"  # Change to twitter_ads.csv or advertiser_spend.csv as needed
DATASET_NAME = "Twitter Ads"  # Update accordingly

# Load dataset
df = pd.read_csv(DATASET_PATH, low_memory=False)

# Select a few key numeric columns to visualize (edit based on dataset)
numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
numeric_cols = [col for col in numeric_cols if df[col].nunique() > 1][:3]  # First 3 valid ones

# Select a few categorical columns with < 100 unique values
categorical_cols = df.select_dtypes(include="object").nunique()
categorical_cols = categorical_cols[categorical_cols < 100].head(2).index.tolist()

# Display histograms for numeric columns
for col in numeric_cols:
    plt.figure()
    sns.histplot(df[col].dropna(), bins=30, kde=True)
    plt.title(f"{DATASET_NAME}: Histogram of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()

# Display bar plots for categorical columns
for col in categorical_cols:
    plt.figure()
    df[col].value_counts().head(10).plot(kind='bar')
    plt.title(f"{DATASET_NAME}: Top 10 Values of {col}")
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

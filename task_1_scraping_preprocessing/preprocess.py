import pandas as pd

df = pd.read_csv("task_1_scraping_preprocessing/reviews_raw.csv")

# Drop duplicates
df.drop_duplicates(subset="review", inplace=True)

# Drop empty
df.dropna(subset=["review"], inplace=True)

# Normalize dates
df["date"] = pd.to_datetime(df["date"]).dt.strftime('%Y-%m-%d')

# Save cleaned dataset
df.to_csv("data/final_reviews_clean.csv", index=False)

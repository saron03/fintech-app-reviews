from google_play_scraper import reviews, Sort
import pandas as pd

apps = {
    "Commercial Bank of Ethiopia": "com.combanketh.mobilebanking",
    "Bank of Abyssinia": "com.boa.boaMobileBanking",
    "Dashen Bank": "com.dashen.dashensuperapp"
}

all_reviews = []

for bank_name, app_id in apps.items():
    print(f"Fetching reviews for {bank_name}...")
    result, _ = reviews(
        app_id,
        lang='en',           # Language of reviews
        country='us',        # Country for the reviews
        sort=Sort.NEWEST,    # Sort by newest first
        count=400            # Number of reviews to fetch
    )
    for r in result:
        all_reviews.append({
            "review": r['content'],
            "rating": r['score'],
            "date": r['at'].strftime("%Y-%m-%d"),
            "bank": bank_name,
            "source": "Google Play"
        })

print(f"Total reviews scraped: {len(all_reviews)}")

df = pd.DataFrame(all_reviews)
df.to_csv("task_1_scraping_preprocessing/reviews_raw.csv", index=False)
print("Saved reviews to reviews_raw.csv")

from google_play_scraper import reviews, Sort
import pandas as pd

apps = {
    "CBE": "com.cbe.customerapp",
    "BOA": "com.boa.app",
    "Dashen": "com.dashen.app"
}

all_reviews = []

for bank, app_id in apps.items():
    result, _ = reviews(
        app_id,
        lang="en",
        country="us",
        sort=Sort.NEWEST,
        count=500
    )
    for r in result:
        all_reviews.append({
            "review": r["content"],
            "rating": r["score"],
            "date": r["at"].strftime('%Y-%m-%d'),
            "bank": bank,
            "source": "Google Play"
        })

df = pd.DataFrame(all_reviews)
df.to_csv("task_1_scraping_preprocessing/reviews_raw.csv", index=False)

from google_play_scraper import reviews, Sort

app_id = "com.combanketh.mobilebanking"  # CBE app ID

rvs, _ = reviews(
    app_id,
    lang='en',
    country='et',
    sort=Sort.NEWEST,
    count=100  # number of reviews to fetch
)

print(f"Fetched {len(rvs)} reviews")
print(rvs[:2])  # print first 2 reviews for a quick check

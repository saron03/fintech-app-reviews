import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("data/final_reviews_clean.csv")

tfidf = TfidfVectorizer(stop_words='english', max_features=100)
X = tfidf.fit_transform(df["review"])

keywords = tfidf.get_feature_names_out()

# Manual grouping (example)
themes = {
    "Access": ["login", "password", "access"],
    "Performance": ["slow", "lag", "crash"],
    "UX": ["interface", "design", "layout"],
    "Features": ["fingerprint", "transfer", "statement"]
}

def classify_theme(text):
    result = []
    for theme, words in themes.items():
        if any(word in text.lower() for word in words):
            result.append(theme)
    return result if result else ["Other"]

df["themes"] = df["review"].apply(classify_theme)
df.to_csv("task_2_sentiment_thematic/themes_results.csv", index=False)

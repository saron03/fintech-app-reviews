from textblob import TextBlob
import pandas as pd

df = pd.read_csv("data/final_reviews_clean.csv")

def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"

df["sentiment"] = df["review"].apply(get_sentiment)
df.to_csv("task_2_sentiment_thematic/sentiment_results.csv", index=False)

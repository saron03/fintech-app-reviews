import os
import sys
import matplotlib.pyplot as plt
import seaborn as sns
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from task4.analysis import load_data

def plot_sentiment_distribution(df):
    os.makedirs('task-4', exist_ok=True)
    
    plt.figure(figsize=(10,6))
    sns.countplot(data=df, x='sentiment', hue='bank_name')
    plt.title('Sentiment Distribution by Bank')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Reviews')
    plt.legend(title='Bank')
    plt.tight_layout()
    plt.savefig('task-4/sentiment_distribution.png')
    plt.show()
    plt.close()

def plot_rating_distribution(df):
    os.makedirs('task-4', exist_ok=True)
    
    plt.figure(figsize=(10,6))
    sns.histplot(data=df, x='rating', hue='bank_name', multiple='stack', bins=5)
    plt.title('Rating Distribution by Bank')
    plt.xlabel('Rating')
    plt.ylabel('Number of Reviews')
    plt.tight_layout()
    plt.savefig('task-4/rating_distribution.png')
    plt.show()
    plt.close()

if __name__ == "__main__":
    df = load_data()
    print(df.shape)
    print(df[['sentiment', 'bank_name', 'rating']].head())

    # Fix missing sentiment values by deriving from rating
    if df['sentiment'].isnull().all():
        df['sentiment'] = df['rating'].apply(
            lambda r: 'positive' if r >= 4 else ('neutral' if r == 3 else 'negative')
        )
    else:
        df['sentiment'] = df['sentiment'].fillna('unknown')

    plot_sentiment_distribution(df)
    plot_rating_distribution(df)

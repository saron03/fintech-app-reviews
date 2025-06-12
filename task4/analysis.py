from sqlalchemy import create_engine
import pandas as pd
from task3.db_config import DB_CONFIG

def load_data():
    # Build the connection string
    user = DB_CONFIG['user']
    password = DB_CONFIG['password']
    host = DB_CONFIG['host']
    port = DB_CONFIG['port']
    dbname = DB_CONFIG['dbname']

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')

    query = """
        SELECT b.name as bank_name, r.review_text, r.rating, r.review_date, r.sentiment, r.themes
        FROM reviews r
        JOIN banks b ON r.bank_id = b.id;
    """
    df = pd.read_sql(query, engine)
    return df

def main():
    df = load_data()
    print("\nRaw DataFrame sample:")
    print(df.head())
    
    # Fill NaNs before grouping (optional)
    df['sentiment'] = df['sentiment'].fillna('unknown')
    df['themes'] = df['themes'].fillna('unknown')

    print("\nSentiment count by bank:")
    print(df.groupby(['bank_name', 'sentiment']).size().unstack(fill_value=0))

    print("\nCommon themes by bank:")
    print(df.groupby(['bank_name', 'themes']).size().unstack(fill_value=0))

if __name__ == "__main__":
    main()

import psycopg2
from psycopg2 import sql
import csv
from db_config import DB_CONFIG
import csv
import psycopg2
from datetime import datetime

def get_bank_id(cur, bank_name):
    cur.execute("SELECT id FROM banks WHERE name = %s", (bank_name,))
    result = cur.fetchone()
    return result[0] if result else None

def insert_reviews(csv_path):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    inserted = 0
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            bank_name = row['bank']
            review_text = row['review']
            rating = int(row['rating'])
            review_date = datetime.strptime(row['date'], '%Y-%m-%d').date()
            source = row['source']
            sentiment = None  # Placeholder — to be filled in Task 4
            themes = None     # Placeholder — to be filled in Task 4

            bank_id = get_bank_id(cur, bank_name)
            if not bank_id:
                print(f"Bank not found: {bank_name}")
                continue

            cur.execute("""
                INSERT INTO reviews (bank_id, review_text, rating, review_date, sentiment, themes, source)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (bank_id, review_text, rating, review_date, sentiment, themes, source))
            inserted += 1

    conn.commit()
    cur.close()
    conn.close()
    print(f"Inserted {inserted} reviews.")

if __name__ == '__main__':
    insert_reviews('task-3/cleaned_reviews.csv')

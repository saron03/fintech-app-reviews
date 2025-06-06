# Fintech App Reviews – Customer Experience Analytics for Ethiopian Banks

## Project Overview

This project is part of the B5W2 data analytics challenge, where the goal is to analyze customer satisfaction with mobile banking apps for three major Ethiopian banks:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The project simulates a real-world consulting task at Omega Consultancy, focusing on data collection, sentiment analysis, and actionable insights from Google Play Store user reviews.

---

## Objectives

- Scrape at least 400 reviews for each bank's mobile app (1,200+ total).
- Preprocess and clean the data for analysis.
- Analyze sentiments and themes using NLP techniques.
- Identify customer satisfaction drivers and pain points.
- Store cleaned data in a structured format (CSV and Oracle DB).
- Visualize insights for stakeholders and deliver recommendations.

---

## Task 1: Data Collection & Preprocessing

### Tools & Libraries
- `google-play-scraper`: For scraping app reviews
- `pandas`: For data manipulation and preprocessing
- `datetime`: For date normalization

### Preprocessing Steps
1. Scraped reviews include: review text, rating, review date, app name, and source.
2. Removed duplicate reviews.
3. Dropped rows with missing review text or rating.
4. Normalized date format to `YYYY-MM-DD`.
5. Saved the cleaned data into a single CSV file (`cleaned_reviews.csv`).

---

## Repository Structure

    ├── .gitignore
    ├── requirements.txt
    ├── README.md
    ├── task_1/
    │ ├── scrape_reviews.py
    │ └── preprocess_reviews.py
    ├── data/
    │ └── cleaned_reviews.csv


---

## Branching Strategy

- `main`: Stable code for final deliverables
- `task-1`: Code for data scraping and preprocessing (current focus)
- `task-2`: Sentiment analysis and theme extraction
- `task-3`: Visualization and reporting

---

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Run the scraping script:

    ```bash
    python scrape_reviews.py

3. Run the preprocessing script:
    ```bash
    python preprocess_reviews.py

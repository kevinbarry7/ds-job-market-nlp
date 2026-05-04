import requests
import json
import os
import time
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("RAPIDAPI_KEY")

url = "https://jsearch.p.rapidapi.com/search"
headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

# Search terms to cover the DS/ML market broadly
search_terms = [
    "data scientist remote",
    "machine learning engineer remote",
    "data analyst remote",
    "NLP engineer remote",
    "MLOps engineer remote"
]

all_jobs = []

for term in search_terms:
    print(f"Fetching: {term}")
    params = {
        "query": term,
        "page": "1",
        "num_pages": "2",
        "date_posted": "month"
    }
    response = requests.get(url, headers=headers, params=params)
    jobs = response.json().get('data', [])
    all_jobs.extend(jobs)
    print(f"  Got {len(jobs)} jobs")
    time.sleep(1)  # be polite to the API

print(f"\nTotal jobs collected: {len(all_jobs)}")

# Save to JSON for later use
with open('jobs_raw.json', 'w') as f:
    json.dump(all_jobs, f, indent=2)

print("Saved to jobs_raw.json")

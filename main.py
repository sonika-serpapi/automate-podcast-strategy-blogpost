from serpapi import GoogleSearch
import os, json
from dotenv import load_dotenv
load_dotenv()

api_key = os.environ["SERPAPI_API_KEY"]

topic = "Algorithmic bias with AI" # Change this to your topic of interest
related_topic_for_google_trends = "AI bias in healthcare" # Change this to your topic of interest

params = {
  "q": topic,
  "api_key": api_key,
  "engine": "google",
  "google_domain": "google.com",
  "gl": "us",
  "hl": "en",
  "location": "Austin, Texas, United States",
  "device": "desktop"
}

search = GoogleSearch(params)
results = search.get_dict()
related_questions = results["related_questions"]
print("RELATED QUESTIONS:")
for block in related_questions:
    print(block["question"])

params = {
  "q": topic,
  "api_key": api_key,
  "engine": "google",
  "google_domain": "google.com",
  "gl": "us",
  "hl": "en",
  "location": "Austin, Texas, United States",
  "device": "desktop"
}

search = GoogleSearch(params)
results = search.get_dict()
related_searches = results["related_searches"]
print("RELATED SEARCHES:")
for block in related_searches:
    print(block["query"])

params = {
  "api_key": api_key,
  "engine": "google_trends",
  "q": topic + "," + related_topic_for_google_trends,
  "data_type": "TIMESERIES",
  "hl": "en",
  "geo": "US"
}

search = GoogleSearch(params)
results = search.get_dict()

# This provides two kinds of data - timeline_data and averages, which you can select depending on your use case
interest_over_time_results = results["interest_over_time"]
print("GOOGLE TRENDS DATA:")
print(interest_over_time_results["averages"])

params = {
  "api_key": api_key,
  "engine": "google_news",
  "q": topic,
  "hl": "en",
  "geo": "US"
}

search = GoogleSearch(params)
results = search.get_dict()

print("NEWS RESULTS:")
news_results = results["news_results"]
for i in range(len(news_results)):
    print("Result ", i + 1, ":")
    print("Title:", news_results[i]["title"])
    print("Link:", news_results[i]["link"])

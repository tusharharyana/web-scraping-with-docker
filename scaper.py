import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

def scrape_data():
    url = "https://www.google.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    titles = soup.find_all('h2') 

    # Connect to MongoDB Atlas
    mongo_uri = "mongodb+srv://admin:admin@cluster0.di279.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0" 
    client = MongoClient(mongo_uri)
    db = client["web_scraping_db"]
    collection = db["scraped_data"]

    # Save scraped data to MongoDB
    for title in titles:
        collection.insert_one({"title": title.text.strip()})

    print("Scraping complete and data saved to MongoDB Atlas!")

if __name__ == "__main__":
    scrape_data()

import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError


def scrape_data():
    url = "https://meet.google.com/"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch the webpage: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    titles = soup.find_all('head')
    

    mongo_uri = "mongodb+srv://admin:admin@cluster0.di279.mongodb.net/web_scraping_db?retryWrites=true&w=majority&appName=Cluster0" 
    try:
        # Connect to MongoDB Atlas
        client = MongoClient(mongo_uri)
        db = client["web_scraping_db"]
        collection = db["scraped_data"]

        # Save scraped data to MongoDB
        for title in titles:
            collection.insert_one({"title": title.text.strip()})

        print("Scraping complete and data saved to MongoDB Atlas!")

    except ServerSelectionTimeoutError:
        print("Error connecting to MongoDB Atlas. Please check your connection string or network.")

if __name__ == "__main__":
    scrape_data()

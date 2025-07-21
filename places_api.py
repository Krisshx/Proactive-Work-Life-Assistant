# places_api.py

import requests
import os
from dotenv import load_dotenv

load_dotenv()
FOURSQUARE_API_KEY = os.getenv("FOURSQUARE_API_KEY")
BASE_URL = "https://api.foursquare.com/v3/places/search"

def search_restaurants(location: str, cuisine: str, limit=5):
    headers = {
        "Accept": "application/json",
        "Authorization": f"{FOURSQUARE_API_KEY}"
    }

    params = {
        "query": cuisine,
        "near": location,
        "limit": limit,
        "categories": "13065"
    }

    response = requests.get(BASE_URL, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        restaurants = []
        for place in data.get("results", []):
            restaurants.append({
                "name": place.get("name"),
                "address": place.get("location", {}).get("formatted_address", "N/A"),
                "distance": place.get("distance", "N/A")
            })
        return restaurants
    else:
        print("Error:", response.status_code, response.text)
        return []

    if response.status_code != 200:
        raise ValueError(f"Foursquare API error: {response.status_code} - {response.text}")

    data = response.json()
    restaurants = []
    for place in data.get("results", []):
        restaurants.append({
            "name": place.get("name"),
            "address": place.get("location", {}).get("formatted_address", "N/A"),
            "distance": place.get("distance", "N/A")
        })
    return restaurants
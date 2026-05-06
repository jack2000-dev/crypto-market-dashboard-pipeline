from log import logger
import requests

BASE_URL = "https://api.coingecko.com/api/v3"

params = {
  "per_page": "10",
  "vs_currency": "usd",
}

def fetch_data() -> list:
    response = requests.get(f"{BASE_URL}/coins/markets", params=params)

    if response.status_code == 200:
        data = response.json()
        logger.info("Extract Completed")
        return data
    else:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")
from log import logger
import requests
import os
from pathlib import Path
from dotenv import load_dotenv

# API handling
load_dotenv(Path(__file__).resolve().parent.parent / ".env")
API_KEY = os.getenv("API_KEY")

BASE_URL = "https://api.coingecko.com/api/v3"

HEADERS = {
    "x-cg-demo-api-key": API_KEY
}



def fetch_market() -> list:
    response = requests.get(
        f"{BASE_URL}/coins/markets",
        headers=HEADERS,
        params={"per_page": "10", "vs_currency": "usd"},
    )

    if response.status_code == 200:
        market = response.json()
        logger.info("Extract: Market")
        return market
    else:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")


def fetch_ohlc(id: str, vs_currency: str, days: int) -> list:
    response = requests.get(
        f"{BASE_URL}/coins/{id}/ohlc",
        headers=HEADERS,
        params={"days": days, "vs_currency": vs_currency},
    )

    if response.status_code == 200:
        ohlc = response.json()
        logger.info("Extract: OHLC")
        return ohlc
    else:
        raise Exception(f"Failed to fetch OHLC. Status code: {response.status_code}")

    
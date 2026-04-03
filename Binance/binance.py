import requests
import json
from pprint import pprint
from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

client = MongoClient("mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@server.example.com/?connectTimeoutMS=300000&authSource=aDifferentAuthDB")

db = client['binance']

 
BASE_URL = "https://api.binance.com/api/v3"

def get_binance_data(endpoint,params=None,collection_name=None):
    url = f"{BASE_URL}/{endpoint}"
    response = requests.get(url,params=params)
    data = response.json()
    pprint(data)
    
    # Convert to list if necessary for MongoDB insertion
    if isinstance(data, dict):
        data = [data]
    elif isinstance(data, list) and len(data) > 0 and isinstance(data[0], list):
        # If it's a list of lists (e.g., klines), wrap into dicts
        data = [dict(kline=k) for k in data]

    if collection_name:
        print(f"Inserting into collection: {collection_name}")
        collection = db[collection_name]
        #collection.delete_many({})  # optional: clear old data
        collection.insert_many(data)
        print(f"[✓] Inserted into {collection_name}")

    return data
    
    

print("Step 1 complete!")
 
def get_24hr_ticker():
    return get_binance_data("ticker/24hr", collection_name="24hr_ticker")


def ticker_price():
    return get_binance_data("ticker/price", collection_name="price")


def klines():
    params = {"symbol": "BTCUSDT", "interval": "1m", "limit": 20}
    return get_binance_data("klines", params=params, collection_name="klines")


def depth():
    params = {"symbol": "BTCUSDT", "limit": 20}
    return get_binance_data("depth", params=params, collection_name="depth")


def trade():
    params = {"symbol": "BTCUSDT", "limit": 20}
    return get_binance_data("trades", params=params, collection_name="trade")

print("Starting to fetch binance data and storage.")


get_24hr_ticker()
ticker_price()
klines()
depth()
trade()

print("All data fetched and stored in MongoDB!")


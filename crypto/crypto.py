import os
from airflow import DAG
import requests
from dotenv import load_dotenv
from airflow.operators.python import PythonOperator
import pandas as pd
from datetime import datetime, timedelta
from pymongo import MongoClient

# Load environment variables
load_dotenv()
API_KEY = os.getenv('crypto_api_key') 


def fetch_crypto(**kwargs):
    """Fetch cryptocurrency prices from CoinGecko and push to XCom"""
    COINS = ["bitcoin", "ethereum", "tether", "binancecoin", "solana", 
             "dogecoin", "tron", "cardano", "polkadot", "litecoin", 
             "avalanche-2", "chainlink", "stellar", "uniswap", "monero"]

    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'ids': ','.join(COINS),
        'vs_currency': 'usd'
    }
    headers = {"accept": "application/json"}

    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    # Transform to DataFrame
    df = pd.DataFrame(data)[['id', 'current_price']]  # only keep relevant columns
    df = df.rename(columns={'id': 'coin', 'current_price': 'price_usd'})

    # Push to XCom
    kwargs['ti'].xcom_push(key='crypto_df', value=df.to_json(orient='records'))
    print("Fetched crypto data and pushed to XCom")


def store_crypto(**kwargs):
    """Retrieve crypto prices from XCom and store in MongoDB"""
    json_str = kwargs['ti'].xcom_pull(key='crypto_df', task_ids='fetch_crypto')
    df = pd.read_json(json_str)

    # Push to MongoDB
    MONGO_URL = "mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@server.example.com/?connectTimeoutMS=300000&authSource=aDifferentAuthDB"
    client = MongoClient(MONGO_URL)
    db = client["CoinGecko"]
    collection = db["crypto_prices"]

    collection.insert_many(df.to_dict(orient='records'))
    print("Crypto data stored in MongoDB successfully!")


# DAG Definition

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 5, 20),
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='crypto_dag',
    schedule_interval='@daily',
    default_args=default_args,
    catchup=False,
    tags=['data_engineering', 'portfolio']
) as dag:

    fetch = PythonOperator(
        task_id='fetch_crypto',
        python_callable=fetch_crypto,
        provide_context=True
    )

    store = PythonOperator(
        task_id='store_crypto',
        python_callable=store_crypto,
        provide_context=True
    )

    fetch >> store
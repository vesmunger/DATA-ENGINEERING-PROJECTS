import requests
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator

load_dotenv()

api_key=os.getenv('api_key')
city_name= 'your_city'

def fetch_weather():
    url=(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")

    response = requests.get(url)

    data=response.json()

    print(response.status_code)

    df = pd.DataFrame([data])

    weather_csv='df.csv'
    df.to_csv(weather_csv,index=False)
    print(f'all good!')
    
def store_weather():
    #Push the data into Mongodb
    client = MongoClient("mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@server.example.com/?connectTimeoutMS=300000&authSource=aDifferentAuthDB")

    db=client["Openweather"]
    collection = db["daily_data"]

    collection.insert_many(df.to_dict(orient='records'))
    print(f"Weather Data inserted into MongoDB successfully!")
    

# user=os.getenv('avnadmin')
# password=os.getenv('your_password')
# host=os.getenv('your_host')
# port=os.getenv('port')
# database=os.getenv('dyour_db')

# engine=create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")

# df.to_sql('weather_data', conn=engine, if_exists='replace', index=False)
# print("Data pushed to PostgreSQL table")


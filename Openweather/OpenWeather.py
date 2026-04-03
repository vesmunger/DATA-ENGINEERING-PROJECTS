#Import the necessary Libraries
import requests #to read data from URLs
import pandas as pd #To manipulaate data
from sqlalchemy import create_engine #To connect to a sql DB
import os # To Connect to our dotenv file(passwords,api_keys)
from dotenv import load_dotenv #load our dotenv files

load_dotenv()

api_key=os.getenv('open_weather_api_key')
city_name= 'Nairobi'

url=(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")

response = requests.get(url)

data=response.json()

print(response.status_code)

df = pd.DataFrame([data])

weather_csv='df.csv'
df.to_csv(weather_csv,index=False)
print(f'all good!')

USER = 'user'
PASSWORD = 'your_password'
HOST = 'host'
PORT = 'port'
DATABASE = 'your_db'

engine=create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")

df.to_sql('weather_data', conn=engine, if_exists='replace', index=False)
print("Data pushed to PostgreSQL table") 
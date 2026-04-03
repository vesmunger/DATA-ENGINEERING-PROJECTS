# Gas prices from https://collectapi.com/
import http.client
import json
import pandas as pd
from pymongo import MongoClient
# Uncomment if using PostgreSQL
# from sqlalchemy import create_engine


# Step 1: Fetch Data from API

API_HOST = "api.collectapi.com"
API_KEY = "your_api_key" 
STATE = "WA"

conn = http.client.HTTPSConnection(API_HOST)

headers = {
    'content-type': "application/json",
    'authorization': f"Bearer {API_KEY}"
}

# Request data for the state
conn.request("GET", f"/gasPrice/stateUsaPrice?state={STATE}", headers=headers)
res = conn.getresponse()
data = res.read()

# Parse JSON
parsed_data = json.loads(data)
cities_data = parsed_data['result']['cities']

# Step 2: Load into DataFrame

df = pd.DataFrame(cities_data)

# Drop unnecessary columns and rename for clarity
df = df.drop(columns=['lowerName'], errors='ignore') 
df = df.rename(columns={'name': 'city'})
print(df.head())

# Step 3: Push to MongoDB

MONGO_URI = "mongodb+srv://myDatabaseUser:D1fficultP%40ssw0rd@server.example.com/?connectTimeoutMS=300000&authSource=aDifferentAuthDB"
client = MongoClient(MONGO_URI)

db = client["CollectAPI"]
collection = db["gas_prices"]

# Insert data as documents
collection.insert_many(df.to_dict(orient='records'))
print("Data inserted into MongoDB successfully!")

# Optional: Push to PostgreSQL

# Uncomment and configure your PostgreSQL credentials if needed
# USER = 'user'
# PASSWORD = 'your_password'
# HOST = 'host'
# PORT = 'port'
# DATABASE = 'your_db'
# 
# engine = create_engine(f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')
# 
# df.to_sql(
#     'gas_prices',
#     engine,
#     if_exists='replace',  # or 'append' if you want to add data
#     index=False
# )
# print("Data inserted into PostgreSQL successfully!")
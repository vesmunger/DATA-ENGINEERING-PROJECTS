import requests
import os
from dotenv import load_dotenv
from kafka import KafkaProducer
import time
import json


load_dotenv()
api_key = os.getenv('api_key')

producer = KafkaProducer(
    bootstrap_servers = 'localhost:9092',
    value_serializer = lambda v:json.dumps(v).encode('utf-8')
    
)

city = 'Nairobi'

def get_weather(city):
    url=(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        return {
            'city':data['name'],
            'country':data['sys']['country'],
            'description':data['weather'][0]['description'],
            'temperature':data['main']['temp']
            
        }
    else:
        print('error fetching weather data')
        return None
while True:
    weather = get_weather(city)
    if weather:
        producer.send('weather', value = weather)
        print('produced:', weather)
time.sleep(5)
    
    
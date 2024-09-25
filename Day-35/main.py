import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("api_key")
OWM_Endpoint = os.getenv("OWM_Endpoint")
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")


MY_LAT = os.getenv("MY_LAT")
MY_LONG = os.getenv("MY_LONG")

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
#print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an umbrella☂️",
            from_='whatsapp:+14155238886',
            to='whatsapp:+2348139960891'
        )
elif will_rain == False:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="No rain today🌞",
            from_='whatsapp:+14155238886',
            to='whatsapp:+2348139960891'
        )
        
print(message.status)
8
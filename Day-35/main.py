import requests
from twilio.rest import Client

api_key = "6ee52075448474a4dc144f1287b99b2b"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "AC2b6ba7f133386292eff0c36c634a9e83"
auth_token = "d4273665fdfa70823390c4cd90e58a82"


MY_LAT = -40.468410
MY_LONG =175.289261
# MY_LAT = 9.076479
# MY_LONG = 7.398574

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
            body="It's going to rain today. Remember to bring an umbrella",
            from_='whatsapp:+14155238886',
            to='whatsapp:+2348139960891'
        )
else:
    print("No rain today")
        
print(message.status)
8
import os
import requests
from pprint import pprint
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/ad99b3b39230f295fbc8127f314e8ac9/copyofFlightDeals/prices"
load_dotenv()


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._user = os.getenv("SHEETY_USERNAME")
        self._password = os.getenv("SHEETY_PASSWORD")
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        
    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self._authorization)
        data = response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=self._authorization
            )
            # print(response.text)
            
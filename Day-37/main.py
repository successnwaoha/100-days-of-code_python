import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")
GRAPH_ID = os.getenv("GRAPH_ID")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Coding Graph",
    "unit" : "hours",
    "type" : "float",
    "color" : "momiji"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
#year=2024, month=7, day=26
print(today.strftime("%Y%m%d"))

pixel_data = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : input("How many hours did you learn today? ")
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

pixel_update_data = {
    "quantity" : "9.0"
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
print(response.text)
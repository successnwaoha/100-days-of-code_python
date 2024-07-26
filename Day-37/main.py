import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "sertyujnhbvdse456y7u",
    "username": "success",
    "agreeTermsOfService": "yes"
    "notMinor": "yes"
}

requests.post(url=pixela_endpoint, json=user_params)
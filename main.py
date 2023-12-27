# Pixela website - https://pixe.la/
# Pixela API documentation - https://docs.pixe.la/
# Make sure to install when you get error while creating account on pixela - pip install chardet
# Check it on - https://pixe.la/v1/users/{username}/graphs/{graphid}.html

from datetime import *
import os
import requests

USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
GRAPH_ID = os.environ.get("GRAPH_ID")

################################################# POST REQUESTS ###############################################

# Create account by making post request
pixela_endpoint = "https://pixe.la/v1/users"

req_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=req_params)
# print(response.text)

# Authenticate yourself using header
headers = {
    "X-USER-TOKEN": TOKEN
}

# Create graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",

}

#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# today = datetime(year=2023, month=12, day=25).strftime('%Y%m%d')
today = datetime.now().strftime('%Y%m%d')
print(today)
# Create pixel
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config = {
    "date": today,
    "quantity": "17"
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
print(response.text)

################################################# PUT REQUESTS ###############################################

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
update_pixel_config = {
    "quantity": "2"
}
# update_response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(update_response.text)

################################################# DELETE REQUESTS ###############################################
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
# delete_response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(delete_response)

import requests
import datetime as dt

TOKEN = "wu87wf76cc5c6dd0"
USERNAME = "hubsterrr"
GRAPH_ID = "graph10"

pixella_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN
}

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixella_endpoint, json=user_params)
# print(response)
#
graph_endpoint = f"{pixella_endpoint}/{USERNAME}/graphs"
#
#
# graph_params = {
#     "id": GRAPH_ID,
#     "name": "Coding Time Graph",
#     "unit": "Hours",
#     "type": "int",
#     "color": "sora",
# }

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

today = dt.datetime.now()
today_str = today.strftime("%Y%m%d")

post_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

pixel_params = {
    "date": today_str,
    "quantity": "2",
}

# response = requests.post(url=post_pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)


pixel_update_endpoint = f"{post_pixel_endpoint}/{today_str}"

pixel_update_params = {
    "quantity": "4",
}

response = requests.put(url=pixel_update_endpoint, json=pixel_update_params, headers=headers)
print(response.text)

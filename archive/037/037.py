# habbit-tracker

import datetime as dt
import requests


# -------------------------- CONFIG ------------------------------------ #

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "pratikkabade"
TOKEN = "asdbhfuyhhbaihif"
GRAPH_ID = "graph1"
HEADER = {
    "X-USER-TOKEN": TOKEN
}

# -------------------------------- CREATE USER ------------------------------------------ #

CREATE_USER_ENDPOINT = PIXELA_ENDPOINT
PARAMS_USER = {
    "token": "asdbhfuyhhbaihif",
    "username": "pratikkabade",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=CREATE_USER_ENDPOINT, json=PARAMS_USER)
# print(response.text)


# -------------------------------- CREATE GRAPH ------------------------------------------ #

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PARAMS_GRAPH = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai"
}
# response = requests.post(url=GRAPH_ENDPOINT, json=PARAMS_GRAPH, headers=HEADER)
# print(response.text)


# -------------------------------- SUPPORT PIXEL ------------------------------------------ #

SUPPORT_ENDPOINT = f"{PIXELA_ENDPOINT}/a-know"
PARAMS_SUPPORT = {
    "thanksCode": "ThisIsThanksCode"
}
# response = requests.post(url=SUPPORT_ENDPOINT, json=PARAMS_SUPPORT)
# print(response.text)


# -------------------------------- TODAY'S DATE ------------------------------------------ #

old_date = dt.datetime(year=2023, month=1, day=25)
today = dt.datetime.now()


# -------------------------------- CREATE PIXEL ------------------------------------------ #

CREATE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
PARAMS_CREATE_PIXEL = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code Today?")
}
# response = requests.post(url=CREATE_PIXEL_ENDPOINT, json=PARAMS_CREATE_PIXEL, headers=HEADER)
# print(response.text)


# -------------------------------- UPDATE PIXEL ------------------------------------------ #

DATE_TO_UPDATE = 20230125
UPDATE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{DATE_TO_UPDATE}"
PARAMS_UPDATE_PIXEL = {
    "quantity": "1"
}
# response = requests.put(url=UPDATE_PIXEL_ENDPOINT, json=PARAMS_UPDATE_PIXEL, headers=HEADER)
# print(response.text)


# -------------------------------- DELETE PIXEL ------------------------------------------ #

DATE_TO_DELETE = 20230126
DELETE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{DATE_TO_DELETE}"

# response = requests.delete(url=DELETE_PIXEL_ENDPOINT, headers=HEADER)
# print(response.text)

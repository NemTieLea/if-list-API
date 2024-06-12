# Windows:  pip freeze | Add-Content requirements.txt
# Unix : pip freeze > requirements.txt
# pip install requests

import requests
import json
from pprint import pprint


def extract_user_data_from_response(user_response):
    return {
        "title:": user_response["name"]["title"],
        "last_name": user_response["name"]["last"],
        "city": user_response["location"]["city"],
        "password": user_response["login"]["password"]
    }


API_URL = 'https://randomuser.me/api/'

params = {
    "results": 6,
    "gender": "female",
    "password": "upper,lower,number,special,12-16",
    "seed": "fc",
}

resp = requests.get(API_URL, params=params)

user_data = [extract_user_data_from_response(r) for r in resp.json()['results']]
pprint(user_data)

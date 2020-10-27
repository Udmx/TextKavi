import requests
import json
from textkavi.config import API_KEY, url_authentication


class Authentication:
    ##################### Get Token by Api Key ##########################
    def get_token_key(self):
        querystring = {"apikey": API_KEY}
        response = requests.request("GET", url_authentication, params=querystring)
        data = json.loads(response.text)
        return data['token']

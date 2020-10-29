import requests
import json
from textkavi.config import API_KEY, url_authentication


class Authentication:
    # Get Token by Api Key
    def __init__(self):
        self.token = ''

    def get_token_key(self):
        response = requests.request(
            "GET", url_authentication, params={'apikey': API_KEY}
        )
        self.token = json.loads(response.text)['token']


auth = Authentication()
auth.get_token_key()

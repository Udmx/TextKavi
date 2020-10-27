import requests

from textkavi.Authentication import Authentication
from textkavi.config import url_formal_converter


class FormalConverter:
    def get_formal_converter(self):
        auth = Authentication()
        token = auth.get_token_key()
        input_text = input("Please write text (farsi or english):")
        data = '\"' + str(input_text) + '\"'
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + token,
            'Cache-Control': "no-cache"
        }
        response = requests.request("POST", url_formal_converter, data=data.encode("utf-8"), headers=headers)
        return response.text

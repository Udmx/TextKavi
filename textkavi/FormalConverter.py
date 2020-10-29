import requests
from textkavi.Authentication import auth
from textkavi.config import url_formal_converter


class FormalConverter:
    def __init__(self):
        self.text = ''

    def get_formal_converter(self):

        input_text = input("Please write text (farsi or english):").strip()
        data = '\"' + input_text + '\"'

        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + auth.token,
            'Cache-Control': "no-cache"
        }

        response = requests.request(
            "POST", url_formal_converter,
            data=data.encode("utf-8"), headers=headers
        )

        self.text = response.text


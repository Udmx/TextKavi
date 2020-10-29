import json
import requests

from textkavi.Authentication import auth
from textkavi.config import url_recognize_vulgar_words


class RecognizeVulgarWords:
    def __init__(self):
        self.curse_list = list()

    def get_recognize_vulgar_words(self):

        input_text = input("Please write text (farsi or english):").strip()
        data = '\"' + input_text + '\"'

        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + auth.token,
            'Cache-Control': "no-cache"
        }
        response = requests.request(
            "POST",
            url_recognize_vulgar_words,
            data=data.encode("utf-8"),
            headers=headers
        )
        result = json.loads(response.text)

        for res in result:
            self.curse_list.append(res)

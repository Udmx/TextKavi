import json

import requests

from textkavi.Authentication import Authentication
from textkavi.config import url_recognize_vulgar_words

class RecognizeVulgarWords:
    def get_recognize_vulgar_words(self):
        auth = Authentication()
        token = auth.get_token_key()
        input_text = input("Please write text (farsi or english):")
        data = '\"' + str(input_text) + '\"'
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + token,
            'Cache-Control': "no-cache"
        }
        response = requests.request("POST", url_recognize_vulgar_words, data=data.encode("utf-8"), headers=headers)
        result = json.loads(response.text)
        list_word = list()
        for res in result:
           list_word.append(res)
        return list_word
import requests
import json

from textkavi.Authentication import Authentication
from textkavi.config import url_sensory_analysis


class SensoryAnalysis:
    def get_sence_sentence(self):
        auth = Authentication()
        token = auth.get_token_key()
        input_text = input("Please write text (farsi or english):")
        data = '\"' + str(input_text) + '\"'
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + token,
            'Cache-Control': "no-cache"
        }
        response = requests.request("POST", url_sensory_analysis, data=data.encode("utf-8"), headers=headers)
        result = response.text
        if result == '2':
            return "Hese +"
        elif result == '1':
            return "Hese khonsa"
        elif result == '0':
            return "Hese -"

import requests

from textkavi.Authentication import auth
from textkavi.config import url_sensory_analysis


class SensoryAnalysis:
    def __init__(self):
        self.feel = None

    def get_feel_sentence(self):
        input_text = input("Please write text (farsi or english):")
        data = '\"' + str(input_text) + '\"'
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + auth.token,
            'Cache-Control': "no-cache"
        }
        response = requests.request(
            "POST",
            url_sensory_analysis,
            data=data.encode("utf-8"),
            headers=headers
        )
        result = response.text
        if result == '2':
            self.feel = "Hese +"
        elif result == '1':
            self.feel = "Hese khonsa"
        elif result == '0':
            self.feel = "Hese -"

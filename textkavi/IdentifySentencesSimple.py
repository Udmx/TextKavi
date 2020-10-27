import requests
import json
from textkavi.config import API_KEY, url_identifySentencesSimple
from textkavi.Authentication import Authentication


class IdentifySentencesSimple:

    def get_list_identify_sentences(self, check_slang=True, normalize=True,
                                    complex_sentence=True):
        auth = Authentication()
        token = auth.get_token_key()
        input_text = input("Please write text (farsi or english):")
        data = str({
            'text': str(input_text), 'checkSlang': str(check_slang), 'normalize': str(normalize),
            'complexSentence': str(complex_sentence)
        })
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + token,
            'Cache-Control': "no-cache"
        }
        response = requests.request("POST", url_identifySentencesSimple, data=data.encode("utf-8"), headers=headers)
        return response.text

    def getـisolatedـlist(self, check_slang=True, normalize=True,
                          complex_sentence=True):
        obj = IdentifySentencesSimple()
        list_text = obj.get_list_identify_sentences(check_slang=check_slang, normalize=normalize,
                                                    complex_sentence=complex_sentence)
        counter = 1
        for exe in eval(list_text):
            print(str(counter), ':', exe)
            counter += 1

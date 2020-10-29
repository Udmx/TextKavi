import requests
from textkavi.config import url_identifySentencesSimple
from textkavi.Authentication import auth


class IdentifySentencesSimple:
    def __init__(self):
        self.list_text = list()
        self.count_text = ''

    def get_list_identify_sentences(self, check_slang=True, normalize=True,
                                    complex_sentence=True):

        input_text = input("Please write text (farsi or english):").strip()
        data = str({
            'text': input_text,
            'checkSlang': str(check_slang),
            'normalize': str(normalize),
            'complexSentence': str(complex_sentence)
        })

        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + auth.token,
            'Cache-Control': "no-cache"
        }

        response = requests.request(
            "POST",
            url_identifySentencesSimple,
            data=data.encode('utf-8'),
            headers=headers
        )

        self.list_text = eval(response.text)

    def get_isolated_list(self):
        counter = 1

        for exe in self.list_text:
            self.count_text += f'{counter}: {exe}\n'
            counter += 1

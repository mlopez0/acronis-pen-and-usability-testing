import requests
import json
import pprint


class ApiBase:
    def __init__(self):
        pass

    def get(self, url, expected_code=200, **kwargs):
        response = requests.get(url, **kwargs)

        if not response.status_code == expected_code:
            raise Exception(f'Response: {response.status_code} | {response.json()}')

        return response.json()

    def post(self, url, expected_code=200, **kwargs):
        response = requests.post(url, **kwargs)

        if not response.status_code == expected_code:
            raise Exception(f'Response: {response.status_code} | {response.json()}')

        return response.json()
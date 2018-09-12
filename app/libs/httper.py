import requests


class Http(object):

    @staticmethod
    def get(url, params=None, data=None, return_json=True):
        response = requests.get(url, params=params, data=data)

        if response.status_code == 404:
            return None
        if return_json:
            return response.json()
        else:
            return response.text

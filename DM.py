import os
import json
import requests
from instapi.client import client

class DM:
    cookie = ''

    def __init__(self):
        for cookie in client.obj.cookie_jar:
            if cookie.name == 'csrftoken':
                self.csrf = cookie.value
            self.cookie += f'{cookie.name}={cookie.value}; '

        self.headers = {
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': self.cookie,
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.277',
            'x-asbd-id': '437806',
            'x-csrftoken': self.csrf,
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR0k9m2HW_nPQhYTXtxXPmFsBiV8xAZ_1IfrhbxRguU3UDMV',
            'x-instagram-ajax': '8c4f274ffe7f'
        }

    def create(self, users):
        users_list = ','.join([f'"{user}"' for user in users])
        url = "https://i.instagram.com/api/v1/direct_v2/create_group_thread/"
        payload = f'recipient_users=[{users_list}]'
        response = requests.request("POST", url, headers=self.headers, data=payload)
        print(response.text)

    def send(self):
        ...
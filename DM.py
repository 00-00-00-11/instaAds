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
            'Cookie': self.cookie,
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Instagram 76.0.0.15.395 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930F; herolte; samsungexynos8890; en_US; 138226743)',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Connection-Speed': '3555kbps',
            'X-IG-App-ID': '567067343352427',
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-FB-HTTP-Engine': 'Liger',
        }

    def create(self, users):
        users_list = ','.join([f'"{user}"' for user in users])
        url = "https://i.instagram.com/api/v1/direct_v2/create_group_thread/"
        payload = f'recipient_users=[{users_list}]'
        response = requests.request("POST", url, headers=self.headers, data=payload)

        try:
            self.thread_id = json.loads(response.text)['thread_id']
        except:
            return False

    def send(self, message, type='text'):
        if type == 'text':
            self.send_text(message)
        elif type == 'link':
            self.send_link(message)

    def send_text(self, text):
        url = "https://i.instagram.com/api/v1/direct_v2/threads/broadcast/text/"
        payload = {
            '_csrftoken': self.csrf,
            '_uuid': '8ac7d712-f428-11eb-9e56-ef1f9492b890',
            '_uid': '11949406014',
            'action': 'send_item',
            'thread_ids': f'["{self.thread_id}"]',
            'text': text
        }
        response = requests.request("POST", url, headers=self.headers, data=payload)
        if response.status_code == 200:
            return True
        return False

    def send_link(self, link):
        url = "https://i.instagram.com/api/v1/direct_v2/threads/broadcast/link/"
        payload = {
            '_csrftoken': self.csrf,
            '_uuid': '8ac7d712-f428-11eb-9e56-ef1f9492b890',
            '_uid': '11949406014',
            'action': 'send_item',
            'thread_ids': f'["{self.thread_id}"]',
            'link_text': link,
            'link_urls': f'["{link}"]'
        }
        response = requests.request("POST", url, headers=self.headers, data=payload)
        if response.status_code == 200:
            return True
        return False
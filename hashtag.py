import json
import requests
from DM import DM
from database import DataBase

class HashTag(DM):
    def __init__(self, tag):
        super().__init__()
        self.tag = tag
        page = 0
        count = 0
        count_posts = self.count_posts()
        print(str(count_posts) + " Posts Available")

        url = f"https://i.instagram.com/api/v1/tags/{self.tag}/sections/"
        payload = {
            'page': page,
            'tab': 'recent',
            'surface': 'grid',
            'include_persistent': 0
        }

        while count_posts >= count:
            print(f"\nFetching Page {page+1}")
            payload['page'] = page
            response = requests.request("POST", url, headers=self.headers, data=payload)
            data = json.loads(response.text)
            if data['more_available']:
                payload['max_id'] = data['next_max_id']

            for section in data['sections']:
                for media in section['layout_content']['medias']:
                    media = media['media']
                    user = media['user']
                    add_user(user['username'], user['pk'])
                    count += 1

            page += 1
            if not data['more_available']:
                print("No more posts available")
                break

        print("Done.")

    def count_posts(self):
        url = f"https://www.instagram.com/explore/tags/{self.tag}/?__a=1"
        response = requests.request("GET", url, headers=self.headers)
        try:
            return json.loads(response.text)['data']['media_count']
        except:
            print("\033[31m"+"\nCounting Posts Failed\n"+"\033[0m")
            exit()

def add_user(username, user_id):
    if not DataBase.Status(user_id):
        print(f"Adding {username} to database")
        newUser = DataBase(username, user_id, 0)
        newUser.GoToDB()
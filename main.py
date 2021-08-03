import os
import json
from DM import DM
from instapi import bind
from instapi import User
from database import DataBase
from dotenv import load_dotenv; load_dotenv()

username = os.getenv('username')
password = os.getenv('password')

print('Login...')
bind(username, password)

print(f"{DataBase.nCount()}/{DataBase.Count()} Users\n")
print("1- Get followers")
print("2- Send group message")

choice = int(input("Choose by number: "))

if choice == 1:
    target_username = input("\nUsername to get followers: ")
    followers = User.from_username(target_username).followers()

    for follower in followers:
        if not DataBase.Status(follower.pk):
            print(f"Adding {follower.username} to database")
            newUser = DataBase(follower.username, follower.pk, 0)
            newUser.GoToDB()
elif choice == 2:
    dm = DM()
    for user in DataBase.GetFromDB():
        if not user[-1]:
            ch_result = dm.create([user[2]])
            if ch_result == True and dm.send_text('text') and dm.send_link('https://example.com'):
                print(f"Sending to {user[1]} "+"\033[32m"+"Success"+"\033[0m")
                DataBase.SendUpdate(user[2], 1)
            else:
                try:
                    if json.loads(ch_result)['message'] == 'Unloadable participant':
                        print(f"Sending to {user[1]} "+"\033[31m"+"User not available"+"\033[0m")
                        DataBase.SendUpdate(user[2], 1)
                    else:
                        raise Exception()
                except:
                    print(f"Sending to {user[1]} "+"\033[31m"+"Failed"+"\033[0m")
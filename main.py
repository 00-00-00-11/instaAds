import os
from DM import DM
from instapi import bind
from instapi import User
from database import DataBase
from dotenv import load_dotenv; load_dotenv()

username = os.getenv('username')
password = os.getenv('password')

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
    dm.create(["16817136641","2109565415"])
    dm.send()
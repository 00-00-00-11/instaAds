import os
from instapi import bind
from instapi import User
from databases import DataBase
from dotenv import load_dotenv; load_dotenv()

username = os.getenv('username')
password = os.getenv('password')
username_for_data = os.getenv('username_for_data')

bind(username, password)

followers = User.from_username(username_for_data).followers()

for follower in followers:
    print(f"Adding {follower.username} to database")
    newUser = DataBase(follower.username, follower.pk, 0)
    newUser.GoToDB()
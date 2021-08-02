import os
from instapi import bind
from instapi import User
from dotenv import load_dotenv; load_dotenv()

username = os.getenv('username')
password = os.getenv('password')

bind(username, password)

followers = User.from_username('discord_js').followers()

for follower in followers:
    print(follower)
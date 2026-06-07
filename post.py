from instagrapi import Client
import requests
import os
import uuid

USERNAME = os.environ.get('IG_USERNAME')
PASSWORD = os.environ.get('IG_PASSWORD')
CAPTION = os.environ.get('CAPTION')
IMAGE_URL = os.environ.get('IMAGE_URL')

r = requests.get(IMAGE_URL, timeout=60)
temp_path = f'/tmp/{uuid.uuid4()}.jpg'
with open(temp_path, 'wb') as f:
    f.write(r.content)

cl = Client()
cl.login(USERNAME, PASSWORD)
cl.photo_upload(temp_path, CAPTION)
print("Posted successfully!")

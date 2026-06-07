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

# Load session kalau ada, biar tidak login ulang terus
session_path = '/tmp/session.json'
if os.path.exists(session_path):
    cl.load_settings(session_path)

cl.login(USERNAME, PASSWORD)
cl.dump_settings(session_path)

# Post sebagai ARCHIVE (tidak muncul di feed, hanya di archive)
media = cl.photo_upload(
    temp_path,
    CAPTION,
    extra_data={"audience": "besties"}  # private-ish, hanya close friends
)

# Langsung archive setelah post
cl.media_archive(media.id)

print(f"Posted and archived successfully! Media ID: {media.id}")

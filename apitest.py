#from flask import Flask
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

with build('youtube', 'v3', developerKey=YOUTUBE_API_KEY) as service:
    response = service.videos().list(part='snippet', id='th5_9woFJmk')
    data = response.execute()
    print(data['description'][0]['snippet']['description'])

#YouTube Data API to get video transcript. 


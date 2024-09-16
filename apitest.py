from googleapiclient.discovery import build # type: ignore
from dotenv import load_dotenv # type: ignore
from openai import OpenAI # type: ignore
import os

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def get_summary(url, length, script):
    id = url.split("v=", 1)[1]

    #YouTube Data API to get video transcript. It seems that we cannot access the transcript from the API
    with build('youtube', 'v3', developerKey=YOUTUBE_API_KEY) as service:
        response = service.videos().list(part='snippet', id=id)
        data = response.execute()
        #print(data['items'][0]['snippet']['description'])

    #OpenAI API
    client = OpenAI(api_key=OPENAI_API_KEY)

    chat_completion = client.chat.completions.create(
        messages =[
            {
                "role": "user",
                "content": f"Imagine you are an teaching assistant. I am trying to learn about a subject and need to watch many youtube videos on certain subjects. Sometimes I just need a summary of the contents of the youtube video in dot points. Please write a {length} word summary using the transcript of the video: {script}. The summary should always be structured as follows: It should start 2-3 sentences introduction of what the video is about. Following this 3-7 dot points of the main things covered in the video. Lastly the summary should end with 2-3 sentences conclusion. Please only respond with a HTML formatted response. If there is no transcript provided, please respond with: \"No transcript available\".",
            }
        ],
        model="gpt-3.5-turbo",
    )

    message = chat_completion.choices[0].message.content
    return message


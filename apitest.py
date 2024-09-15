from googleapiclient.discovery import build # type: ignore
from dotenv import load_dotenv # type: ignore
from openai import OpenAI # type: ignore
import os

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def get_summary(url, length, html):
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
                "content": f"please write a {length} word summary of this youtube video description: {data['items'][0]['snippet']['description']} and the transcript of the video: {html}. Always include dot points of the main things covered in the transcript. Please only respond with a HTML formatted response.",
            }
        ],
        model="gpt-3.5-turbo",
    )

    message = chat_completion.choices[0].message.content
    print(message)
    return message


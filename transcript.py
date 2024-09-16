from youtube_transcript_api import YouTubeTranscriptApi # type: ignore

def get_transcript(video_id):
    
    try:
        response = YouTubeTranscriptApi.list_transcripts(video_id)
        response = response.find_transcript(['en']).fetch()
    except:
        response = []
    return response
    
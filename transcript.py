from youtube_transcript_api import YouTubeTranscriptApi # type: ignore

def get_transcript(video_id):
    response = []
    try:
        response = YouTubeTranscriptApi.list_transcripts(video_id, languages=["en"])
    except:
        response = []
    return response
    
from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    return YouTubeTranscriptApi.get_transcript(video_id)
    
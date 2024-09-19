from youtube_transcript_api import YouTubeTranscriptApi # type: ignore
import logging

import logging

logging.basicConfig(level=logging.INFO)

def get_transcript(video_id):
    logging.info(f"Fetching transcript for video: {video_id}")
    try:
        response = YouTubeTranscriptApi.list_transcripts(video_id)
        response = response.find_transcript(['en']).fetch()
        logging.info("Transcript fetched successfully")
        return response
    except Exception as e:
        logging.error(f"Error fetching transcript: {str(e)}")
        return []
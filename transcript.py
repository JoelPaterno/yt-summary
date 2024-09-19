from youtube_transcript_api import YouTubeTranscriptApi # type: ignore
import logging
import requests

logging.basicConfig(level=logging.INFO)

def get_transcript(video_id):
    logging.info(f"Fetching transcript for video: {video_id}")
    try:
        # Test internet connectivity
        requests.get('https://www.youtube.com', timeout=5)
        logging.info("Internet connectivity test passed")

        response = YouTubeTranscriptApi.list_transcripts(video_id)
        response = response.find_transcript(['en']).fetch()
        logging.info("Transcript fetched successfully")
        return response
    except requests.ConnectionError:
        logging.error("Failed to connect to YouTube. Check network connectivity.")
        return None
    except Exception as e:
        logging.error(f"Error fetching transcript: {str(e)}")
        return None
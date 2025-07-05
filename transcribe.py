from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join([t['text'] for t in transcript])

if __name__ == "__main__":
    video_id = "IK62Rk47aas"
    text = get_transcript(video_id)
    with open("transcript.txt", "w") as f:
        f.write(text)

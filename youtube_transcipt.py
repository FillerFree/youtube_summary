from youtube_transcript_api import YouTubeTranscriptApi


class YoutubeTranscript:
    def __int__(self):
        pass

    def get_transcipts(self, youtube):
        transciptions = YouTubeTranscriptApi.get_transcript(youtube.get_video_id(), languages=youtube.get_lang())
        return ''.join(transciption['text'] + ' ' for transciption in transciptions[::4])

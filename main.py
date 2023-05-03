from youtube import YouTube
from youtube_transcipt import YoutubeTranscript
from freegpt import HuggingChat


if __name__ == "__main__":
    yt = YouTube('2P30W3TN4nI', 'en')
    transcript = YoutubeTranscript().get_transcipts(yt)
    llm = HuggingChat()
    print(llm('Can you please summzrize following text: ' + transcript))

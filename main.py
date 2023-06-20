from youtube import YouTube
from youtube_transcipt import YoutubeTranscript
from llm_factory import LlmFactory
from flask import Flask

app = Flask(__name__)
model = LlmFactory().get_model(model='Noob')


@app.route("/summarize/<youtube_id>")
def hello_world(youtube_id):
    # y - 2P30W3TN4nI
    yt = YouTube(youtube_id, 'en')
    transcript = YoutubeTranscript().get_transcipts(yt)

    return model.build_summary(transcript)


if __name__ == "__main__":
    youtube_id = "2P30W3TN4nI"
    yt = YouTube(youtube_id, 'en')
    transcript = YoutubeTranscript().get_transcipts(yt)

    print(model.build_summary(transcript))

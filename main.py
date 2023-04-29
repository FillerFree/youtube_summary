from youtube import YouTube
from llm_factory import LlmFactory
from youtube_transcipt import YoutubeTranscript
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
import nltk

SENTENCES_COUNT = 10

if __name__ == "__main__":
    nltk.download('punkt')
    language = 'english'
    yt = YouTube('2P30W3TN4nI', 'en')
    transcript = YoutubeTranscript().get_transcipts(yt)
    parser = PlaintextParser.from_string(transcript, Tokenizer(language))
    stemmer = Stemmer(language)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(language)
    for sentence in summarizer(parser.document, 100):
        print(sentence)



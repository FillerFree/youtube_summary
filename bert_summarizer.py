from summarizer import Summarizer


class BertSummarizer:
    def __init__(self):
        self.bert_model = Summarizer()

    def build_summary(self, content):
        response = self.bert_model(content, min_length=60)
        return response

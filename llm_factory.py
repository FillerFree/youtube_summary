# from bert_summarizer import BertSummarizer
from facebook_bart_summarizer import FacebookBartSummarizer


class LlmFactory:
    def get_model(self, model='bert_summarizer'):
        # if model == 'bert_summarizer':
        #     return BertSummarizer()
        # else:
        return FacebookBartSummarizer()

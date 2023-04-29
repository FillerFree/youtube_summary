from bert_summarizer import BertSummarizer
from openai_llm import OpenaiLlm


class LlmFactory:
    def get_model(self, default='bert_summarizer'):
        if default == 'bert_summarizer':
            return BertSummarizer()
        else:
            return OpenaiLlm()

from transformers import PegasusTokenizer, PegasusForConditionalGeneration


class PegasusSumarizer:
    def __init__(self):
        self.model_name = "google/pegasus-xsum"
        self.device = "cpu"
        self.tokenizer = PegasusTokenizer.from_pretrained(self.model_name)
        self.model = PegasusForConditionalGeneration.from_pretrained(self.model_name).to(self.device)

    def build_summary(self, content):
        batch = self.tokenizer([content], max_length=1024, return_tensors="pt").to(self.device)
        translated = self.model.generate(**batch)
        tgt_text = self.tokenizer.batch_decode(translated, skip_special_tokens=True)
        return tgt_text[0]

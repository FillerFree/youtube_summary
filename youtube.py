class YouTube:
    def __init__(self, video_id, lang):
        self.video_id = video_id
        self.lang = [lang]

    def get_video_id(self):
        return self.video_id

    def get_lang(self):
        return self.lang

import openai
import requests

class OpenaiLlm:
    def __init__(self):
        openai.api_key = "sk-Q1TGaA2FG6mS1UQoreZcBT3BlbkFJWWgBjBJL4fUJ0ETwtJDEw"
        self.model = 'gpt-3.5-turbo'

    def build_summary(self, model, content):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Can you please give me summary of the following?"},
                {"role": "user", "content": content}
            ]
        )

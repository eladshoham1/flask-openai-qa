import openai
from os import environ
from typing import Tuple

class OpenAIService:
    """
    Service to interact with the OpenAI API.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(OpenAIService, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, 'initialized'):
            openai.api_key = environ.get('OPENAI_API_KEY')
            self.initialized = True

    def ask_question(self, question: str) -> Tuple[bool, str]:
        """
        Service function to interact with OpenAI API to get an answer to a given question.

        :param question: The question to ask the OpenAI API.
        :return: A tuple where the first element is a boolean indicating success,
                and the second element is the answer or an error message.
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": question}
                ]
            )
            return True, response['choices'][0]['message']['content'].strip()
        except Exception as e:
            return False, f'Something went wrong with your question: {str(e)}'

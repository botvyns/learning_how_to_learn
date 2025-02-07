import os
from dotenv import load_dotenv

import ollama

load_dotenv()


class Summarizer:

    @property
    def model_name(self) -> str:
        return os.getenv("OLLAMA_MODEL")

    @property
    def user_prompt(self) -> str:
        return """Based on the provided transcipt, provide:
        1. key concepts
        2. their brief explanations
        3. any metaphors, analogies, or examples that can help the reader better grasp key points
        4. questions to check up knowledge later
        Text: {text}"""

    @property
    def system_prompt(self) -> str:
        return """You help to solidyfy the knowledge provided in the text.
                You can identify key concepts and provide their brief explanation.
                You can use metaphors, analogies, or examples to help the reader better grasp key points.
                You know which questions will help the learner to better recall information later.
                Cut the chatter."""

    def summarize(self, text: str) -> str:
        prompt = self.user_prompt.format(text=text)
        llm_response = ollama.chat(
            model=self.model_name,
            messages=[{"role": "system", "content": self.system_prompt}, {"role": "user", "content": prompt}],
        )
        return llm_response.message.content

import os
from dotenv import load_dotenv

import backoff
import ollama

load_dotenv()


class Summarizer:

    @property
    def model_name(self) -> str:
        return os.getenv("OLLAMA_MODEL")

    @property
    def user_prompt(self) -> str:
        return """Based on the provided text, provide:

        1. **Key Concepts & Brief Explanations** – Summarize essential ideas concisely.
        2. **Metaphors, Analogies, or Examples** – Provide clear comparisons or real-world examples to enhance understanding.
        3. **Recall Questions** – List targeted questions to reinforce learning.

        Text: {text}"""

    @property
    def system_prompt(self) -> str:
        return """You enhance knowledge retention by structuring information clearly.

        - Identify key concepts and explain them concisely.
        - Use metaphors, analogies, or real-world examples to improve comprehension.
        - Generate effective recall questions to reinforce learning.

        You keep responses precise and to the point. No unnecessary explanations. You alsway respond in Markdown."""

    @backoff.on_exception(backoff.expo, ollama.ResponseError, max_tries=3)
    def summarize(self, text: str) -> str:
        prompt = self.user_prompt.format(text=text)
        llm_response = ollama.chat(
            model=self.model_name,
            messages=[{"role": "system", "content": self.system_prompt}, {"role": "user", "content": prompt}],
        )
        return llm_response.message.content

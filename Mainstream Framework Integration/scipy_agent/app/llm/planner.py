from openai import OpenAI

from config import OPENAI_API_KEY
from config import OPENAI_BASE_URL
from llm.prompts import SYSTEM_PROMPT


class Planner:

    def __init__(self):
        self.client = OpenAI(
            api_key=OPENAI_API_KEY,
            base_url=OPENAI_BASE_URL #,
            #timeout = 120
        )

    def plan(self, user_prompt: str):
        print(OPENAI_API_KEY)
        print(OPENAI_BASE_URL)
        response = self.client.chat.completions.create(
            model="gpt-oss",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )

        content = response.choices[0].message.content

        return [item.strip() for item in content.split(",")]
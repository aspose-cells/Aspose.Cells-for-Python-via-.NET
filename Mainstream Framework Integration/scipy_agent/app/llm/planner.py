from openai import OpenAI
from config import OPENAI_API_KEY, MODEL,OPENAI_BASE_URL
from llm.prompts.tool_selection_prompt import TOOL_SELECTION_PROMPT
import json

client = OpenAI(
            api_key=OPENAI_API_KEY,
            base_url=OPENAI_BASE_URL #,
            #timeout = 120
        )
class Planner:

    def create_plan(self, request: str):

        print(OPENAI_API_KEY)
        print(OPENAI_BASE_URL)
        response = client.chat.completions.create(
            model="gpt-oss",
            messages=[
                {
                    "role": "system",
                    "content": TOOL_SELECTION_PROMPT
                },
                {
                    "role": "user",
                    "content": request
                }
            ]
        )

        content = response.choices[0].message.content
        try:
            plan = json.loads(content)
        except Exception:
            raise ValueError(f"LLM output is not valid JSON: {content}")

        if isinstance(plan, list):
            plan = {"tools": plan}

        if "tools" not in plan:
            raise ValueError(f"Invalid plan format: {plan}")

        return plan


"""       
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": TOOL_SELECTION_PROMPT},
                {"role": "user", "content": request}
            ],
            tools=[
                {
                    "type": "function",
                    "function": {
                        "name": "select_tools",
                        "description": "Select best analysis tools for Excel data analysis",  #  must be string
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "tools": {
                                    "type": "array",
                                    "items": {"type": "string"}
                                },
                                "reason": {
                                    "type": "string"
                                },
                                "confidence": {
                                    "type": "number"
                                }
                            },
                            "required": ["tools"]
                        }
                    }
                }
            ],
            tool_choice="auto",
            temperature=0.2
        )

        msg = response.choices[0].message

        # tool calling
        if msg.tool_calls:
            args = msg.tool_calls[0].function.arguments
            return json.loads(args)

        # fallback
        return json.loads(msg.content)
"""
from openai import OpenAI
from models import SolutionResponse
import os

if not os.getenv("OPENAI_API_KEY", None):
    raise Exception("Set the OPENAI_API_KEY environment variable.")

openai_client = OpenAI()

def chat(system, user):
    messages = [
        {
            "role": "system",
            "content": system
        },
        {
            "role": "user",
            "content": user 
        }
    ]

    response = openai_client.beta.chat.completions.parse(
        model='gpt-4o-2024-08-06',
        messages=messages,
        temperature=0.1,
        response_format=SolutionResponse,
    )

    return response.choices[0].message.parsed

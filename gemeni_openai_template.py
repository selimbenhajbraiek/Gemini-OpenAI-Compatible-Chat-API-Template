'''
Author

Selim Ben Haj Braiek
🎓 Master’s student in Data Science and Artificial Intelligence
📍 Budapest University of Technology and Economics (BME)

Description: A simple Python template demonstrating how to replace OpenAI’s paid API by using **Google Gemini** with OpenAI-compatible endpoints.
'''

import os
from dotenv import load_dotenv
from openai import OpenAI
from IPython.display import Markdown, display


load_dotenv(override=True)

GEMINI_BASE_URL = os.getenv("GEMINI_BASE_URL")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def check_api_key():
    """Validate presence & format of the Gemini API key."""
    if not GOOGLE_API_KEY:
        print("No API key found. Set GOOGLE_API_KEY inside .env.")
        return False
    elif not GOOGLE_API_KEY.startswith("AIz"):
        print("API key found but doesn't start with 'AIz'. Double check your key.")
        return False
    else:
        print("API key found and validated!")
        return True
gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=GOOGLE_API_KEY)
messages = [
        {"role": "system", "content": "You are a helpful chatbot"},
        {
            "role": "user",
            "content": "Explain to me the number 42 when I am using the seed function in random model training"
        }
    ]
response = gemini.chat.completions.create(
        model="gemini-2.5-pro",
        messages=messages
    )

output = response.choices[0].message.content
print(output)


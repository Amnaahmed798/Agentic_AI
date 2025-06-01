from litellm import completion
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Automatically get the keys from environment
openai_key = os.getenv("OPENAI_API_KEY")
gemini_key = os.getenv("GEMINI_API_KEY")

def openai():
    response = completion(
        model="openai/text-davinci-003",
        api_key=openai_key,
        messages=[{ "content": "Hello, how are you?", "role": "user" }]
    )
    print(response)

def gemini():
    response = completion(
        model="gemini/gemini-1.5-flash",
        api_key=gemini_key,
        messages=[{ "content": "Hello, how are you?", "role": "user" }]
    )
    print(response)

def gemini2():
    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        api_key=gemini_key,
        messages=[{ "content": "Hello, how are you?", "role": "user" }]
    )
    print(response)

openai()
gemini()
gemini2()

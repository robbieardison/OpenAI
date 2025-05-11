from openai import OpenAI
from dotenv import load_dotenv
import os
import asyncio

# Load API keys
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()

result = client.images.generate(
    model="dall-e-3",
    prompt="a white siamese cat",
    size="1024x1024"
)

print(result.data[0].url)
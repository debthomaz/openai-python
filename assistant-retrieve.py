import os
from openai import OpenAI

openai.api_key = os.getenv('OPENAI_API_KEY')

my_assistant = client.beta.assistants.retrieve("astro_joe")

print(my_assistant)

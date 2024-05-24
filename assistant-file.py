import os
from openai import OpenAI

openai.api_key = os.getenv('OPENAI_API_KEY')

assistant_file = client.beta.assistants.files.create(
  assistant_id="astro_joe",
  file_id="file-astrojoe"
)
print(assistant_file)

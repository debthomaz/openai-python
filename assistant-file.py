from openai import OpenAI

openai.api_key = 'sk-'

assistant_file = client.beta.assistants.files.create(
  assistant_id="astro_joe",
  file_id="file-astrojoe"
)
print(assistant_file)

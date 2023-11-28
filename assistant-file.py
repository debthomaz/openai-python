from openai import OpenAI

client = OpenAI(api_key="")

assistant_file = client.beta.assistants.files.create(
  assistant_id="astro_joe",
  file_id="file-astrojoe"
)
print(assistant_file)

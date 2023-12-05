from openai import OpenAI

openai.api_key = 'sk-'

my_assistant = client.beta.assistants.retrieve("astro_joe")

print(my_assistant)

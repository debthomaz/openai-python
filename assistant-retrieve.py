from openai import OpenAI

client = OpenAI(api_key="")

my_assistant = client.beta.assistants.retrieve("astro_joe")

print(my_assistant)

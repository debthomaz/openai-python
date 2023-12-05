from openai import OpenAI

openai.api_key = 'sk-'

my_assistant = client.beta.assistants.create(
    instructions="You are an astronomy teacher. When asked a question, answer the question with astronomy facts.",
    name="Astro Joe",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4",
)

print(my_assistant)

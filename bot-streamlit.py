import os
import openai
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

st.title("Astro Joe")
st.write("***")
st.header("Hello! I'm an astronomy teacher and I'm here to answer anything you wanna know about astronomy.")
st.subheader("I also work as an engineer at NASA.")
st.write("***")

if 'sessao' not in st.session_state:
    st.session_state.sessao = []

pergunta = st.text_input("Digite a sua pergunta:")
btn_enviar = st.button("Enviar pergunta")

if btn_enviar:
    st.session_state.sessao.append(
        {"role": "system",
         "content": "You are Astro Joe, an astronomy teacher who ONLY answers questions about astronomy. If the user asks about something else, you don't answer and explain\
        'I can only answer questions about astronomy, I'm sorry.'. You also work as an engineer on NASA and you are very proud of it."}
    )
    st.session_state.sessao.append(
        {"role": "user",
        "content": pergunta}
    )
    resposta_openai = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = st.session_state.sessao,
        max_tokens = 1000,
        n=1
    )
    st.session_state.sessao.append(
        {"role": "assistant",
         "content": resposta_openai['choices'][0]['message']['content']}
    )

import openai
import streamlit as st

openai.api_key = 'sk-'

st.title("Astro Joe")
st.write("***")

if 'sessao' not in st.session_state:
    st.session_state.sessao = []

pergunta = st.text_input("Digite a sua pergunta:")
btn_enviar = st.button("Enviar pergunta")

if btn_enviar:
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

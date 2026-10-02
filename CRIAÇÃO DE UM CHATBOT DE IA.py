# AULA 3 - Criação de um chatbot com IA em tempo real

# o que precisa ter nesse programa:
# título
# campo de mensagem
# quando o usuário enviar uma mensagem
    # mostrar a mensagem na conversa
    # mandar a mensagem pra IA responder
    # mostrar a resposta da IA 

# pip install streamlit e openai

import streamlit as st
from openai import OpenAI 

modelo_ia = OpenAI(api_key="AQ.Ab8RN6IwBhn0sTNqBwLspvI-haoJ1eEFuialGdyi-WuAoMzCdw",
                   base_url="https://generativelanguage.googleapis.com/v1beta/openai")

st.write("## ChatBot de IA") # a função serve para incrementar aquilo que vc pedir na tela do seu programa (nesse caso, na tela do chatBot)

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui") # criação do campo de mensagem

for mensagem in st.session_state["lista_mensagens"]:
    quem_enviou = mensagem["role"]
    texto_mensagem = mensagem["content"] 
    st.chat_message(quem_enviou).write(texto_mensagem)
    


if mensagem_usuario:
    # exibir a mensagem na tela
    # user -> usuario ("Quem esta mandando")
    # assistant -> chatbot ("Quem esta mandando") 
    st.chat_message("user").write(mensagem_usuario) #Responsável por exibir a mensagem no campo de mensagem 
    mensagem1 = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem1)
    
    # pegar a resposta da IA
    resposta_modelo = modelo_ia.chat.completions.create(
        messages = st.session_state["lista_mensagens"],
        model="gemini-flash-lite-latest"
    )

    
    resposta_ia = resposta_modelo.choices[0].message.content

    # enviar a mensagem da IA no chat
    st.chat_message("assistant").write(resposta_ia)
    mensagem2 = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem2)
       


#   tornar as respostas inteligentes

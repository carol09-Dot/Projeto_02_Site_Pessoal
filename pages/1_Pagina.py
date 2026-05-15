import streamlit as st
import os

st.set_page_config(layout="wide")
st.title("Página 1")

def carregar_html(nome_arquivo):
  diretorio_atual = os.path.dirname(os.path.abspath(__file__))
  caminho_completo = os.path.join(diretorio_atual, nome_arquivo)
  with open(caminho_completo, "r", encoding="utf-8") as f:
    return f.read()
  
codigo_html = carregar_html("index.html")
st.components.v1.html(codigo_html, height=1200, scrolling=True)

# app.py (versão com python-dotenv)

import streamlit as st
import requests
import os
from dotenv import load_dotenv

# --- CONFIGURAÇÃO INICIAL E CARREGAMENTO DA CHAVE ---

# A configuração da página deve ser a primeira chamada do Streamlit no script.
st.set_page_config(
    page_title="Resumo de Texto com IA (Gemini)",
    page_icon="✨",
    layout="wide"
)

# Carrega as variáveis do arquivo .env para o ambiente
load_dotenv()

# Pega a chave da API do ambiente (local ou do deploy)
API_KEY = os.getenv("API_KEY")

# Verifica imediatamente se a chave da API foi encontrada
if not API_KEY:
    st.error(
        "Chave da API (API_KEY) não encontrada! Verifique seu arquivo .env ou as configurações de segredos no deploy.")
    st.stop()  # Interrompe a execução se a chave não for encontrada


# --- FUNÇÃO PARA CHAMADA DA API ---

def chamar_api_gemini(texto_para_resumir: str) -> str:
    """
    Envia o texto para a API do Google Gemini e retorna o resumo.

    Args:
        texto_para_resumir: O texto que será enviado para a sumarização.

    Returns:
        O texto resumido pela IA ou uma mensagem de erro.
    """
    # Monta a URL da API com a chave (agora usando a variável API_KEY)
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={API_KEY}"

    # Headers da requisição
    headers = {"Content-Type": "application/json"}

    # Corpo da requisição (payload)
    prompt = f"Aja como um especialista em sumarização de textos. Resuma o seguinte texto de forma clara, concisa e em português:\n\n---\n\n{texto_para_resumir}"
    body = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    # Faz a chamada POST para a API
    response = requests.post(url, headers=headers, json=body, timeout=300)

    # --- TRATAMENTO DA RESPOSTA ---
    if response.status_code == 200:
        try:
            resultado = response.json()
            resumo = resultado.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text")
            if resumo:
                return resumo
            else:
                return f"Erro: A API não retornou um resumo válido. Resposta: {resultado}"
        except (KeyError, IndexError) as e:
            return f"Erro ao processar a resposta da API: {e}. Resposta recebida: {response.text}"
    else:
        return f"Erro na API: {response.status_code} - {response.text}"


# --- INTERFACE DO USUÁRIO (STREAMLIT) ---

st.title("✨ Resumidor de Textos com Gemini AI")
st.markdown("Cole um texto no campo abaixo e a IA do Google criará um resumo para você.")

# Área de texto para o usuário
texto_original = st.text_area("Texto para resumir:", height=250,
                              placeholder="Cole aqui o artigo, e-mail ou qualquer outro texto...")

# Botão para iniciar o processo
if st.button("Gerar Resumo", type="primary"):
    if not texto_original.strip():
        st.warning("Por favor, cole um texto antes de gerar o resumo.")
    else:
        with st.spinner("🧠 A IA está pensando e gerando o resumo..."):
            resumo_gerado = chamar_api_gemini(texto_original)
            st.subheader("📌 Resumo Gerado:")

            if resumo_gerado.startswith("Erro na API:") or resumo_gerado.startswith("Erro ao processar"):
                st.error(resumo_gerado)
            else:
                st.success(resumo_gerado)
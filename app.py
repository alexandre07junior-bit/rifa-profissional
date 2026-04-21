import streamlit as st
import pandas as pd

# 1. Configuração Otimizada para Celular
st.set_page_config(
    page_title="Rifa Profissional",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. CSS para forçar o layout "Mobile-First"
st.markdown("""
    <style>
    /* Ajusta as margens para não ficar espaço sobrando nas laterais */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }
    /* Deixa os botões esticados na largura total do celular */
    div.stButton > button {
        width: 100%;
        height: 3.5rem;
        font-size: 1.2rem;
        background-color: #007BFF;
        color: white;
    }
    /* Melhora a legibilidade do texto no mobile */
    h1, h2, h3 {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Estrutura do Site (Substitua pelos seus dados)
st.title("🚗 Rifa Automotiva")

# Use 'use_container_width=True' para a imagem ocupar a largura da tela
# st.image("sua_imagem.jpg", use_container_width=True)

st.subheader("Garanta seu número!")
st.write("Participe da rifa e concorra a um prêmio exclusivo.")

# Botão principal (Fácil de clicar no Android)
if st.button("Reservar Número pelo WhatsApp"):
    st.write("Redirecionando para o seu atendimento...")
    # Coloque aqui o link do seu WhatsApp
    st.link_button("Ir para o WhatsApp", "https://wa.me/5537991360517")

# Exemplo de lista (Um item embaixo do outro, nada de colunas complexas)
st.divider()
st.write("---")
st.write("📜 **Regulamento:**")
st.write("1. Pagamento via PIX.")
st.write("2. Envie o comprovante no WhatsApp.")

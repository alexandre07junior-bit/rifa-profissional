import streamlit as st
import pandas as pd
import random
import time
import os

# --- CONFIGURAÇÃO INICIAL (Obrigatório vir no topo) ---
st.set_page_config(page_title="Rifa Oficial", layout="wide")

# Inicialização de dados
def carregar_dados():
    if os.path.exists('vendas.csv'):
        df = pd.read_csv('vendas.csv')
        # Converte o CSV de volta para dicionário
        vendas = {}
        for _, row in df.iterrows():
            vendas[row['numero']] = {"nome": row['nome'], "tel": row['tel']}
        return vendas
    return {}

def salvar_dados(vendas_dict):
    lista = [{'numero': k, 'nome': v['nome'], 'tel': v['tel']} for k, v in vendas_dict.items()]
    pd.DataFrame(lista).to_csv('vendas.csv', index=False)

if 'vendas' not in st.session_state: 
    st.session_state.vendas = carregar_dados()
if 'carrinho' not in st.session_state: 
    st.session_state.carrinho = []

# --- CSS PARA PERSONALIZAÇÃO ---
st.markdown("""
    <style>
    .timer-text { font-size: 80px; font-weight: bold; color: #333; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR (CHECKOUT) ---
st.sidebar.title("🛒 Checkout")
valor_total = len(st.session_state.carrinho) * 2
st.sidebar.write(f"Números: {len(st.session_state.carrinho)}")
st.sidebar.write(f"Total: R$ {valor_total},00")

with st.sidebar.form("form_compra", clear_on_submit=True):
    nome = st.text_input("Nome Completo")
    tel = st.text_input("WhatsApp")
    if st.form_submit_button("Confirmar Compra"):
        if nome and tel and st.session_state.carrinho:
            for n in st.session_state.carrinho:
                st.session_state.vendas[n] = {"nome": nome, "tel": tel}
            salvar_dados(st.session_state.vendas)
            st.session_state.carrinho = []
            st.rerun()
        else:
            st.error("Selecione números e preencha os dados!")

# --- CORPO PRINCIPAL ---
st.title("💰 Sorteio Oficial")
st.write(f"Vendidos: {len(st.session_state.vendas)}/500")

cols = st.columns(10)
for i in range(1, 501):
    col = cols[(i-1) % 10]
    if i in st.session_state.vendas:
        col.button(f"{i}", disabled=True)
    else:
        label = f"✅ {i}" if i in st.session_state.carrinho else f"{i}"
        if col.button(label, key=f"btn_{i}"):
            if i in st.session_state.carrinho: st.session_state.carrinho.remove(i)
            else: st.session_state.carrinho.append(i)
            st.rerun()

# --- ADMIN ---
with st.expander("🔐 Painel Admin"):
    if st.text_input("Senha", type="password") == "1234":
        st.dataframe(pd.DataFrame.from_dict(st.session_state.vendas, orient='index'))
        if st.button("Sortear (Cronômetro)"):
            holder = st.empty()
            for _ in range(50):
                n = random.randint(1, 500)
                holder.markdown(f"<div class='timer-text'>{n:03d}</div>", unsafe_allow_html=True)
                time.sleep(0.1)
            vencedor = random.randint(1, 500)
            holder.markdown(f"<div class='timer-text' style='color: green;'>{vencedor:03d}</div>", unsafe_allow_html=True)
            st.balloons()
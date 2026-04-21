import streamlit as st

# Configuração de Layout
st.set_page_config(page_title="Rifa R$ 500", layout="centered")

# CSS Avançado para Design Profissional e Mobile
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; }
    .selected { background-color: #2e7d32 !important; color: white !important; }
    .header-box { background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; }
    .btn-checkout { background-color: #25d366 !important; color: white !important; font-size: 1.2rem !important; }
    </style>
""", unsafe_allow_html=True)

# Lógica de Estado
if 'selecionados' not in st.session_state:
    st.session_state.selecionados = []

# --- CABEÇALHO ---
st.markdown('<div class="header-box"><h1>💰 Rifa de R$ 500,00</h1><p align="center">Sorteio pela Loteria Federal</p></div>', unsafe_allow_html=True)

# --- NAVEGAÇÃO ---
tab1, tab2, tab3 = st.tabs(["Números", "Como Funciona", "Resumo"])

with tab1:
    st.subheader("Escolha seus números:")
    cols = st.columns(5)
    for i in range(1, 101):
        with cols[(i-1) % 5]:
            btn_color = "primary" if i in st.session_state.selecionados else "secondary"
            if st.button(str(i), key=f"btn_{i}", type=btn_color):
                if i in st.session_state.selecionados:
                    st.session_state.selecionados.remove(i)
                else:
                    st.session_state.selecionados.append(i)
                st.rerun()

with tab2:
    st.subheader("Regulamento")
    st.markdown("""
    * **Prêmio:** R$ 500,00 no PIX.
    * **Valor:** R$ 10,00 por número.
    * **Sorteio:** Realizado após a venda total das cotas.
    * **Pagamento:** Chave PIX será enviada no WhatsApp.
    """)

with tab3:
    st.subheader("Seu Pedido")
    if st.session_state.selecionados:
        nums = sorted(st.session_state.selecionados)
        total = len(nums) * 10
        st.write(f"**Números:** {', '.join(map(str, nums))}")
        st.write(f"**Total a pagar:** R$ {total},00")
        
        msg = f"Olá! Quero reservar os números {', '.join(map(str, nums))} (Total: R${total})."
        st.link_button("FINALIZAR NO WHATSAPP", f"https://wa.me/5537991360517?text={msg}", help="Clique aqui para reservar")
    else:
        st.info("Selecione os números na aba 'Números' para prosseguir.")

st.divider()
st.caption("Site de rifas exclusivo - Gestão de Tráfego Automotiva")

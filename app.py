import streamlit as st

# Configuração de Layout Mobile-First
st.set_page_config(page_title="Rifa R$ 500", layout="centered", initial_sidebar_state="collapsed")

# CSS para Design Profissional e Mobile
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; }
    .header-box { background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-bottom: 20px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# Lógica de Estado
if 'selecionados' not in st.session_state:
    st.session_state.selecionados = []

# --- CABEÇALHO ---
st.markdown('<div class="header-box"><h1>💰 Rifa de R$ 500,00</h1><p>Sorteio pela Loteria Federal</p></div>', unsafe_allow_html=True)

# --- NAVEGAÇÃO ---
tab1, tab2, tab3 = st.tabs(["🔢 Números", "📋 Regras", "💳 Pagamento"])

with tab1:
    st.subheader("Escolha seus números:")
    cols = st.columns(5)
    for i in range(1, 101):
        with cols[(i-1) % 5]:
            btn_type = "primary" if i in st.session_state.selecionados else "secondary"
            if st.button(str(i), key=f"btn_{i}", type=btn_type):
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
    * **Instrução:** Copie a chave PIX, realize o pagamento e envie o comprovante no WhatsApp.
    """)

with tab3:
    st.subheader("Checkout")
    if st.session_state.selecionados:
        nums = sorted(st.session_state.selecionados)
        total = len(nums) * 10
        
        st.write(f"**Números escolhidos:** {', '.join(map(str, nums))}")
        st.write(f"**Total a pagar:** R$ {total},00")
        
        st.divider()
        st.write("### 1. Copie a Chave PIX (CPF):")
        st.code("01969189606", language=None)
        
        st.write("### 2. Envie o comprovante:")
        msg = f"Olá! Acabei de fazer o PIX da rifa (R${total}). Números: {', '.join(map(str, nums))}. Segue o comprovante:"
        st.link_button("ENVIAR COMPROVANTE NO WHATSAPP", f"https://wa.me/5537991360517?text={msg}")
    else:
        st.info("Selecione os números na aba 'Números' para prosseguir.")

st.divider()
st.caption("Site de rifas - Sistema Profissional")

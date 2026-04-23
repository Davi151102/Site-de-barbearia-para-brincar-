import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Barber SaaS", page_icon="✂️")

st.title("✂️ Sistema de Agendamento - Barbearia")

# --- SIMULAÇÃO DE BANCO DE DADOS ---
# Usamos o 'session_state' para os dados não sumirem quando a página atualizar
if 'agenda' not in st.session_state:
    st.session_state.agenda = []

# --- FORMULÁRIO DE AGENDAMENTO ---
with st.form("meu_formulario"):
    st.subheader("Marque seu horário")
    nome = st.text_input("Nome do Cliente")
    servico = st.selectbox("Escolha o Serviço", ["Corte Masculino", "Barba", "Combo Corte + Barba", "Sobrancelha"])
    data = st.date_input("Escolha a Data")
    hora = st.time_input("Escolha o Horário")
    
    botao_enviar = st.form_submit_button("Confirmar Agendamento")

if botao_enviar:
    if nome:
        novo_agendamento = {
            "Cliente": nome,
            "Serviço": servico,
            "Data": str(data),
            "Hora": str(hora)
        }
        st.session_state.agenda.append(novo_agendamento)
        st.success(f"✅ Horário marcado para {nome}!")
    else:
        st.error("❌ Por favor, digite o nome do cliente.")

# --- EXIBIÇÃO DA AGENDA (VISÃO DO BARBEIRO) ---
st.divider()
st.subheader("📅 Agenda do Dia")

if st.session_state.agenda:
    df = pd.DataFrame(st.session_state.agenda)
    st.table(df) # Mostra uma tabela bonita com os horários
else:
    st.info("Nenhum agendamento para hoje.")
  

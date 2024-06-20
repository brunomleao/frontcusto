import streamlit as st
import pandas as pd

# Título da aplicação
st.title("Calculadora de Custo com Redução de Falhas no ECM")

# Inputs fixos
valor_hora = st.number_input("Valor médio por hora de trabalho (em dólar)", min_value=0.0, format="%.2f")
quantidade_funcionarios = st.number_input("Quantidade de funcionários dependentes do ECM", min_value=0, format="%d")

# Inputs dinâmicos para incidência de falha e MTTR
num_entries = st.number_input("Quantos valores de incidência de falha e MTTR deseja inserir?", min_value=1, format="%d")

incidencia_falha_list = []
mttr_list = []
costs = []

for i in range(num_entries):
    st.write(f"Entrada {i+1}")
    incidencia_falha = st.number_input(f"Incidência de falha {i+1} (%)", min_value=0.0, max_value=100.0, format="%.2f", key=f"incidencia_{i}")
    mttr = st.number_input(f"MTTR {i+1} (em horas)", min_value=0.0, format="%.2f", key=f"mttr_{i}")
    incidencia_falha_list.append(incidencia_falha)
    mttr_list.append(mttr)
    custo = valor_hora * quantidade_funcionarios * mttr
    costs.append(custo)
    st.write(f"Custo para incidência de falha {i+1}: ${custo:.2f}")

# Preparar dados para o gráfico
df = pd.DataFrame({
    'Incidência de Falha (%)': incidencia_falha_list,
    'Custo ($)': costs
})

st.subheader("Gráfico de Custo por Incidência de Falha")
# Exibir o gráfico
st.line_chart(df.set_index('Incidência de Falha (%)'))

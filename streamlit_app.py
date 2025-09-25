import streamlit as st

# Configuração da página
st.set_page_config(page_title="FarmTech Solutions", page_icon="🌱")

# Dados das culturas
CAFE_INSUMOS = {
    'fungicida': 1.5,
    'fertilizante': 400,
    'herbicida': 2.0
}

CANA_INSUMOS = {
    'herbicida': 3.0,
    'fertilizante': 500,
    'inseticida': 0.5
}

def calcular_area(comprimento, largura):
    return (comprimento * largura) / 10000

def calcular_insumos(cultura, area):
    insumos = CAFE_INSUMOS if cultura == "Café" else CANA_INSUMOS
    return {k: v * area for k, v in insumos.items()}

# Interface
st.title("🌱 FarmTech Solutions")
st.subheader("Sistema de Agricultura Digital")

# Seleção da cultura
cultura = st.selectbox("Escolha a cultura:", ["Café", "Cana-de-açúcar"])

# Entrada de dados
col1, col2 = st.columns(2)
with col1:
    comprimento = st.number_input("Comprimento (metros):", min_value=0.0, value=100.0)
with col2:
    largura = st.number_input("Largura (metros):", min_value=0.0, value=50.0)

# Cálculos
if comprimento > 0 and largura > 0:
    area = calcular_area(comprimento, largura)
    insumos = calcular_insumos(cultura, area)
    
    # Resultados
    st.success(f"Área calculada: {area:.2f} hectares")
    
    st.subheader("Insumos necessários:")
    for insumo, quantidade in insumos.items():
        unidade = "kg" if insumo == "fertilizante" else "L"
        st.write(f"• {insumo.capitalize()}: {quantidade:.2f} {unidade}")

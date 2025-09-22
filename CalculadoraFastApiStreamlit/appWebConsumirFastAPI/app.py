
import streamlit as st
import requests

# Montagem da Tela 
st.subheader("Tela da CALCULADORA Consumindo API - Streamlit")
st.subheader("API para Calcular - FastAPI")
item_id1 = st.number_input("Num 1:", step=1)
item_id2 = st.number_input("Num 2:", step=1)
operacao = st.selectbox(
    "Operação: ",
    ("ADD", "SUB", "PRO", "DIV", "POW", "LOG", "SQRT", "MOD"),
)


# Evento de clique do botão
if st.button("Calcular"):
    r0 = "http://127.0.0.1:8000/"
    r1 = "calculadora1"
    if operacao in ["SQRT","LOG","MOD","POW"]:
       r1 = "calculadora2"    

    print(">>>>> ", f"{r0}/{r1}/{item_id1}/{item_id2}/{operacao}") 

    r = requests.get(f"{r0}/{r1}/{item_id1}/{item_id2}/{operacao}") 
    if r.status_code == 200:
        dados = r.json()

        operacaoX = dados[0]["operação"]
        resultadoX = dados[1]["resultado"]
        st.write("Resultado: " + operacaoX + " = " + str(resultadoX))
        
        # st.write(dados)
    else:
        st.error("Erro ao acessar API")
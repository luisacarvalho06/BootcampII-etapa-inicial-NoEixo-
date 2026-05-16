import streamlit as st
from motivacao import buscar_frase

st.title("Frases Motivacionais")

if st.button("Gerar frase"):
    frase = buscar_frase()
    st.write(frase)
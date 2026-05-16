import streamlit as st
import json
import os
from motivacao import buscar_frase

ARQUIVO = "tarefas.json"

# carregar tarefas
def carregar():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# salvar tarefas
def salvar(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

# interface
st.title("📚 Organizador de Estudos")

# frase motivacional
st.info(buscar_frase())

tarefas = carregar()

# formulário
nome = st.text_input("Tarefa")
data = st.text_input("Data (DD/MM/AAAA)")
prioridade = st.selectbox("Prioridade", ["Alta", "Média", "Baixa"])

if st.button("Adicionar"):
    tarefas.append({
        "nome": nome,
        "data": data,
        "prioridade": prioridade,
        "concluida": False
    })
    salvar(tarefas)
    st.success("Tarefa adicionada!")

# lista
st.subheader("📋 Tarefas")

for i, t in enumerate(tarefas):
    texto = f"{t['nome']} - {t['data']} ({t['prioridade']})"
    
    if t["concluida"]:
        texto += " ✔"

    col1, col2, col3 = st.columns([6,1,1])

    col1.write(texto)

    if col2.button("✔", key=f"c{i}"):
        tarefas[i]["concluida"] = True
        salvar(tarefas)

    if col3.button("X", key=f"x{i}"):
        tarefas.pop(i)
        salvar(tarefas)

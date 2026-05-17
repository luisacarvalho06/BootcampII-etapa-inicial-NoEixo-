import streamlit as st
import json
import os

from logica import (
    adicionar_tarefa,
    remover_tarefa,
    concluir_tarefa
)

from motivacao import (
    alerta_prazo,
    alerta_baixa_prioridade,
    mensagem_conclusao
)

ARQUIVO = "tarefas.json"


# =========================
# FUNÇÕES
# =========================

def carregar_tarefas():

    if os.path.exists(ARQUIVO):

        with open(
            ARQUIVO,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    return []


def salvar_tarefas(tarefas):

    with open(
        ARQUIVO,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            tarefas,
            f,
            indent=4,
            ensure_ascii=False
        )


# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================

st.set_page_config(
    page_title="No Eixo",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Organizador de Estudos - No Eixo")

st.write(
    "Organize suas tarefas, acompanhe prazos "
    "e mantenha seus estudos no caminho certo."
)

# =========================
# CARREGAR TAREFAS
# =========================

tarefas = carregar_tarefas()

# =========================
# ALERTAS AO INICIAR
# =========================

for tarefa in tarefas:

    if tarefa["concluida"]:
        continue

    nome = tarefa["nome"]
    data = tarefa["data"]
    prioridade = tarefa["prioridade"]

    alerta = alerta_prazo(nome, data)

    if alerta:
        st.warning(alerta)

    if prioridade == "Baixa":

        mensagem = alerta_baixa_prioridade(nome)

        st.info(mensagem)

# =========================
# FORMULÁRIO
# =========================

st.subheader("➕ Adicionar nova tarefa")

with st.form("form_tarefa"):

    nome = st.text_input("Nome da tarefa")

    data = st.text_input(
        "Data (DD/MM/AAAA)"
    )

    prioridade = st.selectbox(
        "Prioridade",
        ["Alta", "Média", "Baixa"]
    )

    adicionar = st.form_submit_button(
        "Adicionar tarefa"
    )

    if adicionar:

        sucesso = adicionar_tarefa(
            tarefas,
            nome,
            data,
            prioridade
        )

        if not sucesso:

            st.error("Dados inválidos!")

        else:

            salvar_tarefas(tarefas)

            alerta = alerta_prazo(
                nome,
                data
            )

            if alerta:
                st.warning(alerta)

            if prioridade == "Baixa":

                mensagem = alerta_baixa_prioridade(nome)

                st.info(mensagem)

            st.success(
                "Tarefa adicionada com sucesso!"
            )

            st.rerun()

# =========================
# LISTA DE TAREFAS
# =========================

st.subheader("📋 Suas tarefas")

if not tarefas:

    st.info("Nenhuma tarefa cadastrada.")

else:

    for i, tarefa in enumerate(tarefas):

        if tarefa["prioridade"] == "Alta":
            cor = "🟥"

        elif tarefa["prioridade"] == "Média":
            cor = "🟨"

        else:
            cor = "🟩"

        status = "✔️" if tarefa["concluida"] else "⏳"

        col1, col2, col3 = st.columns([6, 1, 1])

        with col1:

            st.write(
                f"{cor} "
                f"**{tarefa['nome']}** "
                f"- {tarefa['data']} "
                f"{status}"
            )

        with col2:

            if st.button(
                "✔",
                key=f"concluir_{i}"
            ):

                nome_tarefa = tarefa["nome"]

                concluir_tarefa(
                    tarefas,
                    i
                )

                salvar_tarefas(tarefas)

                mensagem = mensagem_conclusao(
                    nome_tarefa
                )

                st.success(mensagem)
                
        with col3:

            if st.button(
                "❌",
                key=f"remover_{i}"
            ):

                remover_tarefa(
                    tarefas,
                    i
                )

                salvar_tarefas(tarefas)

                st.rerun()

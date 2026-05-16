import requests
from datetime import datetime


def buscar_frase():

    try:
        resposta = requests.get(
            "https://zenquotes.io/api/random"
        )

        if resposta.status_code == 200:

            dados = resposta.json()

            frase = dados[0]["q"]
            autor = dados[0]["a"]

            return f'"{frase}"\n\n- {autor}'

    except Exception:
        return "Continue focado nos seus estudos!"


def alerta_prazo(nome, data_entrega):

    hoje = datetime.now().date()

    prazo = datetime.strptime(
        data_entrega,
        "%d/%m/%Y"
    ).date()

    dias_restantes = (prazo - hoje).days

    if dias_restantes <= 1:

        frase = buscar_frase()

        return (
            f"⚠️ A atividade '{nome}' está perto do prazo!\n\n"
            f"{frase}"
        )

    return None


def alerta_baixa_prioridade(nome):

    frase = buscar_frase()

    return (
        f"📌 Não esqueça da atividade '{nome}' "
        f"mesmo sendo baixa prioridade!\n\n"
        f"{frase}"
    )


def mensagem_conclusao(nome):

    return (
        f"🎉 Parabéns por concluir '{nome}'!\n\n"
        f"Agora faça uma pequena pausa "
        f"antes da próxima tarefa 😊"
    )
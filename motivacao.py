import requests
from datetime import datetime

def buscar_frase():
    try:
        resposta = requests.get("https://zenquotes.io/api/random")

        if resposta.status_code == 200:
            dados = resposta.json()

            frase = dados[0]["q"]
            autor = dados[0]["a"]

            return f'"{frase}" - {autor}'

    except:
        return "Continue focado nos  seus estudos!"


def alerta_prazo(nome, data_entrega):

    hoje = datetime.now().date()

    prazo = datetime.strptime(data_entrega, "%d/%m/%Y").date()

    dias_restantes = (prazo - hoje).days

    if dias_restantes <= 1:
        print(f"\n⚠️ A atividade '{nome}' está perto do prazo!")
        print(buscar_frase())


def alerta_baixa_prioridade(nome):

    print(f"\n📌 Não esqueça da atividade '{nome}' mesmo sendo baixa prioridade!")
    print(buscar_frase())


def mensagem_conclusao(nome):

    print(f"\n🎉 Parabéns por concluir '{nome}'!")
    print("Agora faça uma pequena pausa antes da próxima tarefa 😊")
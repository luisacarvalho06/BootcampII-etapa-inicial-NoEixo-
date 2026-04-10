from datetime import datetime

ordem_prioridade = {"Alta": 1, "Média": 2, "Baixa": 3}


def validar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def adicionar_tarefa(lista, nome, data, prioridade):
    if not nome or not data:
        return False

    if not validar_data(data):
        return False

    lista.append({
        "nome": nome,
        "data": data,
        "prioridade": prioridade,
        "concluida": False
    })

    ordenar_tarefas(lista)
    return True


def remover_tarefa(lista, index):
    if index < 0 or index >= len(lista):
        return False

    lista.pop(index)
    return True


def concluir_tarefa(lista, index):
    if index < 0 or index >= len(lista):
        return False

    lista[index]["concluida"] = True
    return True


def editar_tarefa(lista, index, nome, data, prioridade):
    if index < 0 or index >= len(lista):
        return False

    if not validar_data(data):
        return False

    lista[index] = {
        "nome": nome,
        "data": data,
        "prioridade": prioridade,
        "concluida": False
    }

    ordenar_tarefas(lista)
    return True


def ordenar_tarefas(lista):
    lista.sort(key=lambda t: ordem_prioridade[t["prioridade"]])
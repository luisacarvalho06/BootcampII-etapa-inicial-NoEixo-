import tkinter as tk
from tkinter import messagebox
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

tarefas = []

def carregar_tarefas():
    global tarefas
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            tarefas = json.load(f)
    else:
        tarefas = []

def salvar_tarefas():
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

def formatar_data(event):
    texto = entry_data.get().replace("/", "")

    if not texto.isdigit():
        entry_data.delete(0, tk.END)
        return

    novo_texto = ""

    if len(texto) >= 2:
        novo_texto += texto[:2] + "/"
    else:
        novo_texto += texto

    if len(texto) >= 4:
        novo_texto += texto[2:4] + "/"
        novo_texto += texto[4:8]
    else:
        novo_texto += texto[2:]

    entry_data.delete(0, tk.END)
    entry_data.insert(0, novo_texto)

def adicionar_tarefa_gui():
    nome = entry_nome.get()
    data = entry_data.get()
    prioridade = prioridade_var.get()

    sucesso = adicionar_tarefa(tarefas, nome, data, prioridade)

    if not sucesso:
        messagebox.showerror("Erro", "Dados inválidos!")
        return

    # ALERTA DE PRAZO
    alerta = alerta_prazo(nome, data)

    if alerta:
        messagebox.showwarning(
            "Prazo Próximo",
            alerta
        )

    # ALERTA DE BAIXA PRIORIDADE
    if prioridade == "Baixa":

        mensagem = alerta_baixa_prioridade(nome)

        messagebox.showinfo(
            "Lembrete",
            mensagem
        )

    salvar_tarefas()
    atualizar_lista()
    limpar_campos()

def atualizar_lista():
    for widget in frame_lista.winfo_children():
        widget.destroy()

    for i, tarefa in enumerate(tarefas):
        cor = "green"
        if tarefa["prioridade"] == "Alta":
            cor = "red"
        elif tarefa["prioridade"] == "Média":
            cor = "yellow"

        frame = tk.Frame(frame_lista, bg=cor, pady=5)
        frame.pack(fill="x", padx=5, pady=2)

        texto = f"{tarefa['nome']} - {tarefa['data']}"

        if tarefa["concluida"]:
            texto += " ✔"

        label = tk.Label(frame, text=texto, bg=cor)
        label.pack(side="left", padx=10)

        tk.Button(frame, text="✔", command=lambda i=i: concluir_tarefa_gui(i)).pack(side="right")
        tk.Button(frame, text="X", command=lambda i=i: remover_tarefa_gui(i)).pack(side="right")
        tk.Button(frame, text="✏️", command=lambda i=i: editar_tarefa_gui(i)).pack(side="right")

def editar_tarefa_gui(index):
    tarefa = tarefas[index]

    entry_nome.delete(0, tk.END)
    entry_nome.insert(0, tarefa["nome"])

    entry_data.delete(0, tk.END)
    entry_data.insert(0, tarefa["data"])

    prioridade_var.set(tarefa["prioridade"])

    remover_tarefa(tarefas, index)
    salvar_tarefas()
    atualizar_lista()

def concluir_tarefa_gui(index):

    nome_tarefa = tarefas[index]["nome"]

    sucesso = concluir_tarefa(tarefas, index)

    if not sucesso:
        messagebox.showerror("Erro", "Erro ao concluir tarefa!")
        return

    mensagem = mensagem_conclusao(nome_tarefa)

    messagebox.showinfo(
        "Tarefa Concluída",
        mensagem
    )

    salvar_tarefas()
    atualizar_lista()

def remover_tarefa_gui(index):
    sucesso = remover_tarefa(tarefas, index)

    if not sucesso:
        messagebox.showerror("Erro", "Erro ao remover tarefa!")
        return

    salvar_tarefas()
    atualizar_lista()

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_data.delete(0, tk.END)

def verificar_alertas_ao_iniciar():

    for tarefa in tarefas:

        # Ignora tarefas concluídas
        if tarefa["concluida"]:
            continue

        nome = tarefa["nome"]
        data = tarefa["data"]
        prioridade = tarefa["prioridade"]

        # ALERTA DE PRAZO
        alerta = alerta_prazo(nome, data)

        if alerta:

            messagebox.showwarning(
                "Prazo Próximo",
                alerta
            )

        # ALERTA DE BAIXA PRIORIDADE
        if prioridade == "Baixa":

            mensagem = alerta_baixa_prioridade(nome)

            messagebox.showinfo(
                "Lembrete",
                mensagem
            )

root = tk.Tk()
root.title("Organizador de Estudos")
root.state('zoomed')
root.configure(bg="#f0f0f0")

titulo = tk.Label(root, text="📚 Organizador de Estudos", font=("Arial", 18), bg="#0945b6", fg="white")
titulo.pack(fill="x")

frame_form = tk.Frame(root, bg="white", pady=10)
frame_form.pack(fill="x", padx=20, pady=20)

tk.Label(frame_form, text="Tarefa:", bg="white").grid(row=0, column=0, padx=5, pady=5)
entry_nome = tk.Entry(frame_form, width=30)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Data (DD/MM/AAAA):", bg="white").grid(row=1, column=0)

entry_data = tk.Entry(frame_form, width=20)
entry_data.grid(row=1, column=1)
entry_data.bind("<KeyRelease>", formatar_data)

tk.Label(frame_form, text="Prioridade:", bg="white").grid(row=2, column=0)

prioridade_var = tk.StringVar(value="Baixa")
tk.OptionMenu(frame_form, prioridade_var, "Alta", "Média", "Baixa").grid(row=2, column=1)

tk.Button(
    frame_form,
    text="Adicionar Tarefa",
    bg="#2e8b57",
    fg="white",
    command=adicionar_tarefa_gui
).grid(row=3, columnspan=2, pady=10)

frame_lista = tk.Frame(root, bg="#f0f0f0")
frame_lista.pack(fill="both", expand=True, padx=20, pady=10)

carregar_tarefas()
atualizar_lista()

verificar_alertas_ao_iniciar()

root.mainloop()
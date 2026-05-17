# 📚 Organizador de Estudos — No Eixo

🔗 **Acesse a aplicação:**  
https://organizadordetarefas0.streamlit.app/

---

# 🧠 Problema

A falta de organização nos estudos pode gerar impactos significativos no desempenho acadêmico e na saúde mental. Muitas pessoas enfrentam dificuldades para visualizar suas pendências de forma clara, o que provoca sobrecarga mental, procrastinação e perda de produtividade.

A desorganização não é apenas visual — ela força o cérebro a lidar constantemente com excesso de informações sem estrutura, aumentando o estresse e a ansiedade no dia a dia.

---

# 💡 Solução

O **No Eixo** é um aplicativo web desenvolvido para auxiliar estudantes na organização de tarefas acadêmicas, oferecendo um ambiente simples, intuitivo e funcional.

A aplicação permite cadastrar, acompanhar e concluir tarefas de forma prática, além de fornecer:

- alertas de prazo;
- lembretes automáticos;
- mensagens motivacionais dinâmicas;
- acompanhamento de prioridades.

Com isso, o sistema ajuda o usuário a transformar intenção em ação, trazendo mais clareza, produtividade e tranquilidade para sua rotina.

---

# 🎯 Público-Alvo

- Estudantes que desejam organizar seus estudos e tarefas acadêmicas;
- Pessoas que buscam melhorar produtividade e gerenciamento de tempo.

---

## Pré-Visualização
<img width="1919" height="1034" alt="Captura de tela 2026-05-16 201356" src="https://github.com/user-attachments/assets/c2345d47-e35d-446e-9c07-0e34f20da3ba" />
<img width="1919" height="1023" alt="Captura de tela 2026-05-16 201408" src="https://github.com/user-attachments/assets/e41d7173-5abf-4347-a2a0-b439d6549c84" />
<img width="1919" height="1031" alt="Captura de tela 2026-05-16 201424" src="https://github.com/user-attachments/assets/224cb269-6d76-4fb1-a5df-096dcab788ca" />
<img width="1919" height="883" alt="Captura de tela 2026-05-16 205051" src="https://github.com/user-attachments/assets/daa7d70e-8ca2-4ff3-b70e-44a3c0e94731" />
<img width="1814" height="467" alt="Captura de tela 2026-05-16 205114" src="https://github.com/user-attachments/assets/fc7b81ec-6ff5-4e29-b157-83f936bf9c53" />

---

# ⚙️ Funcionalidades

## 📌 Gerenciamento de tarefas

- Adicionar tarefas;
- Editar tarefas;
- Excluir tarefas;
- Concluir tarefas;
- Definir datas de entrega;
- Organização por prioridades.

---

## 🎨 Sistema de prioridades

| Prioridade | Cor |
|---|---|
| Alta | 🟥 Vermelho |
| Média | 🟨 Amarelo |
| Baixa | 🟩 Verde |

---

## 🚨 Alertas inteligentes

O sistema possui alertas automáticos para:

- tarefas próximas do prazo;
- tarefas de baixa prioridade;
- conclusão de atividades.

---

## 💬 Mensagens motivacionais

A aplicação consome uma API pública externa para exibir frases motivacionais dinâmicas ao usuário, incentivando foco e produtividade.

As frases também podem ser traduzidas automaticamente para melhorar a experiência do usuário brasileiro.

---

# 🔌 Integração com API

## API utilizada

👉 https://zenquotes.io/api/random

## Objetivo da integração

Buscar frases motivacionais aleatórias para serem exibidas durante o uso da aplicação.

## Valor agregado

- Melhor experiência do usuário;
- Aplicação mais dinâmica;
- Incentivo à produtividade;
- Engajamento durante os estudos.

---

# 🧪 Testes Automatizados

O projeto possui testes automatizados de integração utilizando Pytest, garantindo que a comunicação com a API funcione corretamente.

## Executar testes

```bash
py -m pytest
```
---

## 🔄 Integração Contínua (CI/CD)

O projeto utiliza GitHub Actions para execução automática de:

- testes automatizados;
- validação do código;
- verificação da pipeline.

✔️ Pipeline configurada e funcionando corretamente.

---

## 🚀 Deploy

A aplicação foi publicada utilizando Streamlit Cloud.

🔗 **Link público:**
https://organizadordetarefas0.streamlit.app/

--- 

## 🛠️ Tecnologias Utilizadas

- Python
- Streamlit
- Requests
- Pytest
- GitHub Actions
- JSON

---

## 💻 Instalação

Clone o repositório
```
git clone https://github.com/luisacarvalho06/BootcampII-etapa-inicial-NoEixo-
```
```
cd BootcampII-etapa-inicial-NoEixo-
```

---

## 📦 Instalação das dependências

```
py -m pip install -r requirements.txt
```

---

## ▶️ Execução do Projeto

```
python -m streamlit run app.py
```

---

## 🔀 Fluxo de Desenvolvimento

O projeto seguiu um fluxo de desenvolvimento semelhante ao utilizado no mercado de trabalho:

- Criação de Issue no GitHub;
- Criação da branch entrega-intermediaria;
- Desenvolvimento da funcionalidade;
- Integração com API externa;
- Implementação de testes automatizados;
- Configuração de CI/CD com GitHub Actions;
- Deploy da aplicação;
- Criação de Pull Request;
- Merge na branch principal.

---

## 📁 Estrutura do Projeto

```
📦 BootcampII-etapa-inicial-NoEixo-
 ┣ 📂 src
 ┃ ┣ 📜 app.py
 ┃ ┣ 📜 logica.py
 ┃ ┣ 📜 motivacao.py
 ┃ ┗ 📜 tarefas.json
 ┣ 📜 requirements.txt
 ┣ 📜 test_api.py
 ┣ 📜 README.md
 ┗ 📂 .github/workflows
```

---

## 📦 Versão

1.0.0

## 👩‍💻 Autora

Luisa Carvalho

🔗 GitHub:
https://github.com/luisacarvalho06

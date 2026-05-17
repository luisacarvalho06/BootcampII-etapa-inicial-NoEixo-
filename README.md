# Organizador de Estudos — No Eixo

🔗 **Acesse a aplicação:**  
https://organizadordetarefas0.streamlit.app/

---

# Problema

A falta de organização nos estudos pode gerar impactos significativos no desempenho acadêmico e na saúde mental. Muitas pessoas enfrentam dificuldades para visualizar suas pendências de forma clara, o que provoca sobrecarga mental, procrastinação e perda de produtividade.

A desorganização não é apenas visual — ela força o cérebro a lidar constantemente com excesso de informações sem estrutura, aumentando o estresse e a ansiedade no dia a dia.

---

# Solução

O **No Eixo** é um aplicativo web desenvolvido para auxiliar estudantes na organização de tarefas acadêmicas, oferecendo um ambiente simples, intuitivo e funcional.

A aplicação permite cadastrar, acompanhar e concluir tarefas de forma prática, além de fornecer:

- alertas de prazo;
- lembretes automáticos;
- mensagens motivacionais dinâmicas;
- acompanhamento de prioridades.

Com isso, o sistema ajuda o usuário a transformar intenção em ação, trazendo mais clareza, produtividade e tranquilidade para sua rotina.

---

# Público-Alvo

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

# Funcionalidades

## Gerenciamento de tarefas

- Adicionar tarefas;
- Editar tarefas;
- Excluir tarefas;
- Concluir tarefas;
- Definir datas de entrega;
- Organização por prioridades.

---

## Sistema de prioridades

| Prioridade | Cor |
|---|---|
| Alta | 🟥 Vermelho |
| Média | 🟨 Amarelo |
| Baixa | 🟩 Verde |

---

## Alertas inteligentes

O sistema possui alertas automáticos para:

- tarefas próximas do prazo;
- tarefas de baixa prioridade;
- conclusão de atividades.

---

## Mensagens motivacionais

A aplicação consome uma API pública externa para exibir frases motivacionais dinâmicas ao usuário, incentivando foco e produtividade.

As frases também podem ser traduzidas automaticamente para melhorar a experiência do usuário brasileiro.

---

# Integração com API

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

# Testes Automatizados

O projeto possui testes automatizados de integração utilizando Pytest, garantindo que a comunicação com a API funcione corretamente.

## Executar testes

```bash
py -m pytest
```
---

## Integração Contínua (CI/CD)

O projeto utiliza GitHub Actions para execução automática de:

- testes automatizados;
- validação do código;
- verificação da pipeline.

✔️ Pipeline configurada e funcionando corretamente.

---

## Deploy

A aplicação foi publicada utilizando Streamlit Cloud.

🔗 **Link público:**
https://organizadordetarefas0.streamlit.app/

--- 

## Tecnologias Utilizadas

- Python
- Streamlit
- Requests
- Pytest
- GitHub Actions
- JSON

---

## Instalação

Clone o repositório
```
git clone https://github.com/luisacarvalho06/BootcampII-etapa-inicial-NoEixo-
```
```
cd BootcampII-etapa-inicial-NoEixo-
```

---

## Instalação das dependências

```
py -m pip install -r requirements.txt
```

---

## Execução do Projeto

```
python -m streamlit run app.py
```

---

## Fluxo de Desenvolvimento

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

## Estrutura do Projeto

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

## Versão

1.0.0

## Autora

Luisa Carvalho

🔗 GitHub:
https://github.com/luisacarvalho06
# Organizador de estudos: No eixo

## Problema
A falta de organizadores de estudos na vida de pessoas já desorganizadas cria um efeito dominó que afeta profundamente o desempenho acadêmico e a saúde mental. A desorganização não é apenas visual, ela causa um cansaço mental crônico por forçar o cérebro a gerenciar excesso de informações sem estrutura.

## Solução
O No Eixo é um aplicativo web que cria um plano de ação claro em meio ao caos de obrigações pendentes, permitindo que as pessoas saibam exatamente o que e até quando devem executar suas tarefas. Ele traz tranquilidade e paz ao dia a dia, uma vez que transformam a intenção em ação.

## Público-Alvo
• Estuantes que desejam organizar suas pendências.

## Funcionalidades Principais
• Adicionar tarefas e suas respectivas datas
• Listar as prioridades sendo: 
  • 🟥Vermelho= Alta prioridade 
  • 🟨Amarelo= Média prioridade 
  • 🟩Verde: Baixa prioridade
• Editar tarefas e datas
• Excluir tarefas
• Concluir tarefas (removendo-as da lista)

## Pré-Visualização
<img width="1919" height="283" alt="image" src="https://github.com/user-attachments/assets/41ec0477-2b9d-44bb-9f25-242792ee6d17" />
<img width="1919" height="440" alt="Captura de tela 2026-04-11 005905" src="https://github.com/user-attachments/assets/3a01eb5e-fb59-43f9-be2e-e0d9f1da03b5" />
<img width="1917" height="377" alt="Captura de tela 2026-04-11 005932" src="https://github.com/user-attachments/assets/a817eb18-c8fe-4ffe-a349-2752fb54cadc" />
<img width="1919" height="376" alt="Captura de tela 2026-04-11 005955" src="https://github.com/user-attachments/assets/88d708c9-7def-43b0-9af5-752fa69f99e0" />
<img width="1919" height="326" alt="image" src="https://github.com/user-attachments/assets/0bc2b258-5da6-4fd2-bdf1-6d667e306fcd" />
<img width="1421" height="205" alt="Captura de tela 2026-04-11 000912" src="https://github.com/user-attachments/assets/ae8c9bc1-33e2-40ba-8259-49fa4125eee0" />

## Tecnologias Utilizadas
• Python 3.11+
• Pytest 
• Ruff 
• GitHub Actions 

## Instalação
Clone o repositorio:
```
git clone <URL_DO_REPOSITORIO>
cd BootcampII-etapa-inicial-NoEixo-
```
Instale as dependências:
```
py -m pip install -r requirements.txt
```
## Execução
Para rodar o aplicativo:
```
py src/NoEixo.py
```
## Testes
Para executar os testes automatizados:
```
py -m pytest
```

## Lint
Para verificar a qualidade e padronização do código:
```
ruff check .
```

## Versão
1.0.0

## Autor
Luisa Carvalho
https://github.com/luisacarvalho06

## Repositório
https://github.com/luisacarvalho06/BootcampII-etapa-inicial-NoEixo-

## Funcionalidades novas

- Alertas de prazo de atividades
- Mensagens motivacionais
- Integração com API ZenQuotes
- Teste de integração automatizado

## Tecnologias
- Python
- Requests
- Pytest
- GitHub Actions

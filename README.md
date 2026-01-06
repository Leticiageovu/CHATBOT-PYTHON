# 🤖 BotLet — Chatbot em Python

BotLet é um chatbot desenvolvido em Python com foco em aprendizado prático de **processamento de linguagem natural básico**, organização de projeto e **boas práticas de desenvolvimento**, incluindo testes automatizados e registro de logs.

---

## 🎯 Objetivo do Projeto

Este projeto foi criado com o objetivo de:
- Consolidar conhecimentos em Python
- Praticar lógica de chatbots baseados em intenções
- Trabalhar com normalização de texto
- Implementar testes automatizados com pytest
- Criar um projeto organizado e apresentável para portfólio

---

## 🧠 Funcionalidades

- Reconhecimento de intenções por palavras-chave
- Normalização de texto (remoção de acentos e case-insensitive)
- Respostas dinâmicas e aleatórias
- Registro de conversas em log com **data e hora**
- Testes automatizados com **pytest**
- Estrutura modular e escalável

---

## 🗂️ Estrutura do Projeto

Chatbot-python/

│

├── chatbot/

│ ├── init.py

│ ├── bot.py

│ └── utils.py

│

├── intents.json

├── logs/

│ └── conversas.txt

│

├── tests/

│ └── test_chatbot.py

│

├── main.py

├── requirements.txt

└── README.md

---

## 🚀 Como Executar o Projeto

### 1️⃣ Criar e ativar o ambiente virtual
``` bash
python -m venv venv
venv\Scripts\activate

```
---

2️⃣ Instalar dependências

```
pip install -r requirements.txt

```
---

<img width="1366" height="728" alt="Chatbot-python" src="https://github.com/user-attachments/assets/1bbc056c-fd08-4892-92fb-aea88e023fd4" />

---

3️⃣ Executar o chatbot

```
python main.py

```
---
### Executando os Testes

Este projeto utiliza pytest para testes automatizados.

```
pytest
```

---

### 📝 Logs de Conversa

Todas as interações são registradas em:

```
logs/conversas.txt
```

Cada mensagem contém data, hora, usuário e resposta do bot, facilitando auditoria e análise.

---

## 🔧 Tecnologias Utilizadas

- Python 3

- Pytest

- JSON

- Virtualenv

---

### 👩‍💻 Autora

### Letícia Geovú
#### Desenvolvedora | Python | Full Stack

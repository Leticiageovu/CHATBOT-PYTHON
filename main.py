import os
from chatbot.bot import Chatbot
from chatbot.utils import carregar_intents
from datetime import datetime

INTENTS_PATH = "chatbot/intents.json"
LOG_PATH = "logs/conversas.txt"

# Garante que a pasta de logs exista
os.makedirs("logs", exist_ok=True)


def salvar_conversa(remetente, mensagem):
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    registro = f"[{data_hora}] {remetente}: {mensagem}"

    with open(LOG_PATH, "a", encoding="utf-8") as arquivo:
        arquivo.write(registro + "\n")


def main():
    intents = carregar_intents(INTENTS_PATH)
    bot = Chatbot("BotLet", intents)

    print("🤖 BotLet iniciado! Digite 'sair' para encerrar.\n")

    while True:
        usuario = input("Você: ")
        salvar_conversa("Você", usuario)

        resposta = bot.responder(usuario)
        print(f"BotLet: {resposta}")
        salvar_conversa("BotLet", resposta)

        if "sair" in usuario.lower():
            print("👋 Conversa encerrada.")
            break


if __name__ == "__main__":
    main()

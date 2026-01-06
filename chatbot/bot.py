from chatbot.utils import encontrar_intencao, resposta_aleatoria

class Chatbot:
    def __init__(self, nome, intents):
        self.nome = nome
        self.intents = intents

    def responder(self, mensagem):
        mensagem = mensagem.lower()
        intencao = encontrar_intencao(mensagem, self.intents)

        if intencao:
            return resposta_aleatoria(self.intents, intencao)
        else:
            return "Desculpe, não entendi. Pode reformular?"

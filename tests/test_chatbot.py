import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from chatbot.bot import Chatbot
from chatbot.utils import carregar_intents

INTENTS_PATH = "chatbot/intents.json"


@pytest.fixture
def bot():
    intents = carregar_intents(INTENTS_PATH)
    return Chatbot("BotLet", intents)


def test_saudacao(bot):
    resposta = bot.responder("oi")
    assert resposta in bot.intents["saudacao"]["responses"]


def test_horario(bot):
    resposta = bot.responder("qual o horário?")
    assert resposta in bot.intents["horario"]["responses"]


def test_agradecimento(bot):
    resposta = bot.responder("obrigado")
    assert resposta in bot.intents["agradecimento"]["responses"]


def test_despedida(bot):
    resposta = bot.responder("tchau")
    assert resposta in bot.intents["despedida"]["responses"]

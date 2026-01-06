import json
import random
import unicodedata


def normalizar_texto(texto):
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = texto.encode("ascii", "ignore").decode("utf-8")
    return texto


def carregar_intents(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def encontrar_intencao(texto, intents):
    texto = normalizar_texto(texto)

    for intencao, dados in intents.items():
        for padrao in dados["patterns"]:
            padrao_normalizado = normalizar_texto(padrao)

            if padrao_normalizado in texto:
                return intencao

    return None


def resposta_aleatoria(intents, intencao):
    return random.choice(intents[intencao]["responses"])

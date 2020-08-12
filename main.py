from bot import Bot
from conversor import Conversor

# Ao iniciar o bot, também iniciamos o driver
wpp_bot = Bot()

# Setando o arquivo que iremos tranformar em lista posteriormente
conversor = Conversor('hp.txt')


def iniciar_bot():
    # Abre o whatsapp e entra na conversa do contato passado como parâmetro

    wpp_bot.inicia('Nome do contato')


def pega_lista():
    # Convertemos o arquivo txt para uma lista de string (cada linha do arquivo representa uma posição)

    lista_mensagens = conversor.converter()
    return lista_mensagens


def enviar():
    # Pega a totalidade do conteúdo do arquivo passado ao conversor e coloca na lista
    # Depois, envia cada mensagem da lista ao contato

    mensagens = pega_lista()
    for mensagem in mensagens:
        wpp_bot.envia_mensagem(mensagem)


iniciar_bot()
enviar()

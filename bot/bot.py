import sys
sys.path.append("../")
from c1.ExprVisitorEval import EvalVisitor
import datetime
from interprete import interprete
# importa l'API de Telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

"""Se crea una clase interprete parecida a la de la carpeta c1, pero que no esta en bucle"""
visitor = EvalVisitor()
# defineix una funció que saluda i que s'executarà quan el bot rebi el missatge /start


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hola! Soc un bot bàsic.")


def help(update, context):
    context.bot.send_message(
            chat_id=update.effective_chat.id, text="Soc un bot amb comandes /start, /help i /hora.")


def hora(update, context):
    missatge = str(datetime.datetime.now())
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=missatge)


def pol(update, context):
    miss_orig = update.message.text

    output = interprete.lector(visitor, miss_orig)

    if update.message.text[:4] == "draw":
        comienzo = miss_orig.find('"') + 1
        archivo = miss_orig[comienzo:]
        final = archivo.find('"')
        archivo = miss_orig[comienzo:final+comienzo]
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(archivo, 'rb'))

    if output is not None:
        context.bot.send_message(chat_id=update.effective_chat.id, text=output)

# declara una constant amb el access token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()

# crea objectes per treballar amb Telegram
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# indica que quan el bot rebi la comanda /start s'executi la funció start
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('hora', hora))
dispatcher.add_handler(CommandHandler('pol', pol))

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, pol))

# engega el bot
updater.start_polling()

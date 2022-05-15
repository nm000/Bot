
import os

# Telegram stuff
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

# Cesar stuff
import cesar
from cesar import encode, decode


def start(update: Update, context: CallbackContext):
    update.message.reply_text("¡Hola, Soy CASMYN \U0001F916! \n Cualquier indicación que necesites, favor escribe /help")


def content(update: Update, context: CallbackContext):
    update.message.reply_text(
        """CASMYN: bot creado para cifrar y descifrar palabras, oraciones o textos completos B).""")


def contact(update: Update, context: CallbackContext):
    update.message.reply_text("""
  BOT CREADO POR:
  Líder: 
    Nombre: Sonya Castro
    Mail: sonyac@uninorte.edu.co
  Miembro 1:
    Nombre: Natalia Mendonza
    Mail: npmendoza@uninorte.edu.co
    """
                              )


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""
  COMANDOS:
  /start -> Bienvenida
  /help -> Este menú
  /content -> Información sobre mí - el BOT - funcionalidades y lo que me gusta.
  /contact -> Contactar programadoras.
  /c -> Codifica, por el método de cifrado del César, un texto ingresado con un número 'x' de desplazamiento. 
  /d -> Decodifica, por el método de cifrado del César, un texto ingresado.
  """)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Lo siento, no pude reconocer lo que dijiste '%s'" % update.message.text)


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Lo siento, '%s' no es un comando valido" % update.message.text)


def codificar(update: Update, context: CallbackContext):
    text = (update.message.text).replace("/codificar ", "").replace("/c ", "")

    encode_text, typo_words = encode(text)

    update.message.reply_text(encode_text)


def decodificar(update: Update, context: CallbackContext):
    text = (update.message.text).replace(
        "/decodificar ", "").replace("/d ", "")

    decode_text = decode(text)
    update.message.reply_text(decode_text)


def main():
    PORT = int(os.environ.get('PORT', 5000))
    print("Server started!")

    # read file with the key gave by BotFather
    with open('key.txt', 'r') as f:
        KEY = f.read()

    # Permite que el bot ande, usando como servidor local el computador
    updater = Updater(KEY, use_context=True)

    # para aceptar los comandos
    disp = updater.dispatcher

    disp.add_handler(CommandHandler("start", start))
    disp.add_handler(CommandHandler("content", content))
    disp.add_handler(CommandHandler("help", help))
    disp.add_handler(CommandHandler("contact", contact))

    disp.add_handler(CommandHandler("c", codificar))

    disp.add_handler(CommandHandler("d", decodificar))

    disp.add_handler(MessageHandler(Filters.text, unknown))
    disp.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=KEY)

    updater.bot.setWebhook('https://casmyn-bot.herokuapp.com/' + KEY)

    # updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

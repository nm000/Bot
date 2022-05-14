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

print("Server started!")

#read file with the key gave by BotFather
with open('key.txt', 'r') as f:
    KEY = f.read()


def start(update: Update, context: CallbackContext):
  update.message.reply_text("Hola, Soy un Robot \U0001F916")


def content(update: Update, context: CallbackContext):
  update.message.reply_text(
    """Tengo un robot, yo lo hago funcionar, \n él es el mejor y vamos a jugar.""")


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
  /help -> Menú
  /content -> Información sobre mí - el BOT -
  /contact -> Contactar programadoras.
  /c -> Codifica, por el método de cifrado del César, un texto ingresado con un número 'x' de desplazamiento. 
  /d -> Decodifica, por el método de cifrado del César, un texto ingresado.
  """)


def unknown_text(update: Update, context: CallbackContext):
  update.message.reply_text(
      "Lo siento, no pude reconocer lo que dijiste '%s'" % update.message.text)


def unknown(update: Update, context: CallbackContext):
  update.message.reply_text("Lo siento, '%s' no es un comando valido" % update.message.text)


def codificar(update: Update, context: CallbackContext):
  text = (update.message.text).replace("/codificar ", "").replace("/c ", "")

  encode_text, typo_words = encode(text)
  
  update.message.reply_text(encode_text)


def decodificar(update: Update, context: CallbackContext):
  text = (update.message.text).replace("/decodificar ", "").replace("/d ", "")

  decode_text = decode(text)
  update.message.reply_text(decode_text)
  
#Permite que el bot ande, usando como servidor local el computador
updater = Updater(KEY, use_context = True)

#para aceptar los comandos
disp = updater.dispatcher

disp.add_handler(CommandHandler("start", start))
disp.add_handler(CommandHandler("content", content))
disp.add_handler(CommandHandler("help", help))
disp.add_handler(CommandHandler("contact", contact))

disp.add_handler(CommandHandler("c", codificar))

disp.add_handler(CommandHandler("d", decodificar))

disp.add_handler(MessageHandler(Filters.text, unknown))
disp.add_handler(MessageHandler(Filters.command, unknown))

updater.start_polling()
updater.idle()

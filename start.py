import os
import importlib.util
import telebot
import random
from variabili import SUPPORT_GROUP_ID, assistenza_sessions
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

# Crea un'istanza del bot
bot = telebot.TeleBot(TOKEN)

# Carica dinamicamente i comandi dalla cartella 'comandi'
def load_commands(bot):
    print('Caricamento comandi...')
    commands_path = 'comandi'
    for filename in os.listdir(commands_path):
        if filename.endswith('.py'):
            file_path = os.path.join(commands_path, filename)
            spec = importlib.util.spec_from_file_location(filename[:-3], file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            print(dir(module))
            module.register(bot)

# Gestisci i messaggi degli utenti e inoltrali al gruppo di supporto
@bot.message_handler(func=lambda message: message.chat.id in assistenza_sessions and assistenza_sessions[message.chat.id]['active'])
def forward_to_support(message):
    user_id = message.chat.id
    forwarded_message = bot.forward_message(SUPPORT_GROUP_ID, user_id, message.message_id)
    assistenza_sessions[user_id]['last_forwarded_message_id'] = forwarded_message.message_id

    # Controlla se il comando "stopassistenza" è stato inviato
    #if message.text == "stopassistenza":
    #    assistenza_sessions[user_id]['active'] = False

# Gestisci i messaggi dal gruppo di supporto e inoltrali all'utente specifico
@bot.message_handler(func=lambda message: message.chat.id == SUPPORT_GROUP_ID)
def forward_to_user(message):
    if message.reply_to_message and message.reply_to_message.forward_from:
        user_id = message.reply_to_message.forward_from.id
        if user_id in assistenza_sessions and assistenza_sessions[user_id]['active']:
            bot.send_message(user_id, message.text)

            # Controlla se il comando "staffstopassistenza" è stato inviato
            #if message.text == "staffstopassistenza":
            #   assistenza_sessions[user_id]['active'] = False
    else:
        # Identificare l'utente dal contenuto del messaggio
        original_message_id = message.reply_to_message.message_id if message.reply_to_message else None
        if original_message_id:
            for user_id, session in assistenza_sessions.items():
                if session['last_forwarded_message_id'] == original_message_id:
                    bot.send_message(user_id, message.text)
                    break


# Carica i comandi personalizzati
load_commands(bot)

# Gestisci tutti gli altri messaggi
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, 'Non ho capito il tuo messaggio.')

# Avvia il bot
bot.polling()
print("Bot avviato con successo!")

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
    commands_path = 'comandi'
    for filename in os.listdir(commands_path):
        if filename.endswith('.py'):
            file_path = os.path.join(commands_path, filename)
            spec = importlib.util.spec_from_file_location(filename[:-3], file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            print(dir(module))
            module.register(bot)

# Gestisci il comando /staffstopassistenza (staff)
@bot.message_handler(commands=['staffstopassistenza'])
def handle_staff_stop_assistenza(message):
    if message.reply_to_message and message.reply_to_message.forward_from:
        user_id = message.reply_to_message.forward_from.id
        if user_id in assistenza_sessions:
            assistenza_sessions[user_id]['active'] = False
            bot.send_message(message.chat.id, f"La sessione di assistenza dell'utente {user_id} è stata terminata dallo staff.")
            bot.send_message(user_id, 'La tua sessione di assistenza è stata terminata dallo staff. Grazie per averci contattato!')

# Gestisci il comando /assistenza
@bot.message_handler(commands=['assistenza'])
def handle_assistenza(message):
    user_id = message.chat.id
    assistenza_sessions[user_id] = {
        'user_chat_id': user_id,
        'active': True,
        'last_forwarded_message_id': None
    }
    bot.reply_to(message, 'Sei in contatto con il supporto. Invia i tuoi messaggi e ti risponderemo al più presto.')

# Gestisci i messaggi degli utenti e inoltrali al gruppo di supporto
@bot.message_handler(func=lambda message: message.chat.id in assistenza_sessions and assistenza_sessions[message.chat.id]['active'])
def forward_to_support(message):
    user_id = message.chat.id
    forwarded_message = bot.forward_message(SUPPORT_GROUP_ID, user_id, message.message_id)
    assistenza_sessions[user_id]['last_forwarded_message_id'] = forwarded_message.message_id

# Gestisci i messaggi dal gruppo di supporto e inoltrali all'utente specifico
@bot.message_handler(func=lambda message: message.chat.id == SUPPORT_GROUP_ID)
def forward_to_user(message):
    if message.reply_to_message and message.reply_to_message.forward_from:
        user_id = message.reply_to_message.forward_from.id
        if user_id in assistenza_sessions and assistenza_sessions[user_id]['active']:
            bot.send_message(user_id, message.text)
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

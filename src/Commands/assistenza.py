from telebot import types
from variabili import assistenza_sessions

def register(bot):
    @bot.message_handler(commands=['assistenza'])
    def handle_assistenza(message):
        user_id = message.chat.id
        assistenza_sessions[user_id] = {
            'user_chat_id': user_id,
            'active': True,
            'last_forwarded_message_id': None
        }

        # Creazione dei bottoni
        keyboard = types.ReplyKeyboardMarkup(row_width=1)
        close_button = types.KeyboardButton('Chiudi sessione')
        keyboard.add(close_button)

        bot.send_message(user_id, 'Sei in contatto con il supporto. Invia i tuoi messaggi e ti risponderemo al più presto.', reply_markup=keyboard)

    @bot.message_handler(commands=['stopassistenza'])
    def handle_stop_assistenza(message):
        user_id = message.chat.id
        if user_id in assistenza_sessions:
            del assistenza_sessions[user_id]
            bot.reply_to(message, 'Sessione di assistenza terminata.')
        else:
            bot.reply_to(message, 'Non sei attualmente in una sessione di assistenza.')

    @bot.message_handler(commands=['staffstopassistenza'])
    def handle_staff_stop_assistenza(message):
        if message.reply_to_message and message.reply_to_message.forward_from:
            user_id = message.reply_to_message.forward_from.id
            if user_id in assistenza_sessions:
                assistenza_sessions[user_id]['active'] = False
                bot.send_message(message.chat.id, f"La sessione di assistenza dell'utente {user_id} è stata terminata dallo staff.")
                bot.send_message(user_id, 'La tua sessione di assistenza è stata terminata dallo staff. Grazie per averci contattato!')
        pass

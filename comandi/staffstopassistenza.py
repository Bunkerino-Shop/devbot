from variabili import SUPPORT_GROUP_ID, assistenza_sessions
print('Caricato comando staffstopassistenza')
def register(bot):
    @bot.message_handler(commands=['staffstopassistenza'])
    def handle_staff_stop_assistenza(message):
        if message.reply_to_message and message.reply_to_message.forward_from:
            user_id = message.reply_to_message.forward_from.id
            if user_id in assistenza_sessions:
                assistenza_sessions[user_id]['active'] = False
                bot.send_message(message.chat.id, f"La sessione di assistenza dell'utente {user_id} è stata terminata dallo staff.")
                bot.send_message(user_id, 'La tua sessione di assistenza è stata terminata dallo staff. Grazie per averci contattato!')
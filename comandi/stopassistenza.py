from variabili import SUPPORT_GROUP_ID, assistenza_sessions
def register(bot):
    @bot.message_handler(commands=['stopassistenza'])
    def handle_stop_assistenza(message):
        user_id = message.chat.id
        if user_id in assistenza_sessions:
            assistenza_sessions[user_id]['active'] = False
            bot.reply_to(message, 'La tua sessione di assistenza è stata terminata. Grazie per averci contattato!')
            # Notifica il gruppo di supporto
            bot.send_message(SUPPORT_GROUP_ID, f"L'utente {user_id} ha terminato la sessione di assistenza.")
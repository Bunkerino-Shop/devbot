from variabili import SUPPORT_GROUP_ID, assistenza_sessions
print('Caricato comando stopassistenza')
def register(bot):
    @bot.message_handler(commands=['stopassistenza'])
    def handle_stop_assistenza(message):
        user_id = message.chat.id
        if user_id in assistenza_sessions:
            assistenza_sessions[user_id]['active'] = False
            bot.send_message(user_id, 'La tua sessione di assistenza è stata terminata. Grazie per averci contattato!')
            bot.send_message(SUPPORT_GROUP_ID, f"La sessione di assistenza dell'utente {user_id} è stata terminata dall'utente.")

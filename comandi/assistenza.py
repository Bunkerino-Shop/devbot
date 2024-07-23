from variabili import SUPPORT_GROUP_ID, assistenza_sessions
print('Caricato comando assistenza')
def register(bot):
    @bot.message_handler(commands=['assistenza'])
    def handle_assistenza(message):
        user_id = message.chat.id
        assistenza_sessions[user_id] = {
            'user_chat_id': user_id,
            'active': True,
            'last_forwarded_message_id': None
        }
        bot.reply_to(message, 'Sei in contatto con il supporto. Invia i tuoi messaggi e ti risponderemo al più presto.')

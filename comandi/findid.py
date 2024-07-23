def register(bot):
    @bot.message_handler(commands=['findid'])
    def handle_findid(message):
        bot.reply_to(message, f'Il tuo ID chat è: {message.chat.id}')

def register(bot):
    @bot.message_handler(commands=['example'])
    def handle_example(message):
        bot.reply_to(message, 'Questo è un esempio di comando personalizzato.')

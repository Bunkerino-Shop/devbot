def register(bot):
    @bot.message_handler(commands=['help'])
    def handle_help(message):
        bot.reply_to(message, 'Questo bot ti aiuta con il mondo della programmazione.')
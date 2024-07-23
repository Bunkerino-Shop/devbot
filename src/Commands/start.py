def register(bot):
    @bot.message_handler(commands=['start'])
    def handle_start(message):
        bot.reply_to(message, 'Ciao! Benvenuto nel devbot di Telegram, scrivi se hai bisogno di aiut sul mondo della programmazione.')
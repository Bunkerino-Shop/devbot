import random
import telebot

# Inserisci il token del tuo bot ottenuto da BotFather
TOKEN = '6710147688:AAEPURsD-C8z2teoaoygEufRBGfvxI81xYU'

# Crea un'istanza del bot
bot = telebot.TeleBot(TOKEN)

# Gestisci il comando /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, 'Ciao! Benvenuto nel devbot di Telegram, scrivi se hai bisogno di aiut sul mondo della programmazione.')

# Gestisci il comando /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, 'Questo bot ti aiuta con il mondo della programmazione.')

# Gestisci il comando /example
@bot.message_handler(commands=['example'])
def handle_example(message):
    # Esempio di implementazione di un comando personalizzato
    bot.reply_to(message, 'Questo è un esempio di comando personalizzato.')

# Gestisci il comando /info
@bot.message_handler(commands=['info'])
def handle_info(message):
    # Esempio di implementazione di un altro comando personalizzato
    bot.reply_to(message, 'Questo è un altro esempio di comando personalizzato.')

# Gestisci il comando /search
@bot.message_handler(commands=['search'])
def handle_search(message):
    # Esempio di implementazione di un comando per la ricerca
    query = message.text.split('/search ')[1]
    results = perform_search(query)
    bot.reply_to(message, f'Ecco i risultati della ricerca: {results}')

# Gestisci il comando /image
@bot.message_handler(commands=['image'])
def handle_image(message):
    # Esempio di implementazione di un comando per inviare un'immagine
    photo_url = 'https://example.com/image.jpg'
    bot.send_photo(message.chat.id, photo_url, caption="Ecco un'immagine di esempio.")

# Gestisci il comando /random
@bot.message_handler(commands=['random'])
def handle_random(message):
    # Esempio di implementazione di un comando per generare un numero casuale
    random_number = random.randint(1, 10)
    bot.reply_to(message, f'Il numero casuale generato è: {random_number}')


# Gestisci il comando /linux
@bot.message_handler(commands=['linux'])
def handle_example(message):
    # Esempio di implementazione di un comando personalizzato
    bot.reply_to(message, 'Ecco la guida completa su coame mettere linux sul tuo dispositivo.')


































# Gestisci tutti gli altri messaggi
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, 'Non ho capito il tuo messaggio.')

# Avvia il bot
bot.polling()
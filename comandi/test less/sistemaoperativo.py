from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext


# Funzione di gestione del comando /sistemaoperativo
def sistema_operativo(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Guida per Windows", callback_data='windows'),
            InlineKeyboardButton("Guida per macOS", callback_data='macos'),
        ],
        [InlineKeyboardButton("Guida per Linux", callback_data='linux')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Seleziona il sistema operativo per la guida:', reply_markup=reply_markup)

# Funzione di gestione dei callback dei bottoni
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == 'windows':
        query.edit_message_text(text="Hai selezionato Windows. Ecco la guida: [link alla guida di Windows]")
    elif query.data == 'macos':
        query.edit_message_text(text="Hai selezionato macOS. Ecco la guida: [link alla guida di macOS]")
    elif query.data == 'linux':
        query.edit_message_text(text="Hai selezionato Linux. Ecco la guida: [link alla guida di Linux]")

def main() -> None:
    # Inserisci qui il tuo token
    updater = Updater("6710147688:AAEPURsD-C8z2teoaoygEufRBGfvxI81xYU", use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("sistemaoperativo", sistema_operativo))
    dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
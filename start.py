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
    bot.reply_to(message, """
📌Ecco la guida completa su coame mettere linux sul tuo dispositivo. (segui attentamente i passaggi)
@1: Scaricare l'immagine ISO di Linux
Scegliere una distribuzione Linux: Vai al sito ufficiale della distribuzione Linux che desideri installare (ad esempio Ubuntu (https://www.ubuntu-it.org/download), Fedora (https://fedoraproject.org/it/coreos/), Debian (https://www.debian.org/index.it.html)).

Per Ubuntu: ubuntu.com
Per Fedora: getfedora.org
Per Debian: debian.org

Scaricare l'immagine ISO: Trova la sezione di download e scarica l'immagine ISO della versione desiderata.

@2: Preparare la chiavetta USB
Procurarsi una chiavetta USB: Assicurati di avere una chiavetta USB con almeno 4 GB di spazio libero.

Scaricare un programma di creazione di unità USB avviabile:

Per Windows: Usa programmi come Rufus (rufus.ie), balenaEtcher (balena.io/etcher).
Per MacOS: Usa balenaEtcher.
Per Linux: Usa dd da terminale o programmi come balenaEtcher.
Installare il programma: Segui le istruzioni sul sito ufficiale per installare ilhttps://t.me/ programma scelto.

Creare l'unità USB avviabile:

Rufus:
Collega la chiavetta USB al computer.
Apri Rufus.
Seleziona la chiavetta USB nel menu a discesa "Dispositivo".
Clicca su "Seleziona" e scegli l'immagine ISO scaricata.
Imposta lo schema di partizione su "MBR" o "GPT" a seconda del tuo sistema.
Clicca su "Start" e attendi il completamento del processo.

balenaEtcher:
Collega la chiavetta USB al computer.
Apri balenaEtcher.
Clicca su "Flash from file" e scegli l'immagine ISO scaricata.
Seleziona la chiavetta USB.
Clicca su "Flash!" e attendi il completamento del processo.

@3: Avviare dal dispositivo USB
Collegare la chiavetta USB al dispositivo: Inserisci la chiavetta USB nel dispositivo su cui desideri installare Linux.

Accedere al BIOS/UEFI:

Riavvia il dispositivo.
Durante l'avvio, premi il tasto appropriato per entrare nel BIOS/UEFI (solitamente F2, F12, DEL o ESC).
Impostare l'avvio dalla chiavetta USB:

Cerca la sezione "Boot" nel BIOS/UEFI.
Cambia l'ordine di avvio per fare in modo che la chiavetta USB sia il primo dispositivo di avvio.
Salva le modifiche e esci dal BIOS/UEFI (solitamente premendo F10).
Passo 4: Installare Linux
Avviare il processo di installazione: Il dispositivo dovrebbe ora avviarsi dalla chiavetta USB e visualizzare il menu di installazione di Linux.

Seguire le istruzioni sullo schermo:

Seleziona "Install Linux" o una voce simile.
Scegli la lingua, il layout della tastiera, e altre preferenze regionali.
Connettiti a una rete Wi-Fi, se richiesto.
Preparare il disco:

Seleziona il tipo di installazione (ad esempio, installazione accanto a un altro sistema operativo, cancellare il disco e installare Linux, o altro).
Se scegli di partizionare manualmente il disco, crea almeno una partizione root (/) e una partizione swap (consigliata ma opzionale).
Continuare con l'installazione:

Fornisci le informazioni richieste (nome utente, password, nome del computer, ecc.).
Conferma le impostazioni e avvia l'installazione.
Completare l'installazione:

Attendi il completamento del processo di installazione.
Una volta completata, ti verrà chiesto di riavviare il dispositivo.
Rimuovi la chiavetta USB quando ti viene chiesto di farlo.
Passo 5: Avvio nel nuovo sistema Linux
Riavviare il dispositivo: Dopo il riavvio, il dispositivo dovrebbe avviarsi nel nuovo sistema operativo Linux.

Configurare il sistema: Segui le eventuali configurazioni post-installazione, come aggiornamenti del sistema, installazione di driver e software aggiuntivi. Consigliamo inoltre di installare yay (puoi trovare la guida completa facendo il comando /yay) """)


# Gestisci il comando /yay
@bot.message_handler(commands=['yay'])
def handle_example(message):
    # Esempio di implementazione di un comando personalizzato
    bot.reply_to(message, """
Ecco la guida completa su come scaricare yay sul tuo sistema operativo LINUX. 
1 Apri la konsole. 

2 Esegui in ordine i seguenti comandi nella konsole. 
    2.1 sudo pacman -Syu 
    2.2 sudo pacman -S --needed git base-devel 
    2.3 git clone https://aur.archlinux.org/yay.git 
    2.3 cd yay 
    2.4 makepkg -si 

Perfetto ora puoi utilizzare tranquillamente 'yay'.""")



#@bot.message_handler(commands=['lpk-assistenza-wow'])
#def handle_example(message):
#    GRUPPO_ASSISTENZA_ID = message.chat.id
#    
## Gestisci il comando /assistenza
#@bot.message_handler(commands=['assistenza'])
#def handle_assistenza(message):
#    chat_id = message.chat.idrsazione corrente
#             message.chat.id
#    # Invia un messaggio di notifica al gruppo di assistenza
#    bot.send_message(GRUPPO_ASSISTENZA_ID, f"Richiesta di assistenza da {message.from_user.first_name}: {message.text}")
## Aspetta la risposta dal gruppo di assistenza
#@bot.message_handler(func=lambda message: message.chat.id == GRUPPO_ASSISTENZA_ID)
#def handle_assistenza_response(message): message.chat.id == GRUPPO_ASSISTENZA_ID)
#    # Invia la risposta al diretto interessato
#    bot.send_message(chat_id, f"Risposta dal gruppo di assistenza: {message.text}")

































# Gestisci tutti gli altri messaggi
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, 'Non ho capito il tuo messaggio.')

# Avvia il bot
bot.polling()
print("Bot avviato con successo!")

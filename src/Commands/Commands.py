import logging
from telebot import TeleBot, types
from telebot.types import Message

class Commands:
    def __init__(self, bot: TeleBot, group_chat_id: int):
        """
        Initialize the Commands object and register commands with the bot.
        
        :param bot: The TeleBot instance to register commands on.
        :param group_chat_id: The ID of the group chat where messages are forwarded.
        """
        self.bot: TeleBot = bot
        self.group_chat_id: int = group_chat_id
        self.assistenza_sessions: dict = {}
        self.register_commands()

    def register_commands(self):
        """
        Register all commands for the bot.
        """

        @self.bot.message_handler(commands=['findid'])
        def handle_findid(message: Message):
            """
            Handle the /findid command by replying with the chat ID.
            
            :param message: The message object containing the command.
            """
            chat_id = message.chat.id
            logging.debug(f"Received /findid command from chat ID: {chat_id}")
            self.bot.reply_to(message, f'Il tuo ID chat è: {chat_id}')

        @self.bot.message_handler(commands=['start'])
        def handle_start(message: Message):
            """
            Handle the /start command by sending a welcome message.
            
            :param message: The message object containing the command.
            """
            logging.debug(f"Received /start command from chat ID: {message.chat.id}")
            self.bot.reply_to(message, 'Ciao! Benvenuto nel devbot di Telegram, scrivi se hai bisogno di aiuto sul mondo della programmazione.')

        @self.bot.message_handler(commands=['help'])
        def handle_help(message: Message):
            """
            Handle the /help command by sending a help message.
            
            :param message: The message object containing the command.
            """
            logging.debug(f"Received /help command from chat ID: {message.chat.id}")
            self.bot.reply_to(message, 'Questo bot ti aiuta con il mondo della programmazione.')

        @self.bot.message_handler(commands=['assistenza'])
        def handle_assistenza(message: Message):
            """
            Handle the /assistenza command to start an assistance session.
            
            :param message: The message object containing the command.
            """
            user_id = message.chat.id
            self.assistenza_sessions[user_id] = {
                'user_chat_id': user_id,
                'active': True,
                'last_forwarded_message_id': None
            }

            # Creazione dei bottoni
            keyboard = types.ReplyKeyboardMarkup(row_width=1)
            close_button = types.KeyboardButton('Chiudi sessione')
            keyboard.add(close_button)

            logging.debug(f"Started assistance session for chat ID: {user_id}")
            self.bot.send_message(user_id, 'Sei in contatto con il supporto. Invia i tuoi messaggi e ti risponderemo al più presto.', reply_markup=keyboard)

        @self.bot.message_handler(func=lambda message: message.chat.id in self.assistenza_sessions)
        def forward_to_group(message: Message):
            """
            Forward user messages to the group chat during an active assistance session.
            
            :param message: The message object containing the user's message.
            """
            user_id = message.chat.id
            if self.assistenza_sessions[user_id]['active']:
                logging.debug(f"Forwarding message from chat ID: {user_id} to group chat ID: {self.group_chat_id}")
                forwarded_message = self.bot.forward_message(self.group_chat_id, user_id, message.message_id)
                self.assistenza_sessions[user_id]['last_forwarded_message_id'] = forwarded_message.message_id

        @self.bot.message_handler(commands=['stopassistenza'])
        def handle_stop_assistenza(message: Message):
            """
            Handle the /stopassistenza command to stop an assistance session.
            
            :param message: The message object containing the command.
            """
            user_id = message.chat.id
            if user_id in self.assistenza_sessions:
                del self.assistenza_sessions[user_id]
                logging.debug(f"Stopped assistance session for chat ID: {user_id}")
                self.bot.reply_to(message, 'Sessione di assistenza terminata.')
            else:
                logging.debug(f"No active assistance session for chat ID: {user_id}")
                self.bot.reply_to(message, 'Non sei attualmente in una sessione di assistenza.')

        @self.bot.message_handler(commands=['staffstopassistenza'])
        def handle_staff_stop_assistenza(message: Message):
            """
            Handle the /staffstopassistenza command to stop an assistance session by staff.
            
            :param message: The message object containing the command.
            """
            if message.reply_to_message and message.reply_to_message.forward_from:
                user_id = message.reply_to_message.forward_from.id
                if user_id in self.assistenza_sessions:
                    self.assistenza_sessions[user_id]['active'] = False
                    logging.debug(f"Staff terminated assistance session for chat ID: {user_id}")
                    self.bot.send_message(message.chat.id, f"La sessione di assistenza dell'utente {user_id} è stata terminata dallo staff.")
                    self.bot.send_message(user_id, 'La tua sessione di assistenza è stata terminata dallo staff. Grazie per averci contattato!')
            else:
                logging.debug(f"Staffstopassistenza command received without valid forwarded message.")
                self.bot.reply_to(message, 'Per favore, rispondi ad un messaggio inoltrato per terminare la sessione di assistenza.')

        @self.bot.message_handler(func=lambda message: message.chat.id == self.group_chat_id)
        def forward_to_user(message: Message):
            """
            Forward messages from the group chat to the appropriate user.
            
            :param message: The message object containing the group's message.
            """
            if message.reply_to_message and message.reply_to_message.forward_from:
                user_id = message.reply_to_message.forward_from.id
                if user_id in self.assistenza_sessions:
                    logging.debug(f"Forwarding message from group chat ID: {self.group_chat_id} to user chat ID: {user_id}")
                    self.bot.forward_message(user_id, self.group_chat_id, message.message_id)

import logging

class Commands:
    def __init__(self, bot_connect) -> None:
        self.bot_connect = bot_connect
        
        @self.bot_connect.message_handler(commands=["example"])
        def handle_example(message: str) -> None:
                self.bot_connect.reply_to(message, "Questo è un esempio di comando personalizzato.")
                logging.debug("Esempio di comando personalizzato eseguito.")
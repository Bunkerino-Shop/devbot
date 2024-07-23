import os
import importlib.util
import logging
from dotenv import load_dotenv

from Misc.Variables import SUPPORT_GROUP_ID, assistenza_sessions
from Bot.BotConnect import BotConnect

def create_logger() -> None:
    logging.basicConfig(
        filename="log.log",
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
)

def get_token_from_env() -> str:
    logging.debug("Getting token from .env file")
    load_dotenv()
    return os.getenv("TOKEN", "")

def main() -> None:
    create_logger()
    try:
        token = get_token_from_env()
        bot = BotConnect(token)
        bot.create_telebot()
        logging.info("Bot created")
    except Exception as e:
        logging.error(f"Error while creating bot: {e}")
        exit(1)
    bot.start_polling()
    

if __name__ == "__main__":
    main()
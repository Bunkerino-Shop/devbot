import logging
import importlib.util
import os

from telebot import TeleBot
from Commands.Commands import Commands

class BotConnect:
    def __init__(self, token: str):
        """
        Initialize the BotConnect object with the token provided"""
        self.token = token
        self.bot = None
        
        logging.getLogger().setLevel(logging.DEBUG)
        
    def create_telebot(self):
        """
        Create a TeleBot object with the token provided"""
        try:
            self.bot = TeleBot(self.token)
            logging.debug("TeleBot object created successfully")
        except Exception as e:
            logging.error(f"Error creating TeleBot object: {e}")
            
    def start_polling(self):
        """
        Start polling the bot"""
        try:
            self.bot.polling()
            logging.debug("Bot started polling")
        except Exception as e:
            logging.error(f"Error starting polling: {e}")


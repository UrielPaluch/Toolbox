import logging
from logging.handlers import BufferingHandler, MemoryHandler
import os
from datetime import datetime
import yaml
import time

class MyLogger():
    def __init__(self, bot_name: str, capacity: int = 20, testing : bool = True) -> None:
        """Inicializa el logger

        Parameters
        ----------

        testing : bool
            Referencia el ambiente
        """
        self.capacity = capacity
        self.testing = testing
        self.logger = logging.getLogger(__name__)
        self.path_to_log_file = self.get_path_to_log_file(bot_name)
        
        file_handler = logging.FileHandler(self.path_to_log_file)
        formatter = logging.Formatter("%(asctime)s :: [%(levelname)s] :: %(funcName)s :: %(lineno)d :: %(message)s")
        file_handler.setFormatter(formatter)
        handler = MemoryHandler(self.capacity, target=file_handler)
        # handler.setFormatter(formatter)
        
        self.logger.addHandler(handler)
        # self.logger.addHandler(file_handler)
        self.logger.setLevel(logging.DEBUG)
    
    def get_path_to_log_file(self, bot_name: str):
        """Devuelve el path al archivo de logging"""

        # Check if the logs folder exists, and if not, create it
        if not os.path.exists('./logs'):
            os.makedirs('./logs')

        # Get the file paths for testing and production.
        if self.testing:
            path = f"./logs/testing_{bot_name}_{datetime.today().strftime('%Y-%m-%d_%H-%M')}.log"
        else:
            path = f"./logs/{bot_name}_{datetime.today().strftime('%Y-%m-%d')}.log"
        
        return path
    
    def log(self, message, level=logging.INFO):
        self.logger.log(level, message)

    def flush(self):
        for handler in self.logger.handlers:
            handler.flush()
            handler.close()

if __name__ == '__main__':
    logger = MyLogger('bot_name', capacity=5)
    for i in range(10):
        logger.log(f'Message {i}', level=logging.DEBUG)
        time.sleep(1)
    logger.flush()
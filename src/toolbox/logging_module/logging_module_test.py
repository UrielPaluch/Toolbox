import logging
from logging.handlers import BufferingHandler, MemoryHandler
import os
from datetime import datetime
import yaml
import time

class MyBatchLogger():
    def __init__(self, bot_name: str, capacity: int, testing : bool = True) -> None:
        """Inicializa el logger

        Parameters
        ----------
        bot_name: str
            Nombre del bot

        capacity : int
            Cantidad de mensajes que se guardan en memoria antes de escribirlos en el archivo de log

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
    
    def get_path_to_log_file(self, bot_name: str) -> str:
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

class MyNormalLogger():
    def __init__(self, bot_name: str, testing : bool = True) -> None:
        """Inicializa el logger

        Parameters
        ----------
        bot_name: str
            Nombre del bot

        testing : bool
            Referencia el ambiente
        """
        self.testing = testing
        self.logger = logging.getLogger(__name__)
        self.path_to_log_file = self.get_path_to_log_file(bot_name)
        
        file_handler = logging.FileHandler(self.path_to_log_file)
        formatter = logging.Formatter("%(asctime)s :: [%(levelname)s] :: %(funcName)s :: %(lineno)d :: %(message)s")
        file_handler.setFormatter(formatter)
        
        self.logger.addHandler(file_handler)
        self.logger.setLevel(logging.DEBUG)
    
    def get_path_to_log_file(self, bot_name: str) -> str:
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

if __name__ == '__main__':
    # Testing speed difference between both loggers.
    N = 10000
    tic = time.time()
    logger = MyBatchLogger('batch', capacity=N//2)
    for i in range(N):
        logger.log(f'Message {i}'*10, level=logging.DEBUG)
    logger.flush()
    toc = time.time()
    print(f'Batch Logger: {toc - tic:.2f}s')

    tic = time.time()
    logger = MyNormalLogger('normal')
    for i in range(N):
        logger.log(f'Message {i}'*10, level=logging.DEBUG)
    toc = time.time()
    print(f'Normal Logger: {toc - tic:.2f}s')
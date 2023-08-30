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
        formatter = logging.Formatter("%(asctime)s :: %(funcName)s :: %(lineno)d :: %(message)s")
        file_handler.setFormatter(formatter)
        handler = MemoryHandler(self.capacity, target=file_handler)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)
    def get_path_to_log_file(self, bot_name: str) -> str:
        """
        Devuelve el path al archivo de logging
        """
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
        formatter = logging.Formatter("%(asctime)s :: %(funcName)s :: %(lineno)d :: %(message)s")
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

def test_time_difference(n: int, cap: int, message_length: int = 100):
    """
    Test the time difference between the batch logger and the normal logger.
    
    Parameters
    ----------
    n : int
        Number of messages to log.
    cap: int
        Capacity of the batch logger.
    message_length: int
        Length of the message to log.
    """
    tic = time.time()
    logger = MyBatchLogger('batch', capacity=cap)
    for i in range(n):
        logger.log('L'*message_length, level=logging.DEBUG)
    toc1 = time.time()
    logger.flush()
    toc2 = time.time()
    batch_log_time = toc2 - tic
    batch_flush_time = toc2 - toc1

    tic = time.time()
    logger = MyNormalLogger('normal')
    for i in range(n):
        logger.log('L'*message_length, level=logging.DEBUG)
    toc = time.time()
    normal_logger_time_difference = toc - tic

    return (batch_log_time, batch_flush_time), normal_logger_time_difference

if __name__ == '__main__':
    # Testing speed difference between both loggers.
    (batch_log_time, batch_flush_time), normal_time = test_time_difference(n=400000, cap=5000)
    batch_time = batch_log_time + batch_flush_time

    print(f'Batch Logger: log time {batch_log_time*1000:.0f}ms, flush time {batch_flush_time*1000:.0f}ms')
    print(f'Normal Logger: {normal_time*1000:.0f}ms')
    print(f'Batch Logger is {normal_time/batch_time:.2f} times faster than the normal logger.')

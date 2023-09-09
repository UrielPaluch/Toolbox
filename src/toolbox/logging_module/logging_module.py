"""
Module for logging.

Classes
-------
BaseLogger
    Base Logger class with common methods.

BatchLogger
    Batch Logger class with BaseLogger methods, and it's own flush method.

NormalLogger
    Regular Logger class with BaseLogger methods.
"""

from datetime import datetime
import logging
from logging.handlers import MemoryHandler
import os


class BaseLogger:
    """
    Base Logger class with common methods.

    Parameters
    ----------
    logger_name : str
        Name of the logger.

    bot_name : str
        Name of the bot.

    testing : bool
        Indicates the environment.

    Methods
    -------
    get_path_to_log_file(bot_name)
        Returns the path to the log file.

    format_log_message(message)
        Formats the message.

    info(message)
        Logs the message in memory with info level.

    debug(message)
        Logs the message in memory with error level.

    warning(message)
        Logs the message in memory with warning level.

    error(message)
        Logs the message in memory with error level.

    critical(message)
        Logs the message in memory with critical level.
    """

    def __init__(self, logger_name: str, bot_name: str, testing: bool) -> None:
        self.testing = testing
        self.path_to_log_file = self.get_path_to_log_file(bot_name)
        self.logger = logging.getLogger(logger_name)

    def get_path_to_log_file(self, bot_name: str) -> str:
        """
        Returns the path to the log file.
        """
        # Check if the logs folder exists, and if not, create it
        log_dir = "./logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Get the file paths for testing and production.
        if self.testing:
            path = f"{log_dir}/testing_{bot_name}_{datetime.today().strftime('%Y-%m-%d_%H-%M-%S')}.log" #pylint: disable=line-too-long
        else:
            path = f"{log_dir}/{bot_name}_{datetime.today().strftime('%Y-%m-%d')}.log"
        return path

    def format_log_message(self, message):
        """
        Formatea el mensaje.

        Ejemplo de formato de salida:

        "17:31:09.289737 :: Esta en PRODUCCION"

        Parameters
        ----------
        message : str
            Mensaje a formatear.
        """

        message = datetime.now().strftime("%H:%M:%S.%f") + " :: " + message
        return message

    def info(self, message: str) -> None:
        """
        Loggea el mensaje en memoria con nivel info.

        Parameters
        ----------
        message : str
            Mensaje a loggear.
        """

        self.logger.info(self.format_log_message(message))

    def debug(self, message: str) -> None:
        """
        Loggea el mensaje en memoria con nivel error.

        Parameters
        ----------
        message : str
            Mensaje a loggear.
        """

        self.logger.debug(self.format_log_message(message))

    def warning(self, message: str) -> None:
        """
        Loggea el mensaje en memoria con nivel warning.

        Parameters
        ----------
        message : str
            Mensaje a loggear.
        """

        self.logger.warning(self.format_log_message(message))

    def error(self, message: str) -> None:
        """
        Loggea el mensaje en memoria con nivel error.

        Parameters
        ----------
        message : str
            Mensaje a loggear.
        """

        self.logger.error(self.format_log_message(message))

    def critical(self, message: str) -> None:
        """
        Loggea el mensaje en memoria con nivel critical.

        Parameters
        ----------
        message : str
            Mensaje a loggear.
        """

        self.logger.critical(self.format_log_message(message))


class BatchLogger(BaseLogger):
    """
    Batch Logger class with BaseLogger methods, and it's own flush method.
    The logger uses a MemoryHandler to write the messages in memory to the log
    file when the capacity is reached.

    Parameters
    ----------
    bot_name : str
        Name of the bot.

    capacity : int
        Amount of messages to be stored in memory before writing them to the
        log file.

    testing : bool
        Indicates the environment.

    Methods
    -------
    get_path_to_log_file(bot_name)
        Returns the path to the log file.

    format_log_message(message)
        Formats the message.

    info(message)
        Logs the message in memory with info level.

    debug(message)
        Logs the message in memory with error level.

    warning(message)
        Logs the message in memory with warning level.

    error(message)
        Logs the message in memory with error level.

    critical(message)
        Logs the message in memory with critical level.

    flush()
        Writes the messages in memory to the log file.

    """

    def __init__(self, bot_name: str, capacity: int, testing: bool) -> None:
        """Inicializa el logger

        Parameters
        ----------
        bot_name: str
            Nombre del bot

        capacity : int
            Cantidad de mensajes que se guardan en memoria antes de escribirlos
            en el archivo de log

        testing : bool
            Referencia el ambiente
        """
        super().__init__(logger_name="batch_logger", bot_name=bot_name, testing=testing)
        self.capacity = capacity
        self.logger = logging.getLogger("batch_logger")
        file_handler = logging.FileHandler(self.path_to_log_file)
        handler = MemoryHandler(self.capacity, target=file_handler)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)

    def flush(self):
        """
        Escribe los mensajes en memoria en el archivo de log
        """
        for handler in self.logger.handlers:
            handler.flush()
            handler.close()


class NormalLogger(BaseLogger):
    """
    Regular Logger class with BaseLogger methods.
    The logger uses a file handler to write the messages to the log file, as soon
    as they are logged.

    Parameters
    ----------
    bot_name : str
        Name of the bot.

    testing : bool
        Indicates the environment.

    Methods
    -------
    get_path_to_log_file(bot_name)
        Returns the path to the log file.

    format_log_message(message)
        Formats the message.

    info(message)
        Logs the message in memory with info level.

    debug(message)
        Logs the message in memory with error level.

    warning(message)
        Logs the message in memory with warning level.

    error(message)
        Logs the message in memory with error level.

    critical(message)
        Logs the message in memory with critical level.
    """

    def __init__(self, bot_name: str, testing: bool) -> None:
        """Inicializa el logger

        Parameters
        ----------
        bot_name: str
            Nombre del bot

        testing : bool
            Referencia el ambiente
        """
        super().__init__(
            logger_name="sequential_logger", bot_name=bot_name, testing=testing
        )
        file_handler = logging.FileHandler(self.path_to_log_file)
        self.logger.addHandler(file_handler)
        self.logger.setLevel(logging.DEBUG)

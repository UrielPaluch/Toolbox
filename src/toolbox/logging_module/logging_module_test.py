import logging
from logging.handlers import MemoryHandler
import os
from datetime import datetime
import timeit

class MyBaseLogger():
    """
    Base Logger class with common methods.
    """
    def __init__(self, bot_name: str, testing: bool) -> None:
        self.testing = testing
        self.path_to_log_file = self.get_path_to_log_file(bot_name)

    def get_path_to_log_file(self, bot_name: str) -> str:
        """
        Returns the path to the log file.
        """
        # Check if the logs folder exists, and if not, create it
        log_dir = './logs'
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Get the file paths for testing and production.
        if self.testing:
            path = f"{log_dir}/testing_{bot_name}_{datetime.today().strftime('%Y-%m-%d_%H-%M')}.log"
        else:
            path = f"{log_dir}/{bot_name}_{datetime.today().strftime('%Y-%m-%d')}.log"
        return path

class MyBatchLogger(MyBaseLogger):
    """
    Logger que guarda los mensajes en memoria hasta que se llena la capacidad, \
    y luego los escribe en el archivo de log.
    """
    def __init__(self, bot_name: str, capacity: int, testing: bool) -> None:
        """Inicializa el logger

        Parameters
        ----------
        bot_name: str
            Nombre del bot

        capacity : int
            Cantidad de mensajes que se guardan en memoria antes de escribirlos \
            en el archivo de log

        testing : bool
            Referencia el ambiente
        """
        super().__init__(bot_name, testing)
        self.capacity = capacity
        self.logger = logging.getLogger('batch_logger')
        file_handler = logging.FileHandler(self.path_to_log_file)
        formatter = logging.Formatter("%(asctime)s :: %(funcName)s :: %(lineno)d :: %(message)s")
        file_handler.setFormatter(formatter)
        handler = MemoryHandler(self.capacity, target=file_handler)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)

    def log(self, message, level=logging.INFO):
        """
        Loggea el mensaje en memoria
        """
        self.logger.log(level, message)

    def flush(self):
        """
        Escribe los mensajes en memoria en el archivo de log
        """
        for handler in self.logger.handlers:
            handler.flush()
            handler.close()

class MyNormalLogger(MyBaseLogger):
    """
    Logger que escribe los mensajes en el archivo de log a medida que se van \
    recibiendo.
    """
    def __init__(self, bot_name: str, testing : bool) -> None:
        """Inicializa el logger

        Parameters
        ----------
        bot_name: str
            Nombre del bot

        testing : bool
            Referencia el ambiente
        """
        super().__init__(bot_name, testing)
        self.logger = logging.getLogger('sequential_logger')
        file_handler = logging.FileHandler(self.path_to_log_file)
        formatter = logging.Formatter("%(asctime)s :: %(funcName)s :: %(lineno)d :: %(message)s")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.setLevel(logging.DEBUG)

    def log(self, message, level=logging.INFO):
        """
        Loggea el mensaje en el archivo de log
        """
        self.logger.log(level, message)

def test_time_difference(n_logs: int, cap: int, message_length: int = 100):
    """
    Testea la diferencia en velocidad entre el BatchLogger y el NormalLogger.

    Parámetros
    ----------
    n_logs: int
        Número de mensajes para loggear.
    def test_time_difference(n_logs: int, cap: int, message_length: int = 100):
    cap: int
        Capacidad del BatchLogger.
    message_length: int
        Longitud del mensaje a Loggear.
    """
    # Batch logger
    tic = timeit.default_timer()
    logger = MyBatchLogger('batch', capacity=cap, testing=True)
    for _ in range(n_logs):
        logger.log('L'*message_length, level=logging.DEBUG)
    toc1 = timeit.default_timer()
    logger.flush()
    toc2 = timeit.default_timer()
    batch_log_time_diff = toc2 - tic
    batch_flush_time_diff = toc2 - toc1

    # Normal logger
    tic = timeit.default_timer()
    logger = MyNormalLogger('normal', testing=True)
    for _ in range(n_logs):
        logger.log('L'*message_length, level=logging.DEBUG)
    toc = timeit.default_timer()
    normal_logger_time_diff = toc - tic



    return (batch_log_time_diff, batch_flush_time_diff), normal_logger_time_diff

if __name__ == '__main__':
    # Testing speed difference between both loggers.
    (batch_log_time, batch_flush_time), normal_time = test_time_difference(
        n_logs=400000, cap=50000
    )
    batch_time = batch_log_time + batch_flush_time

    print(f'Batch Logger: log time {batch_log_time*1000:.0f}ms, flush time {batch_flush_time*1000:.0f}ms')
    print(f'Normal Logger: {normal_time*1000:.0f}ms')
    print(f'Batch Logger is {normal_time/batch_time:.2f} times faster than the normal logger.')

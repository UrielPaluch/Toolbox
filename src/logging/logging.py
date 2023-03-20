# pylint: disable=missing-docstring, invalid-name
import logging
from logging import config
import logging.handlers
import os
from datetime import datetime
import yaml

def my_rotation_filename(self, default_name):
    """
    Modify the filename of a log file when rotating.

    This is provided so that a custom filename can be provided.

    The default implementation calls the 'namer' attribute of the
    handler, if it's callable, passing the default name to
    it. If the attribute isn't callable (the default is None), the name
    is returned unchanged.

    :param default_name: The default name for the log file.
    """

    if not callable(self.namer):
        result = default_name
    else:
        result = self.namer(default_name)

    elements = result.split(".")
    result = elements[0] + "_" + elements[2] + "." + elements[1]
    return result

def my_get_files_to_delete(self):
    """
    Determine the files to delete when rolling over.

    More specific than the earlier method, which just used glob.glob().
    """
    dir_name, base_name = os.path.split(self.baseFilename)
    app_name, extension = base_name.split(".") # pylint: disable=unused-variable
    file_names = os.listdir(dir_name)
    result = []
    prefix = app_name + "_"
    plen = len(prefix)
    for file_name in file_names:
        if file_name[:plen] == prefix:
            suffix = file_name[plen:]
            if self.extMatch.match(suffix):
                result.append(os.path.join(dir_name, file_name))
    if len(result) < self.backupCount:
        result = []
    else:
        result.sort()
        result = result[:len(result) - self.backupCount]
    return result

def new_file(configuration_file : dict, testing: bool, file_handler: str) -> str:
    """Crea un nuevo archivo y devuelve el nombre

    Parameters
    ----------

    configuration_file : dict
        Configuration file defined in config/logging.config.yaml
    testing : bool
        Referencia el ambiente
    file_handler : str
        Nombre del file_handler definido en el configuration file

    Returns
    -------
    str
        Nombre del archivo
    """
    path = configuration_file['handlers'][file_handler]['filename']
    white_space, file_name, extension = path.split(".") # pylint: disable=unused-variable
    if testing:
        result = "." + file_name + "_" + datetime.today().strftime('%Y-%m-%d_%H-%M') + "." + extension # pylint: disable=line-too-long
    else:
        result = "." + file_name + "_" + datetime.today().strftime('%Y-%m-%d') + "." + extension
    return result

def my_logger(testing : bool) -> None:
    """Inicializa el logger configurado especialmente para Tito

    Parameters
    ----------

    testing : bool
        Referencia el ambiente
    """
    with open('config/logging.config.yaml', 'r', encoding="utf-8") as f:
        config_file = yaml.safe_load(f.read())

        if testing is True:
            file_handler = 'file_handler_testing'
        else:
            file_handler = 'file_handler_prod'

        config_file['handlers'][file_handler]['filename'] = new_file(config_file,
                                                            testing,
                                                            file_handler)
        config.dictConfig(config_file)

logging.handlers.BaseRotatingHandler.rotation_filename = my_rotation_filename
logging.handlers.TimedRotatingFileHandler.getFilesToDelete = my_get_files_to_delete

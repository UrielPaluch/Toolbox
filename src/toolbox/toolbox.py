"""
    Define las funciones de la libreria
"""
import datetime
import numpy as np

def get_feriados_byma() -> list['str']:
    """
    Devuelve una lista de strings con fechas de todos los feriados de byma

    Returns
    ----------
    list[str]
        Lista de str con los dias feriados
    """
    feriados_byma = ['2023-02-20', '2023-02-21', '2023-03-24', '2023-04-06',
                     '2023-04-07', '2023-05-01', '2023-05-25', '2023-05-26',
                     '2023-06-19', '2023-06-20', '2023-08-21', '2023-10-13',
                     '2023-10-16', '2023-11-06', '2023-11-20', '2023-12-08', 
                     '2023-12-25']

    return feriados_byma

def calculo_plazo_liquidacion_48hs(hoy : datetime.date = datetime.date.today()) -> int:
    """ Plazo de liquidacion de 48hs en dias para el calculo de la tasa

    Parameters
    ----------
    hoy : datetime.date
        Fecha para calcular el plazo de liquidacion. Default: Hoy.

    Returns
    ----------
    int
        Proximo plazo de liquidacion en dias

    """
    # Los feriados tienen que estar en orden con el formato yyyy-mm-dd
    # Se extraen los feriados de https://www.byma.com.ar/servicios/calendario-bursatil/
    # para cargarlos en la variable feriados_byma
    feriados_byma = get_feriados_byma()

    dia_liquidacion = hoy

    count_dias_habiles = 0

    while count_dias_habiles < 2:
        dia_liquidacion = dia_liquidacion + datetime.timedelta(days = 1)

        if np.is_busday(dia_liquidacion, holidays = feriados_byma):
            count_dias_habiles += 1

    diff_days = dia_liquidacion - hoy

    return diff_days.days
def calculo_plazo_liquidacion_24hs(hoy : datetime.date = datetime.date.today()) -> int:
    """ Plazo de liquidacion en 24hs

    Parameters
    ----------
    hoy : datetime.date
        Fecha para calcular el plazo de liquidacion. Default: Hoy.

    Returns
    ----------
    int
        Proximo plazo de liquidacion en dias

    """
    # Los feriados tienen que estar en orden con el formato yyyy-mm-dd
    # Se extraen los feriados de https://www.byma.com.ar/servicios/calendario-bursatil/
    # para cargarlos en la variable feriados_byma
    feriados_byma = get_feriados_byma()
    dia_liquidacion = hoy + datetime.timedelta(days = 1)

    count_dias = 1

    while not np.is_busday(dia_liquidacion, holidays = feriados_byma):
        dia_liquidacion = dia_liquidacion + datetime.timedelta(days = 1)
        count_dias += 1

    return count_dias

def hay_mercado(hoy : datetime.date = datetime.date.today()) -> np.bool_:
    """ Devuelve si hay mercado

    Parameters
    ----------
    hoy : datetime.date
        Fecha para calcular el plazo de liquidacion. Default: Hoy.

    Returns
    -------
    np.bool_
        `True` si hay mercado, `False` en caso contrario.

    """
    # Los feriados tienen que estar en orden con el formato yyyy-mm-dd
    # Se extraen los feriados de https://www.byma.com.ar/servicios/calendario-bursatil/
    # para cargarlos en la variable feriados_byma
    feriados_byma = get_feriados_byma()

    return np.is_busday(hoy, holidays = feriados_byma)

def extract_price_size_values(my_dict: dict) -> "tuple[float, int]":
    """ Del dict con informacion que envia el mercado se extrae el precio y

    la cantidad

    Parameters
    ----------
    my_dict : dict
        Informacion que envia el mercado

    Returns
    -------
    tuple(precio: float, cantidad: int)
        precio y cantidad

    """

    key = list(my_dict.get('marketData').keys())[0] # type: ignore
    values = my_dict.get('marketData').get(key) # type: ignore

    # Si no hay bid
    # Puede traer una lista vacia o None en caso de que no haya
    if not values:
        price = 0
        size = 0
    # Si hay bid
    else:
        # Entonces tiene que haber precio y cantidad
        # Un detalle es el [0], porque devuelve una lista donde el primer
        # elemento es un diccionario
        price = values[0].get('price')
        size = values[0].get('size')

    return(price, size)

def extract_ticker_market_values(my_dict: dict) -> "tuple[str, str]":
    """ Del dict con informacion que envia el mercado se extrae el ticker y

    el market (48hs, 24hs, ci)

    Parameters
    ----------
    my_dict : dict
        Informacion que envia el mercado

    Returns
    -------
    tuple(ticker: str, market: str)
        ticker y market

    """
    ticker, market = (my_dict.get('instrumentId').get('symbol')[14:] # type: ignore
                                 .replace(" ", "").split("-"))

    return (ticker, market)

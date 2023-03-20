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
                     '2023-10-16', '2023-11-20', '2023-12-08', '2023-12-25']

    return feriados_byma

def calculo_plazo_liquidacion(hoy : datetime.date = datetime.date.today()) -> int:
    """ Plazo de liquidacion de 48hs en dias para el calculo de la tasa

    Returns
    ----------
    int
        Proximo plazo de liquidacion en dias

    """
    # Los feriados tienen que estar en orden con el formato yyyy-mm-dd
    # Se extraen los feriados de https://www.byma.com.ar/servicios/calendario-bursatil/
    # para cargarlos en la variable feriados_byma
    feriados_byma = ['2023-02-20', '2023-02-21', '2023-03-24', '2023-04-06',
                     '2023-04-07', '2023-05-01', '2023-05-25', '2023-05-26',
                     '2023-06-19', '2023-06-20', '2023-08-21', '2023-10-13',
                     '2023-10-16', '2023-11-20', '2023-12-08', '2023-12-25']

    dia_liquidacion = hoy

    count_dias_habiles = 0

    while count_dias_habiles < 2:
        dia_liquidacion = dia_liquidacion + \
                        datetime.timedelta(days = 1)

        if np.is_busday(dia_liquidacion, holidays = feriados_byma):
            count_dias_habiles += 1

    diff_days = dia_liquidacion - hoy

    return diff_days.days

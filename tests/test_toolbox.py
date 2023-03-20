# pylint: disable=missing-docstring
import datetime

from toolbox import get_feriados_byma
from toolbox import calculo_plazo_liquidacion

def test_get_feriados_byma():

    actual_return = get_feriados_byma()

    len_expected_return = 16

    assert len(actual_return) == len_expected_return, "Cantidad de feriados incorrectos"
    assert isinstance(actual_return, list), "El tipo de datos devuelto no es una lista"

test_get_feriados_byma()

def test_calculo_plazo_liquidacion():
    lunes = '2023-03-20'
    lunes_expected_return = 2
    lunes_actual_return = calculo_plazo_liquidacion(datetime.datetime.strptime(lunes,
                                                                               "%Y-%m-%d").date())

    assert lunes_expected_return == lunes_actual_return, "Fallo el lunes"

    jueves = '2023-03-30'
    jueves_expected_return = 4
    jueves_actual_return = calculo_plazo_liquidacion(datetime.datetime.strptime(jueves,
                                                                                "%Y-%m-%d").date())

    assert jueves_expected_return == jueves_actual_return, "Fallo el jueves"

    viernes = '2023-03-31'
    viernes_expected_return = 4
    viernes_actual_return = calculo_plazo_liquidacion(datetime.datetime.strptime(viernes,
                                                                                 "%Y-%m-%d").date())

    assert viernes_expected_return == viernes_actual_return, "Fallo el viernes"

    feriado = '2023-03-23'
    feriado_expected_return = 5
    feriado_actual_return = calculo_plazo_liquidacion(datetime.datetime.strptime(feriado,
                                                                                 "%Y-%m-%d").date())

    assert feriado_expected_return == feriado_actual_return, "Fallo el feriado"

test_calculo_plazo_liquidacion()

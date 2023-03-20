# pylint: disable=missing-docstring
import datetime

from toolbox import get_feriados_byma
from toolbox import calculo_plazo_liquidacion
from toolbox import hay_mercado
from toolbox import extract_price_size_values


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

def test_hay_mercado():
    lunes = '2023-03-20'
    lunes_expected_return = True
    lunes_actual_return = hay_mercado(datetime.datetime.strptime(lunes, "%Y-%m-%d").date())

    assert lunes_expected_return == lunes_actual_return, "Fallo el lunes"

    sabado = '2023-03-18'
    jueves_expected_return = False
    jueves_actual_return = hay_mercado(datetime.datetime.strptime(sabado, "%Y-%m-%d").date())

    assert jueves_expected_return == jueves_actual_return, "Fallo el sabado"

    domingo = '2023-03-19'
    viernes_expected_return = False
    viernes_actual_return = hay_mercado(datetime.datetime.strptime(domingo, "%Y-%m-%d").date())

    assert viernes_expected_return == viernes_actual_return, "Fallo el domingo"

    feriado = '2023-03-24'
    feriado_expected_return = False
    feriado_actual_return = hay_mercado(datetime.datetime.strptime(feriado, "%Y-%m-%d").date())

    assert feriado_expected_return == feriado_actual_return, "Fallo el feriado"

test_hay_mercado()

def test_extract_price_size_values():

    no_values = {
        'type': 'Md',
        'timestamp': 1679278806883,
        'instrumentId': {'marketId': 'ROFX', 'symbol': 'MERV - XMEV - MIRG - CI'},
        'marketData': {'OF': None}
    }

    no_values_expected_return = (0, 0)

    no_values_actual_return = extract_price_size_values(no_values)

    assert no_values_expected_return == no_values_actual_return, "Fallo no_values"

    of_values = {
        'type': 'Md',
        'timestamp': 1679278806885,
        'instrumentId': {'marketId': 'ROFX', 'symbol': 'MERV - XMEV - GOOGL - CI'},
        'marketData': {
            'OF': [{'price': 150.0, 'size': 1}]
        }
    }

    of_values_expected_return = (150.0, 1)

    of_values_actual_return = extract_price_size_values(of_values)

    assert of_values_expected_return == of_values_actual_return, "Fallo of_values"

    bid_values = {
        'type': 'Md',
        'timestamp': 1679278806885,
        'instrumentId': {'marketId': 'ROFX', 'symbol': 'MERV - XMEV - AMZN - 48hs'},
        'marketData': {
            'BI': [{'price': 200.0, 'size': 1}]
        }
    }

    bid_values_expected_return = (200.0, 1)

    bid_values_actual_return = extract_price_size_values(bid_values)

    assert bid_values_expected_return == bid_values_actual_return, "Fallo of_values"

test_extract_price_size_values()
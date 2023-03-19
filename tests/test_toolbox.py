# pylint: disable=missing-docstring

from toolbox import get_feriados_byma

def test_get_feriados_byma():

    actual_return = get_feriados_byma()

    len_expected_return = 16

    assert len(actual_return) == len_expected_return, "Cantidad de feriados incorrectos"
    assert isinstance(actual_return, list), "El tipo de datos devuelto no es una lista"


test_get_feriados_byma()

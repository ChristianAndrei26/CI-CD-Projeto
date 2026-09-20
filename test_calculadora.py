
from feature.calculadora import soma


def test_soma_positivos():
    assert soma(2, 3) == 5


def test_soma_negativos():
    assert soma(-2, -3) == -5


def test_soma_com_zero():
    assert soma(10, 0) == 10


def test_soma_positivo_negativo():
    assert soma(10, -4) == 6


def test_soma_numeros_decimais():
    assert soma(2.5, 3.5) == 6.0


def test_soma_numeros_grandes():
    assert soma(1000000, 2000000) == 3000000

from feature.calculadora import soma


def test_soma():
    assert soma(2, 3) == 5


def test_soma_negativos():
    assert soma(-2, -3) == -5


def test_soma_com_zero():
    assert soma(10, 0) == 10

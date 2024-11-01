
import pytest

from otros.calculadora import es_resultado_negativo, multiplicar, dividir


def test_es_resultado_negativo():
    # Casos donde el resultado debe ser negativo
    assert es_resultado_negativo(-5, 3) is True
    assert es_resultado_negativo(4, -7) is True
    
    # Casos donde el resultado debe ser positivo
    assert es_resultado_negativo(5, 3) is False
    assert es_resultado_negativo(-2, -8) is False

def test_multiplicar():
    # Multiplicación con números positivos
    assert multiplicar(3.421, 3.922) == 12
    assert multiplicar(7.11, 2.1) == 14

    # Multiplicación con un número negativo
    assert multiplicar(-3.477, 4.1) == -12
    assert multiplicar(5, -2) == -10

    # Multiplicación de dos números negativos
    assert multiplicar(-5, -3) == 15

    # Multiplicación con cero
    assert multiplicar(0, 5) == 0
    assert multiplicar(3, 0) == 0

def test_dividir():
    # División con números positivos
    assert dividir(9.33, 3.122) == 3
    assert dividir(14.757, 4.968) == 3

    # División con un número negativo
    assert dividir(-12, 3) == -4
    assert dividir(14.223, -2) == -7

    # División de dos números negativos
    assert dividir(-15.899, -4.499) == 4

    # División con redondeo a entero
    assert dividir(10, 3.101) == 3  # 10 // 3 = 3 (redondeo esperado)

    # División por cero
    with pytest.raises(ZeroDivisionError):
        dividir(5, 0)

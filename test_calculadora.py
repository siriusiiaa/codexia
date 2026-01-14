"""
Tests para el módulo calculadora
"""

import pytest
from calculadora import sumar, restar, multiplicar, dividir, potencia, raiz_cuadrada


def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0
    assert sumar(100, 200) == 300


def test_restar():
    assert restar(5, 3) == 2
    assert restar(10, 10) == 0
    assert restar(0, 5) == -5
    assert restar(-3, -2) == -1


def test_multiplicar():
    assert multiplicar(3, 4) == 12
    assert multiplicar(0, 5) == 0
    assert multiplicar(-2, 3) == -6
    assert multiplicar(-2, -3) == 6


def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(15, 3) == 5
    assert dividir(7, 2) == 3.5
    assert dividir(-10, 2) == -5


def test_dividir_por_cero():
    with pytest.raises(ValueError, match="No se puede dividir por cero"):
        dividir(10, 0)


def test_potencia():
    assert potencia(2, 3) == 8
    assert potencia(5, 2) == 25
    assert potencia(10, 0) == 1
    assert potencia(2, -1) == 0.5


def test_raiz_cuadrada():
    assert raiz_cuadrada(4) == 2
    assert raiz_cuadrada(9) == 3
    assert raiz_cuadrada(0) == 0
    assert raiz_cuadrada(2) == pytest.approx(1.414, rel=0.01)


def test_raiz_cuadrada_numero_negativo():
    with pytest.raises(ValueError, match="No se puede calcular la raíz cuadrada de un número negativo"):
        raiz_cuadrada(-1)
